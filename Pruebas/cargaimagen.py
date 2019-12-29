import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("C:\\Users\\carlo\\OneDrive\\Documentos\\Mama_Pato\\Pruebas\\pato.jpg",0)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()