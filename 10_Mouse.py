import cv2

def mouse_event(event, x, y, flag, img):
    if mouse_event == cv2.EVENT_LBUTTONDOWN:
        mouse_event.x0 = x
        mouse_event.y0 = y
        mouse_event.draw = True

    if mouse_event == cv2.EVENT_LBUTTONUP:
        mouse_event.x1 = x
        mouse_event.y1 = y
        mouse_event.draw = False
        mouse_event.img = img[mouse_event.y0:mouse_event.y1,mouse_event.x0:mouse_event.y1 ]

    if mouse_event == cv2.EVENT_MOUSEMOVE:
        mouse_event.x = x
        mouse_event.y = y

mouse_event.img = None
mouse_event.x0 = 0
mouse_event.y0 = 0
mouse_event.x1 = 0
mouse_event.y1 = 0
mouse_event.x = 0
mouse_event.y = 0
mouse_event.draw = False


cap = cv2.VideoCapture("tracking.mp4")
#Hàm lấy giá trị số khung hình trên 1 giây (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)

#Tính thời gian hiển thị 1 khung hình (ms/hình)
delay_time = 1000/fps

print(fps)
print(delay_time)
play = True
while True:
    if play:
        ret, img = cap.read()



    if mouse_event.draw:
        img = cv2.rectangle(img,(mouse_event.x0,mouse_event.y0),(mouse_event.x,mouse_event.y),(0,0,255),5)
    if mouse_event.img is not None:
        cv2.imshow("abc", mouse_event.img )

    cv2.imshow("Video",img)


    cv2.setMouseCallback("Video",mouse_event, img)

    if cv2.waitKey(int(delay_time)) == ord('q'):
        break
    if cv2.waitKey(int(delay_time)) == ord(' '):
        play = not play
        cv2.imshow("Frame Pause", img)
cv2.destroyAllWindows()