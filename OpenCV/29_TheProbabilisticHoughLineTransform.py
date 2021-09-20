"""Now let's get familiar with The Probabilistic Hough Line Transform."""
import cv2
import numpy as np

img = cv2.imread("Medias/road.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 255, 255, apertureSize=3)

cv2.imshow("Image", img)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100,
                        minLineLength=100, maxLineGap=10)
"""
HoughLinesP(image, rho, theta, threshold[, lines
[, minLineLength[, maxLineGap]]]) -> lines .
@brief Finds line segments in a binary image using the probabilistic
Hough transform. . . The function implements the probabilistic Hough
transform algorithm for line detection, described .

"""

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)

# This image is so big. It's better to resize it.
h, w, _ = img.shape
img = cv2.resize(img, (512, int(512*h/w)))

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""We can see some noises. We learn how to delete them in the next code."""
