import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("bat-man.jpg")

rows, cols = img.shape[:2]

M = np.float32([[1, 0, 200],
                [0, 1, 150]])  # Translation matrix

translated_img = cv2.warpAffine(img, M, (cols, rows))

# plt.figure(figsize=(10, 5))
plt.imshow(cv2.cvtColor(translated_img, cv2.COLOR_BGR2RGB))
plt.title("Translated Image")
plt.show()