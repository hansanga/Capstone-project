import dlib
import cv2
from color_palette import PaletteCreator
from analysis import PersonalColor
import configparser
import yaml

parser = configparser.ConfigParser()

with open('config.yaml') as f:
    cfg = yaml.safe_load(f)

# TODO: load model

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# TODO: extract colors

face_processor = PaletteCreator(detector, predictor)
palette = face_processor.create_palette()

# TODO: tone analysis

analysist = PersonalColor(palette)
tone = analysist.analyze(cfg)

# TODO: send result to server
