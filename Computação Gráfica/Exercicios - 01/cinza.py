import cv2
import numpy as np

def nivelDeCinza(img):
    img = img.astype(np.float16)
    c = img[:,:,0]/3 + img[:,:,1]/3 + img[:,:,2]/3
    c = c.astype(np.uint8)
    return c

def negativo(img):
    c = 255 - img
    return c

def normalizacao(img, c, d):
    a = np.min(img)
    b = np.max(img)
    imagemFinal = (img-a)*((d-c)/(b-a))+c
    imagemFinal = imagemFinal.astype(np.uint8)
    return imagemFinal

def operadorLog(img):
    img = img.astype(np.float16)
    c = 255/ np.log(1 + np.max(img))
    imagemLog = c * (np.log(img + 1))
    imagemFinal = imagemLog.astype(np.uint8)
    return imagemFinal

def potencia(img, c, r):
    img = img.astype(np.float32)
    imgPow = c * np.power(img, r)
    final = normalizacao(imgPow,0,255)
    return final

def mostrarImagem(img, mensagem):
    cv2.imshow(mensagem, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img1 = cv2.imread('Imagens/lena.png')
img2 = cv2.imread('Imagens/img_aluno.png')
cinza = nivelDeCinza(img1)
negative = negativo(img1)
normalizada = normalizacao(img1, 0, 100)
logaritmo = operadorLog(img1)
power = potencia(img1, 2, 2)
cinza2 = nivelDeCinza(img2)
negative2 = negativo(img2)
normalizada2 = normalizacao(img2, 0, 100)
logaritmo2 = operadorLog(img2)
power2 = potencia(img2, 2, 2)

mostrarImagem(img1, "Imagem Original")
mostrarImagem(cinza, "Imagem Cinza")
mostrarImagem(negative, "Imagem Negativa")
mostrarImagem(normalizada, "Imagem Normalizada")
mostrarImagem(logaritmo, "Imagem Logaritmo")
mostrarImagem(power, "Imagem Potencia")
cv2.imwrite("Imagens/lena_cinza.png",cinza)
cv2.imwrite("Imagens/lena_negativa.png",negative)
cv2.imwrite("Imagens/lena_normalizada.png",normalizada)
cv2.imwrite("Imagens/lena_log.png",logaritmo)
cv2.imwrite("Imagens/lena_potencia.png",power)
cv2.imwrite("Imagens/img_aluno_cinza.png",cinza2)
cv2.imwrite("Imagens/img_aluno_negativa.png",negative2)
cv2.imwrite("Imagens/img_aluno_normalizada.png",normalizada2)
cv2.imwrite("Imagens/img_aluno_log.png",logaritmo2)
cv2.imwrite("Imagens/img_aluno_potencia.png",power2)