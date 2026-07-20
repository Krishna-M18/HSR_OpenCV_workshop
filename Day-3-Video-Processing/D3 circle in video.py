import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    resized_frame = cv2.resize(frame, (640, 480))

    cv2.circle(
        resized_frame,  # image
        (350, 300),  # center point
        150,  # radius
        (255, 0, 255),  # color (BGR)
        3  # thickness
    )

    # Show output
    cv2.imshow("Video Manipulation", resized_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
