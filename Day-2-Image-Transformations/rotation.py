import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("bat-man.jpg")

rows, cols = img.shape[:2]

center = (cols//2, rows//2)

M = cv2.getRotationMatrix2D(center, 45, 1)  # Rotate the image by 45 degrees

rotated_img = cv2.warpAffine(img, M, (cols, rows))

plt.imshow(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB))
plt.title("Rotated Image")
plt.show()