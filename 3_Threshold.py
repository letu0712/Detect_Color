import cv2


def change_value(value):
    change_value.value=value
change_value.value = 0

cv2.namedWindow("IMAGE")
cv2.createTrackbar("Value","IMAGE",0,255,change_value)

while True:
    img = cv2.imread('3_Threshold.png')
    #Nếu nhỏ hơn giá trị ngưỡng value thì cho giá trị bằng 0
    ret, img = cv2.threshold(img,change_value.value,255,cv2.cv2.THRESH_TOZERO)
    print(ret)
    cv2.imshow("IMAGE",img)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()