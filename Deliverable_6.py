import cv2
from matplotlib.pyplot import gray
import numpy as np
from Deliverable_1 import *
from Deliverable_2 import *
from Deliverable_5 import *

def render(image): 
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_img = Blur(gray_img, 3)

    edge_img = cv2.adaptiveThreshold(blur_img, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY, 9, 2)

    (x, y)= image.shape[:2]
    edge_img = cv2.resize(edge_img, (y, x))
    edge_img = cv2.cvtColor(edge_img, cv2.COLOR_GRAY2RGB)
    cv2.imwrite("edge.png", edge_img)
    return cv2.bitwise_and(image, edge_img)
  
image=cv2.imread('MyPic.jpeg')
res = render(image) 
  