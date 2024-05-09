import dlib
import cv2
from imutils import face_utils
from color_palette import *
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.externals import joblib
import warnings
warnings.filterwarnings('ignore')

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

photo = None
diag_file = 'photo.jpg '

wc_model = load_model('warm_cool.h5')
warm_model = joblib.load('warm.pkl')
cool_model = joblib.load('cool.pkl')

while photo == None:
    # take photo
    img = cv2.imread(diag_file)
    try:
        faces = detector(img)
        if len(faces) == 1:
            photo = img
        else:
            print('No face detected or too many faces detected. Please retake the photo.')
    except:
        print('No face detected or too many faces detected. Please retake the photo.')

h, w = photo.shape[:2]
face = detector(photo)[0]
face = photo[max(0, face.top()):min(face.bottom(), h), max(0, face.left()):min(face.right(), w)]
features = create_diag_features(diag_file, face)

wc_result = wc_model.predict(features)
if wc_result == 0:
    result = cool_model.predict(features)
else:
    result = warm_model.predict(features)
    
if wc_result == 0:
    if result == 0:
        result = 'sum'
    elif result == 1:
        result = 'win'
elif wc_result == 1:
    if result == 0:
        result = 'spr'
    elif result == 1:
        result = 'fal'
print(result)

# TODO: insert palette on the result photo
# TODO: send info to server