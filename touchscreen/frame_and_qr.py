from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import datetime as dt

# 사진 밝기 높이기
def increase_brightness(image, value):
    factor = 1 + value / 255
    return ImageEnhance.Brightness(image).enhance(factor)

# 프레임 만들기
def frame_and_qr(result):
    t_img1 = Image.open('/home/colorlog/Camera/photo_0.jpg')
    t_img2 = Image.open('/home/colorlog/Camera/photo_1.jpg')
    t_img3 = Image.open('/home/colorlog/Camera/photo_2.jpg')
    t_img4 = Image.open('/home/colorlog/Camera/photo_3.jpg')

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
    new_img.paste(img1, (50, 50))
    new_img.paste(img2, (img_size[0] + 100, 50))
    new_img.paste(img3, (50, img_size[1] + 100))
    new_img.paste(img4, (img_size[0] + 100, img_size[1] + 100))

    # watermark
    waterFont = ImageFont.truetype('/home/colorlog/Camera/Freesentation-7Bold.ttf', 60)
    mark_width, mark_height = waterFont.getsize('Colorlog')
    watermark = Image.new('RGBA', (mark_width, mark_height), (0, 0, 0, 0))
    waterdraw = ImageDraw.Draw(watermark)
    waterdraw.text((0,0), 'Colorlog', fill='#F8F5F8', font=waterFont)
    watermark = watermark.rotate(90,expand=1)

    new_img.paste(watermark, ((img_size[0]*2) + 100 + 10, 1000 - 50 - 130 - 20 - mark_width),    watermark)

    #datestr
    time = dt.datetime.now()
    datestr = time.strftime('%Y/%m/%d')
    dateFont = ImageFont.truetype('/home/colorlog/Camera/Freesentation-7Bold.ttf', 30)
    date_width, date_height = dateFont.getsize(datestr)
    datemark = Image.new('RGBA', (date_width, date_height), (0, 0, 0, 0))
    datedraw = ImageDraw.Draw(datemark)
    datedraw.text((0,0), datestr, fill='black', font=dateFont)
    datemark = datemark.rotate(90,expand=1)

    new_img.paste(datemark, ((img_size[0]*2) + 100 + 10 + mark_height + 10, 1000 - 50 - 130 - 20 - date_width), datemark)
    #print("이미지 저장 중...")
    #new_img.save("merged_img.jpg", "JPEG")

    return new_img

# frame_and_qr 함수를 호출하여 이미지를 생성하고 저장합니다.
result = 'spr'  # 프레임 색상에 대한 결과값, 여기서는 임의로 'spr'을 사용했습니다.
frame_and_qr_result = frame_and_qr(result)
