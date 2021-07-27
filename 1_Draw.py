import numpy as np
import cv2

#Tạo một bức ảnh đen với toàn giá trị 0
img = np.zeros((600,800,3))
img1 = np.zeros((500,500,3))
img2 = np.zeros((500,500,3))

#Kênh 0,1,2 là màu xanh lam, lục, đỏ
img[100:200,100:300,0]=255
img[300:400,400:600,(1,2)]=255



#Vẽ đường thẳng
#Hàn cv2.line gồm các tham số: tên ảnh, điểm đầu, ddiemr cuối, màu, độ rộng đường
img1[:,:,(0,1,2)]=255

for i in range(0,501,50):
    cv2.line(img1,(0,i),(500,i),(0,255,0),5)
    cv2.putText(img1,str(i),(10,i),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
for i in range(0,501,50):
    cv2.line(img1,(i,0),(i,500),(0,255,0),5)


#Vẽ đường tròn
#Hàm cv2.circle gồm các tham số: tên ảnh, tọa độ tâm, bán kính, màu, độ rộng đường
cv2.circle(img1,(250,250),50,(255,0,0),5)

#Vẽ hình chữ nhật
#Hàm cv2.rectangle gồm các tham số: tên ảnh, tọa độ 2 điểm, màu, độ rộng
cv2.rectangle(img1,(100,100),(400,400),(0,0,255),5)

#Vẽ hình elipse
#Hàm cv2.ellipse gồm: tên ảnh, tâm, độ dài 1 nửa trục đứng, trục ngang, góc nghiêng, góc quét từ bao nhiêu đến bao nhiêu
#Màu, Độ rộng
cv2.ellipse(img1,(250,250),(100,250),90,0,360,(0,0,255),5)


#Vẽ đa giác

#Tham số pts tạo ra bởi mảng gồm tọa độ các điểm, kiểu np.int32
pts = np.array(((50,100),(200,300),(80,90)),np.int32)
#Chuyển đổi về 3 chiều
pts = [pts.reshape(-1,1,2)]

#Hàm cv2.pylines gồm các tham số: tên biến ảnh, tham số pts, hình có kín không,màu, độ rộng đường
cv2.polylines(img2,pts,True,(255,255,255),5)

cv2.imshow("IMAGE",img)
cv2.imshow("IMAGE1",img1)
cv2.imshow("IMAGE2",img2)
cv2.waitKey(0)