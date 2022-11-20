import cv2
import numpy as np

#image=cv2.imread('Bozu.png')

def Blur(image, ksize):
    blurred_img = cv2.GaussianBlur(image, (ksize,ksize),0) 
    cv2.imwrite('real_Blurred_Bozu.jpg', blurred_img)
    return blurred_img

#Blur(image,25)

def Vintage(image):
    h,w = image.shape[:2]
    k_y = cv2.getGaussianKernel(w,200)
    k_x = cv2.getGaussianKernel(h,200) 
    kernel = k_y * k_x.T  
    filter = 255 * kernel / np.linalg.norm(kernel)
    vintage_img = np.zeros(image.shape)
    for i in range(h):
        for j in range(w):
            vintage_img[i,j,0] = image[i,j,0] * filter[j][i]
            vintage_img[i,j,1] = image[i,j,1] * filter[j][i]
            vintage_img[i,j,2] = image[i,j,2] * filter[j][i]       
    cv2.imwrite('Vintage_Bozu.jpg',vintage_img)
    return vintage_img

#Vintage(image)

def Sepia(image):
    sepia_img=np.zeros(image.shape)
    h,w = image.shape[:2]
    for i in range(h):
        for j in range(w):
            B,G,R=image[i,j]
            sepia_img[i,j,0] = R*0.272 + G*0.534 + B*0.131
            sepia_img[i,j,1] = R*0.349 + G*0.686 + B*0.168
            sepia_img[i,j,2] = R*0.393 + G*0.769 + B*0.189
            (B,G,R)=sepia_img[i,j]
            sepia_img[i,j,0] = 0 if B<0 else 255 if B>255 else B
            sepia_img[i,j,1] = 0 if G<0 else 255 if G>255 else G
            sepia_img[i,j,2] = 0 if R<0 else 255 if R>255 else R
    cv2.imwrite('Sepia_Bozu.jpg',sepia_img)
    return sepia_img

#Sepia(image)

def Sharpen(image):
    kernel=np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    sharp_img = cv2.filter2D(image, -1, kernel)
    cv2.imwrite('Sharp_Bozu.jpg',sharp_img)
    return sharp_img

#Sharpen(Sepia(image))
