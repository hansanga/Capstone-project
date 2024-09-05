import os
import time
import subprocess
import threading
import platform

prefix = '/home/colorlog/Capstone-project' if platform.system() == 'Linux' else 'C:/Users/pomat/Capstone-project'

# 프린터 IP 주소 설정 (예: 192.168.1.100)
printer_ip = "192.168.0.88"
# printer_ip = 'EPSON_L6170_Series'
printer_name = 'something'

# 출력할 이미지 경로 설정 (예: /home/jetson/image.jpg)
image_path = os.path.join(prefix, "results/qr_img.jpg")

# 커맨드 실행 함수
def run_command(command):
    if platform.system() == 'Linux':
        subprocess.call(command, shell=True)
    elif platform.system() == 'Windows':
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        return stdout, stderr

# 이미지 출력 함수
def print_image():
    if platform.system() == 'Linux':
        # 이미지를 CUPS 프린터 큐에 추가
        run_command(f"lp -o media=Custom.4x6in -o scaling=fit-page -o media=GlossyPhotoPaper -o job-name='10x15cm_Photo' {image_path}")
        # 프린터 재시작 (필요한 경우)
        run_command(f"ping {printer_ip} -c 1 > /dev/null && echo && lpadmin -p {printer_ip} -E")
        
    elif platform.system() == 'Windows':
        run_command(f"rundll32 %systemroot%\system32\shimgvw.dll,ImageView_PrintTo {image_path} {printer_name}")
        run_command(f"ping {printer_ip} -n 1")

    # 프린트 작업 진행 확인
    while True:
        if platform.system() == 'Linux':
            status = run_command(f"lpq -P {printer_ip} | grep 'completed'")
            if status:
                print("프린트 작업 완료")
                break
            else:
                print("프린트 작업 진행 중...")
                time.sleep(5)
        elif platform.system() == 'Windows':
            stdout, stderr = run_command(f"powershell -command Get-PrintJob -PrinterName {printer_name} | Select-String 'Completed'")
            if not stdout:  # If there's no output, assume the queue is empty
                print('Print job completed')
                break
            else:
                print('Print job in progress...')
                time.sleep(5)

# 비동기로 프린트 작업을 실행하는 함수
def print_image_async():
    threading.Thread(target=print_image).start()
