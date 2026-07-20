import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    resized_frame = cv2.resize(frame, (640, 480))

    cv2.rectangle(
        resized_frame,  # image
        (100, 100),  # top-left corner
        (300, 400),  # bottom-right corner
        (255, 0, 0),  # color (BGR)
        15  # thickness
    )

    # Show output
    cv2.imshow("Video Manipulation", resized_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
