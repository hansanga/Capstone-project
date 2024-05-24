import os
import time
import subprocess

printer_ip = "192.168.0.88"

image_path = '/home/colorlog/Capstone-project/results/merged_img.jpg'

def run_command(command):
    subprocess.call(command, shell=True)

def print_photo():
    run_command(f"lp -o media=Letter -o scaling=fit-page -o media=GlossyPhotoPaper -o job-name='10x15cm_Photo' {image_path}")
    run_command(f"ping {printer_ip} -c 1 > /dev/null && echo && lpadmin -p {printer_ip} -E")

    while True:
        status = run_command(f"lpq -p {printer_ip} | grep 'completed'")
        if status:
            print("프린트 작업 완료")
            break
        else:
            print("프린트 작업 진행 중...")
            time.sleep(5)
