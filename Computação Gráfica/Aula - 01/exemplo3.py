import cv2

img = cv2.imread('img_aluno.png')
recorte = img[200:300, 200:300]
img[0:100,0:100] = recorte

cv2.imshow('Recorte', img)
cv2.waitKey(0)
cv2.destroyAllWindows()