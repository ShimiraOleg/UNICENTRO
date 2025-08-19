import cv2

img1 = cv2.imread('Imagens/lena.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Imagens/img_aluno.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('Imagens/lena_cinza.png', img1)
cv2.imwrite('Imagens/img_aluno_cinza.png', img2)
