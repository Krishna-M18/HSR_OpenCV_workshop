from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np

model1 = YOLO ("yolo26n.pt")  # 2026 released Model

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    resized_frame = cv2.resize(frame, (1080, 600))

    results = model1(resized_frame)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Live Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

