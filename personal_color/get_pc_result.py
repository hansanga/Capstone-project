import dlib
import cv2
from imutils import face_utils
import numpy as np
import os
from tensorflow.keras.models import load_model
from sklearn.externals import joblib
import warnings
warnings.filterwarnings('ignore')

def count_faces(img):
    detector = dlib.get_frontal_face_detector()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    if len(rects) == 0:
        print('No face detected')
        return True
    elif len(rects) > 1:
        print('More than 1 face detected')
        return True
    else:
        False

def get_pc_result(diag_file='image.jpg', n_colors=4):

    wc_model = load_model('models/warm_cool.h5')
    warm_model = joblib.load('models/warm.pkl')
    cool_model = joblib.load('models/cool.pkl')

    features = create_diag_features(diag_file, n_colors)
    wc_result = wc_model.predict(features)
    print('wc_result:', wc_result)
    
    if wc_result == 0:
        result = cool_model.predict(features)
    else:
        result = warm_model.predict(features)
    print('result:', result)
        
    if wc_result <= .5:
        if result < .5:
            result = 'spr'
        else:
            result = 'fal'        
    else:
        if result <= .5:
            result = 'sum'
        else:
            result = 'win'
            
    print('Diag result:', result)
    os.remove(diag_file)
    
    return result
