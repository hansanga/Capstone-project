import subprocess
import threading
import platform
import win32ui
from PIL import Image, ImageWin


printer_name = 'DS-RX1'
dpi = 300

image_path = 'C:/Users/pomat/Capstone-project/results/qr_img.jpg' if platform.system() == 'Windows' \
    else '/home/colorlog/Capstone-project/results/qr_img.jpg'


def print_image():

    # Create a printer device context (DC)
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)

    bmp = Image.open(image_path)
    hdc.StartDoc(image_path)
    hdc.StartPage()
    dib = ImageWin.Dib(bmp)

    dib.draw(hdc.GetHandleOutput(), (0, 0, dpi*6+20, dpi*4+15))
    hdc.EndPage()
    hdc.EndDoc()
    hdc.DeleteDC()
                

# 비동기로 프린트 작업을 실행하는 함수
def print_image_async():
    threading.Thread(target=print_image).start()
