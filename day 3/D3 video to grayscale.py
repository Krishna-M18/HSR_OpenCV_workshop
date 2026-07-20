import cv2

cap = cv2.VideoCapture('../car_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Video", gray)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()