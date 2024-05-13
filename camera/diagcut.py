import cv2
from check_face import *
import dlib
import time

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()
ret, frame = cap.read()

def check_face(diag_file='photo.jpg'):
    detector = dlib.get_frontal_face_detector()
    img = cv2.imread(diag_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    if len(faces) == 0:
        return False
    return True
    
def capture(diag_file):
    cv2.imwrite(diag_file, frame)

def run(diag_file='photo.jpg'):
    flag = 0
    
    # TODO: 단장할 시간
    # def see_mirror():
    
    if not flag:
        capture(diag_file)
        print('진단용 사진을 촬영하였습니다.')
    else:
        while not check_face(diag_file):
            flag += 1
            capture(diag_file)
            print(f"얼굴이 감지되지 않았습니다. 남은 기회: {3-flag}번")
            if flag == 3:
                print("3번 이상 얼굴 감지에 실패했습니다. 프로그램을 종료합니다.")
                cap.release()
                exit()
            print('3초 후 다시 촬영합니다.')
    cap.release()