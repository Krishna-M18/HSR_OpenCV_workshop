from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np

model2 = YOLO ("yolo26n.pt") # just object detection without segementation

image2 = cv2.imread("m_cars.jpg")
results2 = model2(image2)

annotated_image2 = results2[0].plot()
plt.figure(figsize=(10,8))
plt.imshow(cv2.cvtColor(annotated_image2, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

