from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
import Main_Ui
from frame_and_qr import frame_and_qr
import cv2
import camera
import sys
import time
from philips_hue import control_hue

def crop_and_resize_frame(frame, crop_width, crop_height, img_size):
    original_height, original_width = frame.shape[:2]
    center_x = original_width // 2
    center_y = original_height // 2

    left = int(center_x - crop_width // 2)
    top = int(center_y - crop_height // 1.8)
    right = int(center_x + crop_width // 2)
    bottom = int(center_y + crop_height // 2.3)

    cropped_frame = frame[top:bottom, left:right]
    resized_frame = cv2.resize(cropped_frame, img_size)
    return resized_frame

class ColorLog(QMainWindow, Main_Ui.Ui_ColorLog):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # Stacked Widget을 처음 화면으로 돌리기
        self.stackedWidget.setCurrentIndex(0)

        self.show()

        # 선택된 조명버튼, 프레임
        self.selected_button = None
        self.selected_frame = None
        self.selected_button_color = ""

        # 필립스휴 연결
        self.hue = control_hue.Hue()
        # self.hue.connect()
        # self.hue.set_color_tone('default')

        # 기본 폰트 설정
        self.default_font = QFont()
        self.default_font.setFamily("KoPubWorld돋움체 Medium")
        self.default_font.setPointSize(18)

        # 선택된 폰트 설정
        self.selected_font = QFont()
        self.selected_font.setFamily("KoPubWorld돋움체 Bold")
        self.selected_font.setPointSize(18)

        # 조명 버튼 원래 위치 지정
        self.button_positions = {
            'select1': 510,
            'select2': 845,
            'select3': 1180,
        }

        # 프레임 원래 위치 지정
        self.frame_positions = {
            'color1': 140,
            'color2': 400,
            'color3': 660,
        }

        # 카메라 촬영 타이머 설정
        self.num_timer = QTimer(self)
        self.num_timer.timeout.connect(self.delayed_check)
        self.num_timer.start(5000)

        # 사진 찍는 횟수 0으로 초기화
        self.num_value = 0
        self.num2_value = 0

        # 대기화면 타이머 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.remaining_time = 30
        self.remaining_time_5 = 80  # page5

        # 카메라 타이머 설정
        self.camera_timer = QTimer(self)
        self.camera_timer.timeout.connect(self.update_frame)
        # self.frame_gen, self.cap = camera.get_camera_frame()
        # self.camera_timer.start(30)
        self.cap = None
        self.frame_gen = None
        self.out = None

        # 페이지 변경 시그널 연결
        self.stackedWidget.currentChanged.connect(self.on_page_changed)

    #--------------------------------------------------------

    # 기본 버튼 조작

    def NextBtn(self):
        self.goToNextPage()
        QSound.play('./touch_sound.wav')

    def goToNextPage(self):
        currentIndex = self.stackedWidget.currentIndex()
        nextIndex = (currentIndex + 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(nextIndex)
        print(nextIndex)

        # 인덱스가 마지막에서 처음으로 돌아갈 때 변수 초기화
        if nextIndex == 0:
            self.reset_selections()

    def reset_selections(self):
        # 선택된 조명 버튼 초기화
        if self.selected_button is not None:
            self.selected_button.setStyleSheet("background-color: {}; border-radius: 110px; border: 1px solid #c8c8c8;".format(self.selected_button_color))
            self.selected_button_text.setFont(self.default_font)
            initial_position = self.button_positions[self.selected_button.objectName()]
            self.selected_button.setGeometry(QtCore.QRect(initial_position + 10, 340, 230, 230))
            self.selected_button = None
            self.selected_button_color = ""

        # 선택된 프레임 초기화
        if self.selected_frame is not None:
            self.selected_frame.setStyleSheet("border: 2px solid #c8c8c8")
            initial_position = self.frame_positions[self.selected_frame.objectName()]
            self.selected_frame.setGeometry(QtCore.QRect(initial_position, 410, 191, 191))
            self.selected_frame = None

        # 기타 초기화 작업
        self.personalColor.clear()
        self.recoColor.clear()

    # 조명 선택 버튼
    def SelectBtn(self, btn_number):

        # 선택 X 버튼은 초기화
        if self.selected_button is not None:
            self.selected_button.setStyleSheet("background-color: {}; border-radius: 110px; border: 1px solid #c8c8c8;".format(self.selected_button_color))
            self.selected_button_text.setFont(self.default_font)
            initial_position = self.button_positions[self.selected_button.objectName()]
            self.selected_button.setGeometry(QtCore.QRect(initial_position+10, 340, 230, 230))

        # 선택된 버튼 스타일 적용
        if btn_number == 1:
            self._select_button(self.select1, self.select_1, "#e63412", 'spr1', 500, 330, btn_number)
        elif btn_number == 2:
            self._select_button(self.select2, self.select_2, "#ffe300", 'spr2', 835, 330, btn_number)
        elif btn_number == 3:
            self._select_button(self.select3, self.select_3, "#ff7b89", 'spr3', 1170, 330, btn_number)

    def _select_button(self, button, button_text, color, tone, x, y, btn_number):
        self.selected_button = button
        print(f"selected button is {btn_number}")
        self.selected_button_text = button_text
        self.selected_button_color = color
        self.hue.set_color_tone(tone)
        button_text.setFont(self.selected_font)
        button.setStyleSheet(f"background-color: {color}; border-radius: 110px; border: 9px solid #c8c8c8;")
        button.setGeometry(QtCore.QRect(x, y, 250, 250))

    # 프레임 선택 버튼
    def SelectFrame(self, frame_number):

        # 선택 X 프레임은 초기화
        if self.selected_frame is not None:
            self.selected_frame.setStyleSheet("border: 2px solid #c8c8c8")
            initial_position = self.frame_positions[self.selected_frame.objectName()]
            self.selected_frame.setGeometry(QtCore.QRect(initial_position, 410, 191, 191))

        # 선택된 프레임 (테두리 두껍게, 크기 약간 키우기)
        if frame_number == 1:
            self._select_frame(self.color1, 130, 400, 'spr', frame_number)
        elif frame_number == 2:
            self._select_frame(self.color2, 390, 400, 'sum', frame_number)
        elif frame_number == 3:
            self._select_frame(self.color3, 650, 400, 'fal', frame_number)


    def _select_frame(self, frame, x, y, frame_result, frame_number):
        self.selected_frame = frame
        print(f"selected frame is {frame_number}")
        frame.setStyleSheet("border: 4px solid #c8c8c8")
        frame.setGeometry(QtCore.QRect(x, y, 211, 211))
        new_img = frame_and_qr(frame_result)
        new_img.save("final_photo.jpg")
        self.finalPhoto.setPixmap(QPixmap("final_photo.jpg").scaled(self.finalPhoto.size(), Qt.KeepAspectRatio))
        self.finalPhoto2.setPixmap(QPixmap("final_photo.jpg").scaled(self.finalPhoto.size(), Qt.KeepAspectRatio))

    #----------------------------------------------------------------

    # 퍼스널진단 결과 받기
    def process_result(self, frame_result):
        Index = self.stackedWidget.currentIndex()
        if Index == 5:
            result = frame_result  # 'frame_result' 값을 사용하여 'result' 값을 설정

            if result == 'spr':
                myColor = "봄 웜톤"
                palette_image = "palette_spring.png"
            elif result == 'sum':
                myColor = "여름 쿨톤"
                palette_image = "palette_summer.png"
            elif result == 'fal':
                myColor = "가을 웜톤"
                palette_image = "palette_autumn.png"
            elif result == 'win':
                myColor = "겨울 쿨톤"
                palette_image = "palette_winter.png"
            else:
                myColor = "알 수 없음"
                palette_image = None

            self.personalColor.setText(QCoreApplication.translate("ColorLog", myColor, None))

            if palette_image:
                self.recoColor.setPixmap(QPixmap(palette_image).scaled(self.recoColor.size(), Qt.KeepAspectRatio))
            else:
                self.recoColor.clear()

    #----------------------------------------------------------------

    # page3(진단용 사진) & page7(네컷용 사진)

    def delayed_check(self):
        Index = self.stackedWidget.currentIndex()
        if Index == 3:
            QTimer.singleShot(4000, self.update_num)
        elif Index == 7:
            QTimer.singleShot(5000, self.update_num)

    # 카메라 페이지(5초마다 사진찍고 숫자 올라가게하기)

    def update_num(self):
        Index = self.stackedWidget.currentIndex()
        if Index == 3:
            self.num_value += 1
            if self.num_value >= 2:  # 2가 되면 다음 페이지로 넘어감
                self.goToNextPage()
                return
            QSound.play('./camera_sound.wav')
            self.capture_photo(index=3)

            QTimer.singleShot(1000, lambda: self.num.setText(QCoreApplication.translate("ColorLog", f"{self.num_value} / 1", None)))
            self.delayed_check()

        elif Index == 7:
            self.num2_value += 1
            if self.num2_value >= 5:  # 5가 되면 다음 페이지로 넘어감
                self.goToNextPage()
                self.hue.end_program()
                return
            
            QSound.play('./camera_sound.wav')
            self.capture_photo(index=7)

            QTimer.singleShot(1000, lambda: self.num_2.setText(QCoreApplication.translate("ColorLog", f"{self.num2_value} / 4", None)))
            # self.delayed_check()

    #----------------------------------------------------------------

    # 30초간의 타이머 작동

    # 타이머가 있는 페이지로 이동할 때 타이머 시작
    def on_page_changed(self, index):
        if index in [1, 2, 6, 8, 5]:  # 타이머가 있는 페이지 인덱스로 변경
            self.start_timer(index)
        else:
            self.timer.stop()

        # 3번 페이지에서 카메라 시작, 다른 페이지에서는 카메라 중지
        if index == 3 or index == 7 or index == 2:
            self.start_camera()
        else:
            self.stop_camera()

    def start_timer(self, index):
        if index == 5:
            self.remaining_time_5 = 80
        else:
            self.remaining_time = 30
        self.timer.start(1000)  # 1000ms = 1s

    # 타이머 작동
    def update_timer(self):
        currentIndex = self.stackedWidget.currentIndex()
        # page5는 80초
        if currentIndex == 5 and self.remaining_time_5 > 0:
            self.remaining_time_5 -= 1
            self.pushButton_5.setText(QCoreApplication.translate("ColorLog", f"{self.remaining_time_5} \u2192", None))
            if self.remaining_time_5 == 0:
                self.timer.stop()
                self.goToNextPage()
        # 나머지 페이지들은 30초
        elif self.remaining_time > 0:
            self.remaining_time -= 1
            if currentIndex == 1:
                self.timer_1.setText(QCoreApplication.translate("ColorLog", str(self.remaining_time), None))
            elif currentIndex == 2:
                self.timer_2.setText(QCoreApplication.translate("ColorLog", str(self.remaining_time), None))
            elif currentIndex == 6:
                self.timer_3.setText(QCoreApplication.translate("ColorLog", str(self.remaining_time), None))
            elif currentIndex == 8:
                self.timer_4.setText(QCoreApplication.translate("ColorLog", str(self.remaining_time), None))
            if self.remaining_time == 0:
                self.timer.stop()
                if self.selected_button is None:
                    self.SelectBtn(1)
                if self.selected_frame is None:
                    self.SelectFrame(1)  # 아무것도 선택되지 않으면 1번 프레임 선택
                self.goToNextPage()

    #----------------------------------------------------------------

    # 카메라 화면에 띄우기
    def start_camera(self):
        self.frame_gen, self.cap, self.out = camera.get_camera_frame()
        self.camera_timer.start(30)

    def stop_camera(self):
        self.camera_timer.stop()
        if self.cap:
            camera.release_camera(self.cap, self.out)
            self.cap = None
            self.out = None

    @pyqtSlot()
    def update_frame(self):
        currentIndex = self.stackedWidget.currentIndex()
        try:
            frame = next(self.frame_gen)

            # index가 7일 때만 비디오 녹화
            if currentIndex == 7:
                self.out.write(frame)

            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            if currentIndex == 2:
                self.camera.setPixmap(QtGui.QPixmap.fromImage(convert_to_Qt_format))
            elif currentIndex == 3:
                self.camera2.setPixmap(QtGui.QPixmap.fromImage(convert_to_Qt_format))
            elif currentIndex == 7:
                self.camera3.setPixmap(QtGui.QPixmap.fromImage(convert_to_Qt_format))
        except StopIteration:
            self.camera_timer.stop()

    def closeEvent(self, event):
        self.camera_timer.stop()
        if self.cap and self.out:
            camera.release_camera(self.cap, self.out)
        event.accept()

    def capture_photo(self, index):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                # 자르기 및 크기 조정
                crop_width = 582
                crop_height = 325
                img_size = (890, 625)
                frame = crop_and_resize_frame(frame, crop_width, crop_height, img_size)

                if index == 3:
                    img_name = f"photo_0.jpg"
                    cv2.imwrite(img_name, frame)
                    print(f"{img_name} saved")
                    self.facePhoto.setPixmap(QPixmap(img_name).scaled(self.facePhoto.size(), Qt.KeepAspectRatio))
                elif index == 7:
                # 비디오 녹화
                    self.out.write(frame)
                    img_name = f"photo_{self.num2_value}.jpg"
                    cv2.imwrite(img_name, frame)
                    print(f"{img_name} saved")

#----------------------------------------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ColorLog()
    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Exiting with error: {e}")
