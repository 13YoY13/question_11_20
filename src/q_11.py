#11
import cv2 
import numpy as np
import matplotlib as plt

img = cv2.imread("imori.jpg")

img_smooth = cv2.blur(img, ksize=(3, 3))

cv2.imwrite("answers/img_smooth.jpg", img_smooth)