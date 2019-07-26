### Adaptive threshold
import cv2

image2 = cv2.imread('sudoku.png',0)
th6 = cv2.adaptiveThreshold(image2 , 155 , cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,5)
th7 = cv2.adaptiveThreshold(image2 , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,5)

cv2.imshow('image2',image2)
cv2.imshow('th6',th6)
cv2.imshow('th7',th7)

cv2.waitKey(0) 

cv2.destroyAllWindows()

