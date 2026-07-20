from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np

model3 = YOLO ("yolo26n-pose.pt")

image1 = cv2.imread("yoga.jpg")
results1 = model3(image1)

annotated_image1 = results1[0].plot()
plt.figure(figsize=(10,8))
plt.imshow(cv2.cvtColor(annotated_image1, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

