from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np

from ultralytics import YOLO

model_mask = YOLO("weights.pt")

image_path = "mask.jpg"   # replace with your image
results = model_mask(image_path)

annotated = results[0].plot()

plt.figure(figsize=(10,8))
plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
