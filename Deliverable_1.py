import cv2
import numpy as np

image=cv2.imread('Bozu.png')

def reddify(image):
    red_channel = image[:,:,2]
    red_img = np.zeros(image.shape)
    red_img[:,:,2] = red_channel
    cv2.imwrite('Red_Bozu.jpg',red_img) 
    return red_img
    
def greenify(image):
    green_channel = image[:,:,1]
    green_img = np.zeros(image.shape)
    green_img[:,:,1] = green_channel
    cv2.imwrite('Green_Bozu.jpg',green_img) 
    return green_img

def blueify(image):
    blue_channel = image[:,:,0]
    blue_img = np.zeros(image.shape)
    blue_img[:,:,0] = blue_channel
    cv2.imwrite('Blue_Bozu.jpg',blue_img) 
    return blue_img

def grayify(image):
    h,w=image.shape[:2]
    gray_img = np.zeros(image.shape)
    for i in range(h):
        for j in range(w):
            (B,G,R)=image[i,j]
            #print('R={},G={},B={}'.format(R,G,B))
            gray_img[i,j] = 0.2989*R + 0.5870*G + 0.1140*B
    cv2.imwrite('real_Gray_Bozu.jpg',gray_img)
    return gray_img

def negative(image):
    negative_img = 255-image
    cv2.imwrite('Negative_Bozu.jpg',negative_img)
    return negative_img

negative(image)