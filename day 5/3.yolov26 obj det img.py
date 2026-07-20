from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np

model1 = YOLO ("yolo26n.pt")  # 2026 released Model

img = cv2.imread("vk.jpg")
result = model1(img)

annotated_image_ = result[0].plot()
plt.figure(figsize=(10,8))
plt.imshow(cv2.cvtColor(annotated_image_, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
