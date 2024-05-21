import camera.frame_and_qr as frame_and_qr
from camera import fourcuts, diagcut
from personal_color.get_pc_result import get_pc_result
from philips_hue import control_hue

import threading
import cv2
import time

def capture_photos():
    global count
    now = time.time()
    while count < 4:
        if time.time() - now >= 5:
            cuts.run(count)
            now = time.time()
            count += 1

# 필립스휴 연결하고 흰색으로 설정
hue = control_hue.Hue()
hue.connect()
hue.set_color_tone('default')

# 진단용 사진 촬영
diagcut.run()
cv2.destroyAllWindows()

# 진단 수행
res = get_pc_result(diag_file='photo.jpg', n_colors=4)

# TODO 진단에 맞는 옵션 조명 색상 중 하나 선택
res = 

# 필립스휴 색조 설정
hue.set_color_tone(res)

cuts = fourcuts.FourCuts()
count = 0
photo_thread = threading.Thread(target=capture_photos)
photo_thread.start()

photo_thread.join()
cuts.end_program()

# 필립스휴 다시 흰색으로 설정
control_hue.set_color_tone('default')

# TODO: 프레임 디자인 선택
res = 

# 진단 결과에 맞는 프레임에 이미지와 QR 코드를 넣어서 저장 & 서버로 전송
frame_and_qr.frame_and_qr(result=res)

control_hue.end_program()