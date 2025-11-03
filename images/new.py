import cv2

# Load image
img = cv2.imread(r"D:\Python\images\img2.png")

# Rotate 180 degrees
rotated = cv2.rotate(img, cv2.ROTATE_180)

# Show both
cv2.imshow("Original", img)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()


