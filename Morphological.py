import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('smarties.png',0)
image2 = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',image)
cv2.imshow('image2',image2)
cv2.waitKey(0)

cv2.destroyAllWindows()
