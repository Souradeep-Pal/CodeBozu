import cv2

#reading image
img=cv2.imread('Bozu.png')

h,w=img.shape[:2]
print('height={}, width={}'.format (h,w))

#extracting RGB values
#it is in BGR not RGB
(B,G,R)=img[500,500]
print('R={},G={},B={}'.format(R,G,B))
B=img[400,400,0]
#0 for B, 1 for G, 2 for R

#extracting region of interest
#slicing
roi=img[100:500,400:800]

#resising
res=cv2.resize(img,(800,800))
#however, aspect ratio is not kept, therefore:
ratio=400/w
t=(400,int(h*ratio))
res_aspect=cv2.resize(img,t)

cv2.imshow('Bozu',res_aspect)
cv2.waitKey(0)
cv2.destroyAllWindows()
        