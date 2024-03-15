import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from imutils import face_utils
import dlib

class PaletteCreator:
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
        
    def save_palette(self, mean_colors):
        fig, axes = plt.subplots(1, len(mean_colors), figsize=(15, 3))
        for ax, color in zip(axes, mean_colors):
            img = np.full((1, 1, 3), color, dtype=np.uint8)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            ax.imshow(img)
            ax.axis('off')
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.margins(0,0)
        plt.savefig('images/palette.jpg', bbox_inches='tight', pad_inches=0)
        
    def extract_face_part(self, face_part_points):

        (x, y, w, h) = cv2.boundingRect(face_part_points)
        crop = self.img[y:y+h, x:x+w]
        
        # https://www.researchgate.net/publication/262371199_Explicit_image_detection_using_YCbCr_space_color_model_as_skin_detection
        # filter skin only (YCbCr)
        crop = cv2.cvtColor(crop, cv2.COLOR_BGR2YCrCb)
        mask = cv2.inRange(crop, np.array([0, 133, 77]), np.array([255, 173, 127]))
        crop = cv2.bitwise_and(crop, crop, mask=mask)
        crop = cv2.cvtColor(crop, cv2.COLOR_YCrCb2BGR)
        
        # Remove green pixels
        crop = crop[~np.all(crop == [0, 135, 0], axis=-1)]
        crop = crop.reshape(((1, crop.shape[0], 3)))
        
        return crop


    def detect_face_part(self):
        face_parts = [[] for _ in range(len(face_utils.FACIAL_LANDMARKS_IDXS))]

        faces = self.detector(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), 1)

        rect = faces[0]

        shape = self.predictor(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), rect)
        shape = face_utils.shape_to_np(shape)

        for idx, (_, (i, j)) in enumerate(face_utils.FACIAL_LANDMARKS_IDXS.items()):
            if idx not in [1, 3]:
                face_parts[idx] = shape[i:j]

        self.lips = self.extract_face_part(np.concatenate((shape[48:60], shape[60:68])))
        self.left_cheek = self.extract_face_part(np.concatenate((shape[29:33], shape[4:9])))
        self.right_cheek = self.extract_face_part(np.concatenate((shape[29:33], shape[10:15])))
        self.right_eye = self.extract_face_part(shape[36:42])
        self.left_eye = self.extract_face_part(shape[42:48])
        self.nose = self.extract_face_part(shape[27:36])

        cv2.imwrite('images/face_parts/right_eye.png', self.right_eye)
        cv2.imwrite('images/face_parts/left_eye.png', self.left_eye)
        cv2.imwrite('images/face_parts/lips.png', self.lips)
        cv2.imwrite('images/face_parts/left_cheek.png', self.left_cheek)
        cv2.imwrite('images/face_parts/right_cheek.png', self.right_cheek)
        cv2.imwrite('images/face_parts/nose.png', self.nose)
        
    def create_palette(self):

        self.detect_face_part()
        
        stacked_images = np.hstack([self.right_eye, self.left_eye, self.lips, self.left_cheek, self.right_cheek, self.nose])
        stacked_images = stacked_images.reshape(-1, 3)
            
        kmeans = KMeans(n_clusters=6, n_init=10, random_state=42)
        kmeans.fit(stacked_images)

        cluster_centers = kmeans.cluster_centers_.astype(int)
        
        self.save_palette(cluster_centers)
        
        # colors = []
        
        # for part in [self.right_eye, self.left_eye, self.lips, self.left_cheek, self.right_cheek, self.nose]:
        #     print(part.shape)
        #     part = part.reshape(-1, 3)
        #     print(part.shape)
        #     kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
        #     kmeans.fit(part)
        #     cluster_centers = kmeans.cluster_centers_
        #     colors.append(cluster_centers)
            
        # self.save_palette(colors)
        
        # return colors
        
        return cluster_centers


# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# face_processor = PaletteCreator(detector, predictor)
# face_processor.create_palette()
