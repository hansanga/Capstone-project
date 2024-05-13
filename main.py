import camera.frame_and_qr as frame_and_qr
from camera import fourcuts, diagcut
from personal_color.get_pc_result import get_pc_result
import cv2

# 진단용 사진 촬영
diagcut.run()
cv2.destroyAllWindows()

# 진단 수행
res = get_pc_result(diag_file='photo.jpg', n_colors=4)

# TODO: 진단 결과에 맞는 색상조명 설정

# 진단 결과에 맞는 프레임에 이미지와 QR 코드를 넣어서 저장 & 서버로 전송
frame_and_qr.frame_and_qr(result=res)
