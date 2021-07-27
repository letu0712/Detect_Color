import cv2
import numpy as np

video = cv2.VideoCapture("tracking.mp4")
#fps = video.get(cv2.CAP_PROP_FPS)
#delay = 1000 / fps


def change_hue_min(x):
    change_hue_min.value = x


change_hue_min.value = 98


def change_saturation_min(x):
    change_saturation_min.value = x


change_saturation_min.value = 159


def change_value_min(x):
    change_value_min.value = x


change_value_min.value = 23


def change_hue_max(x):
    change_hue_max.value = x


change_hue_max.value = 150


def change_saturation_max(x):
    change_saturation_max.value = x


change_saturation_max.value = 255


def change_value_max(x):
    change_value_max.value = x


change_value_max.value = 86

cv2.namedWindow("Tracking")
cv2.createTrackbar("Hue Min", "Tracking", 0, 255, change_hue_min)
cv2.createTrackbar("Saturation Min", "Tracking", 0, 255, change_saturation_min)
cv2.createTrackbar("Value Min", "Tracking", 0, 255, change_value_min)

cv2.createTrackbar("Hue Max", "Tracking", 255, 255, change_hue_max)
cv2.createTrackbar("Saturation Max", "Tracking", 255, 255, change_saturation_max)
cv2.createTrackbar("Value Max", "Tracking", 255, 255, change_value_max)
play = True

#Tạo biến để lưu quỹ đạo
arr_point = np.array((),np.int32)
while True:
    if play:
        ret, img = video.read()
    else:
        ret = False
    img_clone = img.copy()
#    cv2.imshow("Video", img)
    img_hsv = cv2.cvtColor(img_clone, cv2.COLOR_BGR2HSV)
#    cv2.imshow("Video HSV", img_hsv)

    # Tạo khoảng giá trị giới hạn màu của đối tượng
    lower = np.array([change_hue_min.value, change_saturation_min.value, change_value_min.value])
    upper = np.array([change_hue_max.value, change_saturation_max.value, change_value_max.value])

    # Tạo mặt nạ nhị phân: Những giá trị thuộc khoảng thì sẽ nhận bit 1 (màu trắng), còn lại là đen
    mask = cv2.inRange(img_hsv, lower, upper)

    # Tạo ma trận bộ lọc nhiễu là ma trận 3x3 với phần từ là 1
    kernel_matrix = np.ones((3, 3))
    # Tiến hành lọc nhiễu (tích chập bộ lọc với từng pixel của ảnh)
    mask = cv2.erode(mask, kernel_matrix)
    # Mở rộng vùng của đối tượng
    mask = cv2.dilate(mask, kernel_matrix)
#    cv2.imshow("Mask", mask)

    # Hàm findContours chỉ áp dụng với ảnh nhị phân
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#    print(len(contours))


    # Viết text lên đối tượng

    if len(contours) >0 :
        tmp_c = contours[0]
        (cx,cy), cr = cv2.minEnclosingCircle(tmp_c)
        result1 = cv2.circle(img_clone,(int(cx),int(cy)),int(cr),(0,0,255),2)

     #   cv2.putText(img,"Green",(int(cx),int(cy)),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
        arr_point = np.append(arr_point, (int(cx), int(cy)))
        print(arr_point)
        arr_point = arr_point.reshape((-1,1,2))
        cv2.polylines(result1,[arr_point],False,(0,0,255),5)

    else:
        result1 = img_clone

    cv2.imshow("Result1", result1)




#    merge_mask = cv2.merge((mask, mask, mask))

 #   result = cv2.bitwise_and(img, merge_mask)

#    cv2.imshow("Result", result)

    if cv2.waitKey(1) == ord('q'):
        break
    if cv2.waitKey(1) == ord(' '):
        play = not play

cv2.destroyAllWindows()

