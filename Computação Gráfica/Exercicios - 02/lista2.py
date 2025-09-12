import cv2
import numpy as np

def nivelDeCinza(img):
    img = img.astype(np.float16)
    c = img[:,:,0]/3 + img[:,:,1]/3 + img[:,:,2]/3
    c = c.astype(np.uint8)
    return c

def filtro_media(img, k=3):
    kernel = np.ones((k, k), np.float32) / (k * k)
    return cv2.filter2D(img, -1, kernel)

def filtro_media_k(img, janela=3, k=5):
    h, w = img.shape
    offset = janela // 2
    saida = np.zeros_like(img)

    for y in range(offset, h - offset):
        for x in range(offset, w - offset):
            vizinhos = img[y-offset:y+offset+1, x-offset:x+offset+1].flatten()
            centro = img[y, x]
            indices = np.argsort(np.abs(vizinhos - centro))
            mais_proximos = vizinhos[indices[:k]]
            saida[y, x] = np.mean(mais_proximos)

    return saida.astype(np.uint8)

def filtro_mediana(img, k=3):
    return cv2.medianBlur(img, k)

def filtro_laplaciano(img):
    return cv2.Laplacian(img, cv2.CV_64F).astype(np.uint8)

def filtro_roberts(img):
    kernel_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
    kernel_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)
    gx = cv2.filter2D(img, -1, kernel_x)
    gy = cv2.filter2D(img, -1, kernel_y)
    return cv2.convertScaleAbs(gx + gy)

def filtro_prewitt(img):
    kernel_x = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]], dtype=np.float32)
    kernel_y = np.array([[1, 1, 1],
                         [0, 0, 0],
                         [-1, -1, -1]], dtype=np.float32)
    gx = cv2.filter2D(img, -1, kernel_x)
    gy = cv2.filter2D(img, -1, kernel_y)
    return cv2.convertScaleAbs(gx + gy)

def filtro_sobel(img):
    gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    return cv2.convertScaleAbs(gx + gy)

img1 = cv2.imread('Imagens/lena.png')
img2 = cv2.imread('Imagens/img_aluno.png')
cinza1 = nivelDeCinza(img1)
cinza2 = nivelDeCinza(img2)

cv2.imwrite("Imagens/lena_media.png", filtro_media(cinza1, 5))
cv2.imwrite("Imagens/img_aluno_media.png", filtro_media(cinza2, 5))
cv2.imwrite("Imagens/lena_media_k.png", filtro_media_k(cinza1, janela=5, k=10))
cv2.imwrite("Imagens/img_aluno_media_k.png", filtro_media_k(cinza2, janela=5, k=10))
cv2.imwrite("Imagens/lena_mediana.png", filtro_mediana(cinza1, 5))
cv2.imwrite("Imagens/img_aluno_mediana.png", filtro_mediana(cinza2, 5))
cv2.imwrite("Imagens/lena_laplaciano.png", filtro_laplaciano(cinza1))
cv2.imwrite("Imagens/img_aluno_laplaciano.png", filtro_laplaciano(cinza2))
cv2.imwrite("Imagens/lena_roberts.png", filtro_roberts(cinza1))
cv2.imwrite("Imagens/img_aluno_roberts.png", filtro_roberts(cinza2))
cv2.imwrite("Imagens/lena_prewitt.png", filtro_prewitt(cinza1))
cv2.imwrite("Imagens/img_aluno_prewitt.png", filtro_prewitt(cinza2))
cv2.imwrite("Imagens/lena_sobel.png", filtro_sobel(cinza1))
cv2.imwrite("Imagens/img_aluno_sobel.png", filtro_sobel(cinza2))
