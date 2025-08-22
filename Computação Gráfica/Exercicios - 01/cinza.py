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
    imagemFinal = img
    return imagemFinal

def mostrarImagem(img, mensagem):
    cv2.imshow(mensagem, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img1 = cv2.imread('Imagens/lena.png')
cinza = nivelDeCinza(img1)
negative = negativo(img1)
normalizada = normalizacao(img1, 0, 100)
mostrarImagem(cinza, "Imagem Normal")
mostrarImagem(img1, "Realce de Cor 100%")
mostrarImagem(negative, "Imagem Cinza")
mostrarImagem(normalizada, "Imagem Cinza Sem Tratamento")
#cv2.imwrite("Imagens/lena_cinza.png",output)