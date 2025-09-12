import cv2
import matplotlib.pyplot as plt
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

def fatiamento_bits(img):
    img_gray = nivelDeCinza(img)
    planos = []
    for i in range(8):
        plano = np.bitwise_and(img_gray, 1 << i)
        plano = np.where(plano > 0, 255, 0).astype(np.uint8)
        planos.append(plano)
    return planos

def histograma(img):
    h, w = img.shape
    hist = np.zeros(256, dtype=np.int32)
    for y in range(h):
        for x in range(w):
            hist[img[y, x]] += 1
    return hist

def histograma_normalizado(img):
    hist = histograma(img)
    return hist / hist.sum()

def histograma_acumulado(img):
    hist = histograma(img)
    return np.cumsum(hist)

def histograma_acumulado_normalizado(img):
    h_acc = histograma_acumulado(img)
    return h_acc / h_acc[-1]

def salvar_histograma(hist, titulo, nome_arquivo):
    plt.figure()
    plt.title(titulo)
    plt.bar(range(256), hist, width=1, color='black')
    plt.savefig(nome_arquivo)
    plt.close()

def mostrarImagem(img, mensagem):
    cv2.imshow(mensagem, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def equalizacao_histograma(img):
    img_gray = nivelDeCinza(img) if len(img.shape) == 3 else img
    hist = histograma(img_gray)
    cdf = np.cumsum(hist)
    cdf_normalizado = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    cdf_normalizado = cdf_normalizado.astype(np.uint8)
    img_eq = cdf_normalizado[img_gray]
    return img_eq    

img1 = cv2.imread('Imagens/lena.png')
img2 = cv2.imread('Imagens/img_aluno.png')
img3 = cv2.imread('Imagens/unequalized.jpg')
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
planos_lena = fatiamento_bits(img1)
planos_aluno = fatiamento_bits(img2)
unequalized_gray = nivelDeCinza(img3)
hist_u = histograma(unequalized_gray)
eq_lena = equalizacao_histograma(img1)
eq_aluno = equalizacao_histograma(img2)
eq_unequalized = equalizacao_histograma(img3)

salvar_histograma(hist_u, "Histograma unequalized cinza", "Imagens/hist_unequalized.png")

for i, cor in enumerate(["Blue", "Green", "Red"]):
    hist_c = histograma(img2[:,:,i])
    salvar_histograma(hist_c, f"Histograma canal {cor} - img_aluno", f"Imagens/hist_img_aluno_{cor}.png")
        
salvar_histograma(histograma(cinza2), "Histograma (A)", "Imagens/hist_img_aluno_A.png")
salvar_histograma(histograma_normalizado(cinza2), "Histograma Normalizado (B)", "Imagens/hist_img_aluno_B.png")
salvar_histograma(histograma_acumulado(cinza2), "Histograma Acumulado (C)", "Imagens/hist_img_aluno_C.png")
salvar_histograma(histograma_acumulado_normalizado(cinza2), "Histograma Acumulado Normalizado (D)", "Imagens/hist_img_aluno_D.png")

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

for i, p in enumerate(planos_lena):
    cv2.imwrite(f"Imagens/lena_bit_{i}.png", p)

for i, p in enumerate(planos_aluno):
    cv2.imwrite(f"Imagens/img_aluno_bit_{i}.png", p)

cv2.imwrite("Imagens/lena_equalizada.png", eq_lena)
cv2.imwrite("Imagens/unequalized_equalizada.png", eq_unequalized)
cv2.imwrite("Imagens/img_aluno_equalizada.png", eq_aluno)