import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    flipped = cv2.flip(frame, -1)   #default horizontal

    cv2.imshow("Video Manipulation", flipped)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()