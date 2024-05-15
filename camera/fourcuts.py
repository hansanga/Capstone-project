import cv2
import time
import threading

class FourCuts():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('output.avi', self.fourcc, 20.0, (640, 480))
        self.lock = threading.Lock()
        
        if not self.cap.isOpened():
            print("카메라를 열 수 없습니다.")
            exit()

    def run(self, count):
        ret, frame = self.cap.read()
        
        # 비디오 녹화
        with self.lock:
            self.out.write(frame)
        
        # 5초마다 사진 촬영
        img_name = f"photo_{count}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} 저장됨")

        # 녹화된 비디오와 사진을 화면에 표시
        cv2.imshow('frame', frame)
        
    def end_program(self):
        # 모든 작업이 끝나면 자원 해제
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()
