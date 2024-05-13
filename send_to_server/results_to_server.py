import requests
import asyncio

url = 'http://192.168.0.75:8080/api/photogroup/photogroup_upload'

image_paths = ['../results/1.jpg', '../results/2.jpg', '../results/3.jpg', '../results/4.jpg']
video_path = '../results/1.mp4'

files = {}

for i, image_path in enumerate(image_paths):
    files['photo_' + str(i)] = open(image_path, 'rb')
files['video'] = open(video_path, 'rb')

other_data = {
    'user_id': 5,
    'season': 'spring',
    'frame':1
}

async def send_request():
    try:
        response = await requests.post(url, files=files, data=other_data)
        print(response.text)
    except Exception as e:
        print(f'에러 발생: {e}')
        
asyncio.run(send_request())