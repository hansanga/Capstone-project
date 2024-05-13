from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import datetime as dt
import qrcode
import requests

def increase_brightness(image, value):
	factor = 1 + value / 255
	return ImageEnhance.Brightness(image).enhance(factor)

def frame_and_qr(result):
    t_img1 = Image.open("/home/colorlog/ver1/photo_0.jpg")
    t_img2 = Image.open("/home/colorlog/ver1/photo_1.jpg")
    t_img3 = Image.open("/home/colorlog/ver1/photo_2.jpg")
    t_img4 = Image.open("/home/colorlog/ver1/photo_3.jpg")

    crop_width = 582
    crop_height = 325

    # 원본 이미지의 크기를 구합니다.
    original_width, original_height = t_img1.size

    center_x = original_width // 2
    center_y = original_height // 2

    # 가운데를 기준으로 이미지를 자릅니다.
    left = int(center_x - crop_width // 2)
    top = int(center_y - crop_height // 1.8)
    right = int(center_x + crop_width // 2)
    bottom = int(center_y + crop_height // 2.25)

    img1 = t_img1.crop((left, top, right, bottom))
    img2 = t_img2.crop((left, top, right, bottom))
    img3 = t_img3.crop((left, top, right, bottom))
    img4 = t_img4.crop((left, top, right, bottom))

    img_size = (600, 425)

    img1 = increase_brightness(img1, 20)
    img2 = increase_brightness(img2, 20)
    img3 = increase_brightness(img3, 20)
    img4 = increase_brightness(img4, 20)

    img1 = img1.resize(img_size)
    img2 = img2.resize(img_size)
    img3 = img3.resize(img_size)
    img4 = img4.resize(img_size)

    if(result == 'spr'):
        frame_color = '#F8E0EC'
    elif(result == 'sum'):
        frame_color = '#E0F2F7'
    elif(result == 'fal'):
        frame_color = '#81543F'
    elif(result == 'win'):
        frame_color = '#42075D'

    new_img = Image.new("RGB", (1500, 1000), frame_color)
    new_img.paste(img1, (50,50))
    new_img.paste(img2, (img_size[0] + 100, 50))
    new_img.paste(img3, (50, img_size[1] + 100))
    new_img.paste(img4, (img_size[0] + 100, img_size[1] + 100))

    #make QR code
    spring_server_url = "http://192.168.0.75:8080/api/user/qr-code"

    try:
        # 스프링 서버로 GET 요청 보내기
        response = requests.get(spring_server_url)

        # 응답 확인
        if response.status_code == 200:
            # 링크를 가져옴
            qr_code_link = response.json()["link"]

            # QR 코드 생성
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=1,
                border=1,
            )
            qr.add_data(qr_code_link)
            qr.make(fit=True)

            # QR 코드 이미지 저장
            qr_img = qr.make_image(fill_color="black", back_color="white")
            qr_img.save("QRCodeImg.jpg")
            print("QR 코드 생성 완료")
        else:
            print("Failed to get link from Spring server. Status code:", response.status_code)
    except Exception as e:
        print("Error getting link from Spring server:", str(e))

    qrcode = Image.open("./QRCodeImg.jpg")
    qrcode = qr_img.resize((130,130))
    new_img.paste(qrcode, ((img_size[0]*2) + 100 + 10, 1000 - 50 - 130))

    #watermark
    waterFont = ImageFont.truetype('/home/colorlog/Freesentation-7Bold.ttf', 60)
    mark_width, mark_height = waterFont.getsize('Colorlog')
    watermark = Image.new('RGBA', (mark_width, mark_height), (0, 0, 0, 0))
    waterdraw = ImageDraw.Draw(watermark)
    waterdraw.text((0,0), 'Colorlog', fill='#F8F5F8', font=waterFont)
    watermark = watermark.rotate(90,expand=1)

    new_img.paste(watermark, ((img_size[0]*2) + 100 + 10, 1000 - 50 - 130 - 20 - mark_width), watermark)

    #datestr
    time = dt.datetime.now()
    datestr = time.strftime('%Y/%m/%d')
    dateFont = ImageFont.truetype('/home/colorlog/Freesentation-7Bold.ttf', 30)
    date_width, date_height = dateFont.getsize(datestr)
    datemark = Image.new('RGBA', (date_width, date_height), (0, 0, 0, 0))
    datedraw = ImageDraw.Draw(datemark)
    datedraw.text((0,0), datestr, fill='black', font=dateFont)
    datemark = datemark.rotate(90,expand=1)

    new_img.paste(datemark, ((img_size[0]*2) + 100 + 10 + mark_height + 10, 1000 - 50 - 130 - 20 - date_width), datemark)


    new_img.save("merged_img.jpg","JPEG")


    # 스프링 서버의 엔드포인트 URL
    server_url = 'http://192.168.0.75:8080/api/photogroup/photogroup_upload'


    # 이미지 파일들의 경로
    image_path = './merged_img.jpg'

    # 동영상 파일의 경로
    video_path = '/home/colorlog/ver1/output.avi'

    try:
        # 파일들을 전송할 딕셔너리
        files = {

            'video': open(video_path, 'rb'), # 동영상 파일 전송
            'image': open(image_path, 'rb')  # 이미지 파일 전송
        }

        # POST 요청 보내기
        response = requests.post(server_url, files=files)

        # 응답 확인
        if response.status_code == 200:                                                               print('Photo group uploaded successfully.')
        else:
            print(f'Failed to upload photo group. Status code: {response.status_code}')
    except Exception as e:
        print('Error uploading photo group:', str(e))


    # 사진 파일 삭제
    for i in range(4):
        image_path = f"/home/colorlog/ver1/photo_{i}.jpg"
        if os.path.exists(image_path):
            os.remove(image_path)

    if os.path.exists(video_path):
        os.remove(video_path)
