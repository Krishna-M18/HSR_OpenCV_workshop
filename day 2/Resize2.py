import cv2
import matplotlib.pyplot as plt

img = cv2.imread("bat-man.jpg")
resized_img = cv2.resize(img, (400, 300))  # Resize the image to 400x300 pixels
scaled_img = cv2.resize(img, None, fx=0.5, fy=0.2)

img_rgb =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
resized_rgb = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
scaled_rgb = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2RGB)


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure(figsize=(10,5))
plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(resized_rgb)
plt.title("Fixed Resized")

plt.subplot(1,3,3)
plt.imshow(scaled_rgb)
plt.title("Scaled")

plt.show()