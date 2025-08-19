import cv2
import numpy as np

img1 = cv2.imread('lena.png')
img2 = cv2.imread('img_aluno.png')
img2.resize(512,512,3)

print('Image 1: {} {}'.format(img1.shape, img1.dtype))
print('Image 2: {} {}'.format(img2.shape, img2.dtype))

img3 = img1*0.8+img2*0.2
img3 = img3.astype(np.uint8)

print('Image 3: {} {}'.format(img3.shape, img3.dtype))

cv2.imshow('Recorte', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
