import cv2
import numpy as np

image1 = cv2.imread("../data/banana/1.jpg")
image2 = cv2.imread("../data/banana/2.jpg")
image3 = cv2.imread("../data/banana/3.jpg")

difference = cv2.subtract(image1, image2)

result = not np.any(difference)

if result is True:
    print("The images are the same")
else:
    cv2.imwrite("result.jpg", difference)
    print("The images are the different")
