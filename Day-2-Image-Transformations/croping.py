import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("bat-man.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Print image dimensions
print("Image Shape:", img.shape)

# Get height and width
h, w = img.shape[:2]

# Crop 20% from each side
row_start = int(h * 0.2)
row_end = int(h * 0.8)
col_start = int(w * 0.2)
col_end = int(w * 0.8)

cropped = img[row_start:row_end, col_start:col_end]

# Display images
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

# Cropped Image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
plt.title("Cropped Image")
plt.axis("off")

plt.tight_layout()
plt.show()