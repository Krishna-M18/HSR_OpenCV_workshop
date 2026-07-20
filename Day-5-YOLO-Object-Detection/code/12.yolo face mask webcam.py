from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np

from ultralytics import YOLO

model_mask = YOLO("weights.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model_mask(frame, verbose=False)
    annotated = results[0].plot()

    cv2.imshow("Industry Face Detection (YOLO)", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
