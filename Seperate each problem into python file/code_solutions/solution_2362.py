def box_blur(image):
    # Your code here
    pass

"""

import cv2
import numpy as np

# Read image
img = cv2.imread('../Photos/cat.jpg')
cv2.imshow('Cat', img)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Blur the image
bl