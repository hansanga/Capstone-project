from phue import Bridge
import time

class Hue():
    def __init__(self, bridge_ip='192.168.0.73'):
        self.bridge_ip = bridge_ip
        
        self.b = Bridge(self.bridge_ip)
        self.b.connect()
        
        self.light_names = ['colorlog-더블팩', 'colorlog-더블팩2']
        self.lights = self.b.get_light_objects('name')
        
        self.color_settings = {
            'default' : {'hue': 0, 'sat': 0, 'bri': 254},
            'spr': {'hue': 56000, 'sat': 80, 'bri': 200},
            'sum': {'hue': 46920, 'sat': 180, 'bri': 200},
            'fal': {'hue': 6500, 'sat': 180, 'bri': 200},
            'win': {'hue': 51000, 'sat': 254, 'bri': 200}
        }

    def set_color_tone(self, tone):
        settings = self.color_settings.get(tone)
        if settings:
            for light_name in self.light_names:
                light = self.lights[light_name]
                if not light.on:
                    light.on = True
                    time.sleep(1)
                light.hue = settings['hue']
                light.saturation = settings['sat']
                light.brightness = settings['bri']
            print(f"{tone} 색상으로 모든 조명이 설정되었습니다.")
        else:
            print("올바른 색조가 아닙니다. 'spr', 'sum', 'fal', 'win' 중 하나여야 함")


    def end_program(self):
        for light_name in self.light_names:
            light = self.b.get_light_objects('name')[light_name]
            light.on = False
        print("모든 조명이 꺼졌습니다. 프로그램을 종료합니다.")
        