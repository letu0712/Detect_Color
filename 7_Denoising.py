import cv2
import numpy as np

cap = cv2.VideoCapture("tracking.mp4")
#Hàm lấy giá trị số khung hình trên 1 giây (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)
#Tính thời gian hiển thị 1 khung hình (ms/hình)
delay_time = 1000/fps
print(fps)



def min_red(value):
    min_red.value = value
min_red.value = 0
def min_green(value):
    min_green.value = value
min_green.value = 15
def min_blue(value):
    min_blue.value = value
min_blue.value = 0
def max_red(value):
    max_red.value = value
max_red.value = 115
def max_green(value):
    max_green.value = value
max_green.value = 255
def max_blue(value):
    max_blue.value = value
max_blue.value = 35



cv2.namedWindow("Tracking")
cv2.createTrackbar("Min_RED","Tracking",0,255,min_red)
cv2.createTrackbar("Min_GREEN","Tracking",0,255,min_green)
cv2.createTrackbar("Min_BLUE","Tracking",0,255,min_blue)

cv2.createTrackbar("Max_RED","Tracking",255,255,max_red)
cv2.createTrackbar("Max_GREEN","Tracking",255,255,max_green)
cv2.createTrackbar("Max_BLUE","Tracking",255,255,max_blue)

play = True
while True:
    if play:
        ret, img = cap.read()
    if ret == False:
        break

    cv2.imshow("Video", img)

    #Tạo khoảng giá trị màu được chọn
    min_color = np.array([min_blue.value,min_green.value,min_red.value])
    max_color = np.array([max_blue.value,max_green.value,max_red.value])

    #Những pixel có giá trị màu thuộc khoảng sẽ gán = 1 (màu trắng), còn lại bằng 0 (màu đen)
    mask = cv2.inRange(img,min_color,max_color)

    #Khử nhiễu (Trong bài bộ lọc 1_Filter)
    kernel_matrix = np.ones((3,3))
    mask = cv2.erode(mask, kernel_matrix)

    #Tăng vùng đối tượng được chọn
    mask = cv2.dilate(mask, kernel_matrix)

    #Lấy hình ảnh đơn kênh ghép thành 3 kênh
    mask_main = cv2.merge((mask,mask,mask))

    #Dùng toán tử logic bit AND để giữ nguyên màu
    result = cv2.bitwise_and(img,mask_main)


    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)

    if cv2.waitKey(int(delay_time)) == ord(' '):
        play = not play
    if cv2.waitKey(int(delay_time)) == ord('q'):
        break
cv2.destroyAllWindows()