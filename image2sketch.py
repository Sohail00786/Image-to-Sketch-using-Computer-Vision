### Image To Sketch ###

import cv2

image = cv2.imread("sohail.jpg")

grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(grey)

blur = cv2.GaussianBlur(invert,(21,21), 0)

inverted_blur = cv2.bitwise_not(blur)

sketch = cv2.divide(grey,inverted_blur,scale = 256.0)

cv2.imshow("Orginal image",sketch)

cv2.imwrite("sketch.jpg",sketch)

cv2.waitKey(0)