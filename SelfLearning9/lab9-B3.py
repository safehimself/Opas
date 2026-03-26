import cv2
import numpy as np
img = cv2.imread("Image1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
edges_3 = edges_3ch = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
result = np.hstack((img, edges_3))
cv2.imwrite("result.jpg", result)
