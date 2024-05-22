# -*- coding: utf-8 -*-
import cv2

def get_camera_frame():
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

    # 비디오 녹화를 위한 설정 (XVID 코덱 사용, 초당 60프레임)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 60.0, (640, 480))

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return None, None, None

    def frame_generator():
        while True:
            ret, frame = cap.read()
            if not ret:
                print("프레임을 받을 수 없습니다. 종료합니다.")
                break
            yield frame

    return frame_generator(), cap, out

def release_camera(cap, out):
    if cap:
        cap.release()
    if out:
        out.release()
    cv2.destroyAllWindows()
