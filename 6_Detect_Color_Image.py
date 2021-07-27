import cv2
import numpy as np

def min_red(x):
    min_red.value = x
min_red.value = 0
def min_green(x):
    min_green.value = x
min_green.value = 0
def min_blue(x):
    min_blue.value = x
min_blue.value = 0
def max_red(x):
    max_red.value = x
max_red.value = 255
def max_green(x):
    max_green.value = x
max_green.value = 255
def max_blue(x):
    max_blue.value = x
max_blue.value = 255

cv2.namedWindow("Detect Color")
cv2.createTrackbar("Min_Red", "Detect Color", 0, 255, min_red)
cv2.createTrackbar("Min_Green", "Detect Color",0,255, min_green)
cv2.createTrackbar("Min_Blue", "Detect Color", 0, 255, min_blue)

cv2.createTrackbar("Max_Red", "Detect Color", 255, 255, max_red)
cv2.createTrackbar("Max_Green", "Detect Color", 255, 255, max_green)
cv2.createTrackbar("Max_Blue", "Detect Color", 255, 255, max_blue)


while True:
    img1 = cv2.imread("6_Detect_Color_Image.png")

    cv2.imshow("Detect Color", img1)
    min_color = np.array([min_blue.value, min_green.value, min_red.value])
    max_color = np.array([max_blue.value, max_green.value, max_red.value])

    choose_color = cv2.inRange(img1, min_color, max_color)
    cv2.imshow("choose", choose_color)

    merge_choose_color = cv2.merge((choose_color, choose_color, choose_color))

    result = cv2.bitwise_and(img1, merge_choose_color)
    cv2.imshow("Result",result)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

