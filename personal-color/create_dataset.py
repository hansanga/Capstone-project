from color_palette import PaletteCreator

import cv2
import numpy as np
import pandas as pd
import os

pc = PaletteCreator()

data_root = '.'

def bgr2cmyk(bgr):
    b, g, r = bgr.T
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    k = min(c, m, y)
    c = (c - k) / (1 - k)
    m = (m - k) / (1 - k)
    y = (y - k) / (1 - k)
    if k == 1.0:
        c = m = y = 0
    else:
        k = 1 - k
    return np.array([c, m, y, k]).swapaxes(0, 2)

df = pd.DataFrame(columns=['H', 'S', 'V', 'L', 'A', 'B', 'C', 'M', 'Y', 'K', 'label'])

for folder in os.listdir(data_root):
    this_df = pd.DataFrame(columns=['H', 'S', 'V', 'L', 'A', 'B', 'C', 'M', 'Y', 'K', 'label'])
    
    for file in os.listdir(os.path.join(data_root, folder)):
        full_path = os.path.join(data_root, folder, file)
        
        img = cv2.imread(full_path)
        
        palette = pc.create_palette(full_path)
        palette = np.array([palette], np.uint8)
        
        hsv_palette = cv2.cvtColor(palette, cv2.COLOR_BGR2HSV)
        lab_palette = cv2.cvtColor(palette, cv2.COLOR_BGR2LAB)
        cmyk_palette = bgr2cmyk(palette)
        
        mean_hsv = np.mean(hsv_palette, axis=1)
        mean_lab = np.mean(lab_palette, axis=1)
        mean_cmyk = np.mean(cmyk_palette, axis=1)
        
        row = np.concatenate((mean_hsv, mean_lab, mean_cmyk), axis=1).tolist()
        row.append(folder)
        this_df[len(this_df)] = row
        
    this_df.to_csv(f'dataset/mean_{folder}.csv', index=False)
        
    pd.concat([df, this_df], axis=0)
    
df.to_csv('dataset/mean.csv', index=False)
        