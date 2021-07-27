import numpy as np
import cv2

#Khởi tạo giá trị ban đầu cho 3 biến
red = 0
blue = 0
green = 0

#Viết hàm thay đổi giá trị màu
def value_red(value):
    global red
    red = value
def value_green(value):
    global green
    green = value
def value_blue(value):
    global blue
    blue = value

#Tạo một cửa sổ
cv2.namedWindow("Image")

#Tạo thanh trượt để thay đổi giá trị màu từ 0 đến 255
#Hàm gồm các tham số: tên thanh trượt, thuộc cửa sổ nào, giá trị chạy, hàm thay đổi
cv2.createTrackbar("RED: ","Image",0,255,value_red)
cv2.createTrackbar("GREEN: ","Image",0,255,value_green)
cv2.createTrackbar("BLUE: ","Image",0,255,value_blue)

#Việc thực hiện chương tình được chạy liên tục
while True:
    #Tạo một cửa sổ kích thước 500x500 màu đen
    img = np.zeros((500, 500, 3), np.uint8)

    #Giá trị màu sẽ phụ thuộc vào hàm ở trên
    img[:, :, 2] = red
    img[:, :, 1] = green
    img[:, :, 0] = blue
    cv2.imshow("Image",img)

    #THoát màn hình
    if cv2.waitKey(10) == ord('q'):
        break



