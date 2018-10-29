# -*- coding: utf-8 -* 
import cv2

img=cv2.imread('timg.jpeg',cv2.IMREAD_COLOR)

cv2.imshow('lena',img)

print img.shape # 图片分辨率(747,1024)
k=cv2.waitKey(0)
