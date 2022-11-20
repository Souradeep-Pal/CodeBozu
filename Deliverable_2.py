import numpy as np
import cv2

image=cv2.imread('Bozu.png')

def horizontal_flip(image):
    h,w=image.shape[:2]
    hflip_img=np.zeros(image.shape)
    for i in range(h):
        for j in range(w):
            hflip_img[i,j]=image[i,w-j-1]
    return hflip_img

def vertical_flip(image):
    h,w=image.shape[:2]
    vflip_img=np.zeros(image.shape)
    for i in range(h):
        for j in range(w):
            vflip_img[i,j]=image[h-i-1,j]
    return vflip_img

# cv2.imwrite('Horizontal_Red_Bozu.png',horizontal_flip(image))
# cv2.imwrite('Vertical_Red_Bozu.png',vertical_flip(image))


def clip(broken_image):
    h,w = broken_image.shape[:2]
    for i in range(h):
        for j in range(w):
            (B,G,R)=broken_image[i,j]
            broken_image[i,j,0] = 0 if B<0 else 255 if B>255 else B
            broken_image[i,j,1] = 0 if G<0 else 255 if G>255 else G
            broken_image[i,j,2] = 0 if R<0 else 255 if R>255 else R
    return broken_image

def contrast(image, alpha):
    h,w = image.shape[:2]
    contrast_img=np.zeros(image.shape)
    for i in range(h):
        for j in range(w):
            (B,G,R)=image[i,j]
            contrast_img[i,j,0] = B * alpha
            contrast_img[i,j,1] = G * alpha
            contrast_img[i,j,2] = R * alpha
            (B,G,R)=contrast_img[i,j]
            contrast_img[i,j,0] = 0 if B<0 else 255 if B>255 else B
            contrast_img[i,j,1] = 0 if G<0 else 255 if G>255 else G
            contrast_img[i,j,2] = 0 if R<0 else 255 if R>255 else R
            # contrast_img[i,j,0] = 0 if B<0 else 1 if B>1 else B
            # contrast_img[i,j,1] = 0 if G<0 else 1 if G>1 else G
            # contrast_img[i,j,2] = 0 if R<0 else 1 if R>1 else R
    cv2.imwrite('Contrast_Bozu.jpg',contrast_img)
    return contrast_img

#contrast(image,1.5)

def add_brightness(image, beta):
    h,w = image.shape[:2]
    bright_img=np.zeros(image.shape)
    for i in range(h):
        for j in range(w):
            #image[i,j]+=beta
            (B,G,R)=image[i,j]
            bright_img[i,j,0] = B + beta
            bright_img[i,j,1] = G + beta
            bright_img[i,j,2] = R + beta
            (B,G,R)=bright_img[i,j]
            bright_img[i,j,0] = 0 if B<0 else 255 if B>255 else B
            bright_img[i,j,1] = 0 if G<0 else 255 if G>255 else G
            bright_img[i,j,2] = 0 if R<0 else 255 if R>255 else R
    cv2.imwrite('Bright_Bozu.jpg',bright_img)
    return bright_img

#add_brightness(image,100)


def apply_threshold(image, threshold):
    threshold_img=np.zeros(image.shape)
    h,w=image.shape[:2]
    for i in range(h):
        for j in range(w):
            (B,G,R)=image[i,j]
            threshold_img[i,j,0] = 0 if B<threshold else 255 
            threshold_img[i,j,1] = 0 if G<threshold else 255 
            threshold_img[i,j,2] = 0 if R<threshold else 255
    cv2.imwrite('Bozu_in_the_dark.jpg',threshold_img)
    return threshold_img

#to get just the white eyes
apply_threshold(image,255)
