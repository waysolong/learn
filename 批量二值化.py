import cv2
import os
import numpy as np
for i in range(11,56):
    location=(rf"C:\Users\Administrator\Desktop\data and img\proceed img\Sample011\img011-0{i}.png")
    img = cv2.imread(location)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 获取灰度图
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)  # 利用阈值自动选择的方法获取二值图像
    np.savetxt(rf'0{i}.txt', binary, fmt='%d', delimiter=' ')
c=np.loadtxt(r'011.txt')
print(c[0])