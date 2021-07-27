import cv2
import numpy as np

img = np.zeros((512,512,3))
cv2.imwrite("Gray_Scale.jpg",img)
img = cv2.imread("Gray_Scale.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

for i in range(0,513,2):
    img[i:i+1,0:512] = i/2

print(img[126,245])
cv2.imshow("IMG",img)
cv2.waitKey(0)