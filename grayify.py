import cv2
import numpy as np

image=cv2.imread('rgb leaves.jpg')


h, w = image.shape[:2]
gray_img = np.zeros(image.shape)
for i in range(h):
    for j in range(w):
        (B, G, R) = image[i,j]
        gray_img[i, j] = 0.2989*R + 0.5870*G + 0.1140*B
cv2.imwrite('Gray.jpg', gray_img)
