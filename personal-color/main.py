import dlib
import cv2
from color_palette import PaletteCreator
from analysis import PersonalColor

# TODO: load model

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# TODO: extract colors

face_processor = PaletteCreator(detector, predictor)
face_processor.create_palette()

# TODO: tone analysis

analysist = PersonalColor()
tone = analysist.analyze()

# TODO: send result to server
