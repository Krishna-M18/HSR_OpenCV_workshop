from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np


model2 = YOLO ("yolo26n-seg.pt")
image3 = cv2.imread("vk.jpg")
results3 = model2(image3)

annotated_image3 = results3[0].plot()
plt.figure(figsize=(10,8))
plt.imshow(cv2.cvtColor(annotated_image3, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
