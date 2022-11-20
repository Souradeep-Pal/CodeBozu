import cv2
import numpy as np
import random


image=cv2.imread('Bozu.png')
h,w = image.shape[:2]
edit_img = np.zeros(image.shape)

colours=np.array([(0,0,255),(0,255,0),(255,0,0),(255,0,255),(0,255,255),(255,255,0),(255,51,255),(255,255,51),(51,255,255)])
ln=len(colours)
for i in range(h):
    s=random.randint(50,200)
    for p in range(s):
        if p+i<h:
            for j in range(w):
                s=random.randint(50,200)
                ran=random.randint(0,8)
                (b,g,r)=colours[ran]
                for q in range(s):
                    if q+j<w:
                        (B,G,R)=image[i,j]
                        edit_img[i+p,j+q,0] = 0 if B<1 else b
                        edit_img[i+p,j+q,1] = 0 if G<1 else g
                        edit_img[i+p,j+q,2] = 0 if R<1 else r
                j+=s
    i+=s

cv2.imwrite('Random_Bozu.jpg',edit_img)
