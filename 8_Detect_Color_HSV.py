import cv2
import numpy as np

video = cv2.VideoCapture("tracking.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
delay = 1000/fps

def change_hue_min(x):
    change_hue_min.value = x
change_hue_min.value = 41

def change_saturation_min(x):
    change_saturation_min.value = x
change_saturation_min.value = 36

def change_value_min(x):
    change_value_min.value = x
change_value_min.value = 0

def change_hue_max(x):
    change_hue_max.value = x
change_hue_max.value = 64

def change_saturation_max(x):
    change_saturation_max.value = x
change_saturation_max.value = 255

def change_value_max(x):
    change_value_max.value = x
change_value_max.value = 255

cv2.namedWindow("Tracking")
cv2.createTrackbar("Hue Min","Tracking",0,255,change_hue_min)
cv2.createTrackbar("Saturation Min","Tracking",0,255,change_saturation_min)
cv2.createTrackbar("Value Min","Tracking",0,255,change_value_min)

cv2.createTrackbar("Hue Max","Tracking",255,255,change_hue_max)
cv2.createTrackbar("Saturation Max","Tracking",255,255,change_saturation_max)
cv2.createTrackbar("Value Max","Tracking",255,255,change_value_max)
play = True
while True:
    if play:
        ret, img = video.read()


    else:
        ret = False


    cv2.imshow("Video", img)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("Video HSV", img_hsv)

    lower = np.array([change_hue_min.value, change_saturation_min.value, change_value_min.value])
    upper = np.array([change_hue_max.value, change_saturation_max.value, change_value_max.value])

    mask = cv2.inRange(img_hsv,lower,upper)

    kernel_matrix = np.ones((3,3))
    mask = cv2.erode(mask, kernel_matrix)
    mask = cv2.dilate(mask, kernel_matrix)


    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))



    result1 = cv2.drawContours(img,contours,-1,(255,0,0),2)
    for contour in contours:
        moment = cv2.moments(contour)
        x = int(moment['m10']/moment['m00'])
        y = int(moment['m01']/moment['m00'])

        cv2.putText(result1,"Green",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))

    cv2.imshow("Result1",result1)




    merge_mask = cv2.merge((mask, mask, mask))

    result = cv2.bitwise_and(img,merge_mask)
    cv2.imshow("Mask",mask)

    cv2.imshow("Result", result)








    if cv2.waitKey(int(delay)) == ord('q'):
        break
    if cv2.waitKey(int(delay)) == ord(' '):
        play = not play

cv2.destroyAllWindows()
