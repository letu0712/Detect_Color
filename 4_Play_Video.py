import cv2

cap = cv2.VideoCapture("Cat.mp4")

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
        cv2.imshow("Video",img)


    if cv2.waitKey(int(delay_time)) == ord('q'):
        break
    if cv2.waitKey(int(delay_time)) == ord(' '):
        play = not play
        cv2.imshow("Frame Pause", img)
cv2.destroyAllWindows()