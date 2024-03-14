import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import dlib
from imutils import face_utils
from collections import Counter


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

        self.detect_face_part()
                
        self.right_eye = cv2.resize(self.right_eye, (self.right_eye.shape[0] * self.right_eye.shape[1], 1))
        self.left_eye = cv2.resize(self.left_eye, (self.left_eye.shape[0] * self.left_eye.shape[1], 1))
        self.lips = cv2.resize(self.lips, (self.lips.shape[0] * self.lips.shape[1], 1))
        self.left_cheek = cv2.resize(self.left_cheek, (self.left_cheek.shape[0] * self.left_cheek.shape[1], 1))
        self.right_cheek = cv2.resize(self.right_cheek, (self.right_cheek.shape[0] * self.right_cheek.shape[1], 1))
        self.nose = cv2.resize(self.nose, (self.nose.shape[0] * self.nose.shape[1], 1))
        
        cv2.imwrite('reshaped/right_eye.png', self.right_eye)
        cv2.imwrite('reshaped/left_eye.png', self.left_eye)
        cv2.imwrite('reshaped/lips.png', self.lips)
        cv2.imwrite('reshaped/left_cheek.png', self.left_cheek)
        cv2.imwrite('reshaped/right_cheek.png', self.right_cheek)
        cv2.imwrite('reshaped/nose.png', self.nose)
        
        stacked_images = np.hstack([self.right_eye, self.left_eye, self.lips, self.left_cheek, self.right_cheek, self.nose])
        stacked_images = stacked_images.reshape(-1, 3)
            
        kmeans = KMeans(n_clusters=6, n_init=10, random_state=42)
        kmeans.fit(stacked_images)

        cluster_centers = kmeans.cluster_centers_.astype(int)
            
        fig, axes = plt.subplots(1, len(cluster_centers), figsize=(15, 3))
        for ax, color in zip(axes, cluster_centers):
            img = np.full((1, 1, 3), color, dtype=np.uint8)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imwrite('img.png', img)
            ax.imshow(img)
            ax.axis('off')

        plt.savefig('color_palette.png', bbox_inches='tight', pad_inches=0)

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

        cv2.imwrite('orig/right_eye.png', self.right_eye)
        cv2.imwrite('orig/left_eye.png', self.left_eye)
        cv2.imwrite('orig/lips.png', self.lips)
        cv2.imwrite('orig/left_cheek.png', self.left_cheek)
        cv2.imwrite('orig/right_cheek.png', self.right_cheek)
        cv2.imwrite('orig/nose.png', self.nose)

    def extract_face_part(self, face_part_points):

        (x, y, w, h) = cv2.boundingRect(face_part_points)
        crop = self.img[y:y+h, x:x+w]
        
        return crop


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

face_processor = PersonalColor(detector, predictor)
face_processor.get_color_palette()
