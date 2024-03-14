import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import dlib
from imutils import face_utils


class PersonalColor:
    def __init__(self, detector, predictor, image_path='image.jpg', n_colors=6):
        self.img = cv2.imread(image_path)
        self.n_colors = n_colors

        self.detector = detector
        self.predictor = predictor

        self.right_eye = None
        self.left_eye = None
        self.left_cheek = None
        self.right_cheek = None
        self.lips = None
        self.nose = None

    def get_color_palette(self):
        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        img = img.reshape((img.shape[0] * img.shape[1], 3))

        kmeans = KMeans(n_clusters=self.n_colors)
        kmeans.fit(img)

        colors = kmeans.cluster_centers_
        colors = colors.astype(int)

        fig, axes = plt.subplots(1, len(colors), figsize=(15, 3))
        for ax, color in zip(axes, colors):
            ax.imshow([[color]])
            ax.axis('off')

        plt.savefig('color_palette.png', bbox_inches='tight', pad_inches=0)

    def detect_face_part(self):
        face_parts = [[] for _ in range(len(face_utils.FACIAL_LANDMARKS_IDXS))]

        faces = self.detector(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), 1)

        if not faces:
            # Handle the case where no face is detected
            print("No faces detected.")
            return

        rect = faces[0]

        shape = self.predictor(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), rect)
        shape = face_utils.shape_to_np(shape)

        for idx, (_, (i, j)) in enumerate(face_utils.FACIAL_LANDMARKS_IDXS.items()):
            # Exclude eyebrow landmarks (17-26 and 36-45)
            if idx not in [1, 3]:
                face_parts[idx] = shape[i:j]

        self.lips = self.extract_face_part(np.concatenate((shape[48:60], shape[60:68])))
        self.left_cheek = self.extract_face_part(np.concatenate((shape[29:33], shape[4:9])))
        self.right_cheek = self.extract_face_part(np.concatenate((shape[29:33], shape[10:15])))
        self.right_eye = self.extract_face_part(shape[36:42])
        self.left_eye = self.extract_face_part(shape[42:48])
        self.nose = self.extract_face_part(shape[27:36])

        cv2.imwrite('right_eye.png', self.right_eye)
        cv2.imwrite('left_eye.png', self.left_eye)
        cv2.imwrite('lips.png', self.lips)
        cv2.imwrite('left_cheek.png', self.left_cheek)
        cv2.imwrite('right_cheek.png', self.right_cheek)
        cv2.imwrite('nose.png', self.nose)

    def extract_face_part(self, face_part_points):

        (x, y, w, h) = cv2.boundingRect(face_part_points)
        crop = self.img[y:y+h, x:x+w]
        adj_points = np.array([np.array([p[0]-x, p[1]-y]) for p in face_part_points])

        # Create a mask
        mask = np.zeros((crop.shape[0], crop.shape[1]))
        cv2.fillConvexPoly(mask, adj_points, 1)
        mask = mask.astype(np.bool)
        crop[np.logical_not(mask)] = [255, 0, 0]

        return crop


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

face_processor = PersonalColor(detector, predictor)
face_processor.detect_face_part()
face_processor.get_color_palette()
