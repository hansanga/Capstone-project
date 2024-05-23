import cv2

def capture_frame(device_index=0):
    cap = cv2.VideoCapture(device_index, cv2.CAP_DSHOW)  # CAP_DSHOW is used for DirectShow backend on Windows

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return None

    ret, frame = cap.read()
    if not ret:
        print("프레임을 받을 수 없습니다.")
        return None

    return frame

def main():
    device_index = 1  # 사용할 카메라 장치 인덱스
    frame = capture_frame(device_index)

    if frame is not None:
        cv2.imshow("Captured Frame", frame)
        cv2.waitKey(0)  # 키 입력 대기
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
