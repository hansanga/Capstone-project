import dlib
import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model
import pickle
import warnings
from personal_color.color_palette import create_diag_features

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

    wc_model = load_model('models/warm_cool.h5', compile=False)
    
    cool_model = pickle.load(open('models/cool.pkl', 'rb'))
    warm_model = pickle.load(open('models/warm.pkl', 'rb'))

    features = create_diag_features(diag_file, n_colors)
    wc_result = wc_model.predict(features)[0][0]
    print('wc_result:', wc_result)
    
    if wc_result == 0:
        result = cool_model.predict(features)[0]
    else:
        result = warm_model.predict(features)[0]
    print('result:', result)
        
    if wc_result == 0:
        if result == 0:
            result = 'spr'
        else:
            result = 'fal'        
    else:
        if result == 0:
            result = 'sum'
        else:
            result = 'win'
            
    print('Diag result:', result)
    os.remove(diag_file)
    
    return result
