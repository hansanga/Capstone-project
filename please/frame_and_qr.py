from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import datetime as dt

# 사진 밝기 높이기
def increase_brightness(image, value):
    factor = 1 + value / 255
    return ImageEnhance.Brightness(image).enhance(factor)

# 프레임 만들기
def frame_and_qr(result):
    t_img1 = Image.open("D:\Project\ColorLog_ui\d\photo_1.jpg")
    t_img2 = Image.open("D:\Project\ColorLog_ui\d\photo_2.jpg")
    t_img3 = Image.open("D:\Project\ColorLog_ui\d\photo_3.jpg")
    t_img4 = Image.open("D:\Project\ColorLog_ui\d\photo_4.jpg")

    img_size = (600, 425)

    img1 = increase_brightness(t_img1, 50)
    img2 = increase_brightness(t_img2, 80)
    img3 = increase_brightness(t_img3, 80)
    img4 = increase_brightness(t_img4, 50)

    img1 = img1.resize(img_size)
    img2 = img2.resize(img_size)
    img3 = img3.resize(img_size)
    img4 = img4.resize(img_size)

    if(result == 'spr'):
        frame_color = '#DFFFD9'
    elif(result == 'sum'):
        frame_color = '#C6D1FF'
    elif(result == 'fal'):
        frame_color = '#D6F5FF'
    elif(result == 'win'):
        frame_color = '#42075D'

    new_img = Image.new("RGB", (1500, 1000), frame_color)
    new_img.paste(img1, (50, 50))
    new_img.paste(img2, (img_size[0] + 100, 50))
    new_img.paste(img3, (50, img_size[1] + 100))
    new_img.paste(img4, (img_size[0] + 100, img_size[1] + 100))

    # watermark
    waterFont = ImageFont.truetype("D:\Project\ColorLog_ui\d\SokchoBadaDotum.ttf", 60)
    waterdraw = ImageDraw.Draw(new_img)
    bbox = waterdraw.textbbox((0, 0), 'Colorlog', font=waterFont)
    mark_width, mark_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    watermark = Image.new('RGBA', (mark_width, mark_height+130), (0, 0, 0, 0))
    waterdraw = ImageDraw.Draw(watermark)
    waterdraw.text((0, 0), 'Colorlog', fill='black', font=waterFont)
    watermark = watermark.rotate(90, expand=1)

    new_img.paste(watermark, ((img_size[0]*2) + 100 + 10, 1000 - 50 - 10 - 10 - mark_width), watermark)

    # datestr
    time = dt.datetime.now()
    datestr = time.strftime('%Y/%m/%d')
    dateFont = ImageFont.truetype("D:\Project\ColorLog_ui\d\SokchoBadaDotum.ttf", 30)
    draw = ImageDraw.Draw(new_img)
    bbox = draw.textbbox((0, 0), datestr, font=dateFont)
    date_width, date_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    datemark = Image.new('RGBA', (date_width, date_height+130), (0, 0, 0, 0))
    datedraw = ImageDraw.Draw(datemark)
    datedraw.text((0, 0), datestr, fill='black', font=dateFont)
    datemark = datemark.rotate(90, expand=1)

    new_img.paste(datemark, ((img_size[0]*2) + 100 + 10 + mark_height + 10, 1000 - 50 - 10 - 10 - date_width), datemark)
    # print("이미지 저장 중...")
    # new_img.save("merged_img.jpg", "JPEG")

    return new_img

# frame_and_qr 함수를 호출하여 이미지를 생성하고 저장합니다.
result = 'spr'  # 프레임 색상에 대한 결과값, 여기서는 임의로 'spr'을 사용했습니다.
frame_and_qr_result = frame_and_qr(result)
