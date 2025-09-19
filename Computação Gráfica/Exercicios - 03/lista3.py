import cv2
import numpy as np
import matplotlib.pyplot as plt

def nivelDeCinza(img):
    img = img.astype(np.float16)
    c = img[:,:,0]/3 + img[:,:,1]/3 + img[:,:,2]/3
    c = c.astype(np.uint8)
    return c

def salvar_imagem(img, nome):
    cv2.imwrite(f"Imagens_Resultado/{nome}", img)

def salvar_espectro(fft, nome):
    mag = np.log(1 + np.abs(fft))
    mag = (mag / np.max(mag) * 255).astype(np.uint8)
    salvar_imagem(mag, nome)

def espectro_fourier(img, nome_saida):
    img_gray = nivelDeCinza(img)
    f = np.fft.fft2(img_gray)
    fshift = np.fft.fftshift(f)
    salvar_espectro(fshift, nome_saida)
    return fshift

def filtro_gaussiano(shape, sigma, tipo="low"):
    M, N = shape
    U, V = np.meshgrid(np.arange(N), np.arange(M))
    U = U - N//2
    V = V - M//2
    D2 = U**2 + V**2
    if tipo == "low":
        H = np.exp(-D2/(2*(sigma**2)))
    else:  
        H = 1 - np.exp(-D2/(2*(sigma**2)))
    return H

def aplicar_filtro(img, H, nome_saida):
    img_gray = nivelDeCinza(img)
    F = np.fft.fft2(img_gray)
    Fshift = np.fft.fftshift(F)
    G = Fshift * H
    g = np.fft.ifft2(np.fft.ifftshift(G))
    g = np.abs(g)
    g = (g / g.max() * 255).astype(np.uint8)
    salvar_imagem(g, nome_saida)
    return g

def aplicar_filtro_imagem(img, filtro_img, nome_saida):
    img_gray = nivelDeCinza(img)
    F = np.fft.fft2(img_gray)
    Fshift = np.fft.fftshift(F)

    filtro_gray = nivelDeCinza(filtro_img)
    filtro_norm = filtro_gray.astype(np.float32)/255.0

    G = Fshift * filtro_norm
    g = np.fft.ifft2(np.fft.ifftshift(G))
    g = np.abs(g)
    g = (g / g.max() * 255).astype(np.uint8)
    salvar_imagem(g, nome_saida)
    return g

def filtro_passa_banda(shape, d0, w):
    M, N = shape
    U, V = np.meshgrid(np.arange(N), np.arange(M))
    U = U - N//2
    V = V - M//2
    D = np.sqrt(U**2 + V**2)
    H = np.logical_and(D >= d0 - w/2, D <= d0 + w/2).astype(np.float32)
    return H

def filtro_rejeita_banda(shape, d0, w):
    return 1 - filtro_passa_banda(shape, d0, w)

if __name__ == "__main__":
    for nome in ["arara.png","barra1.png","barra2.png","barra3.png","barra4.png","teste.tif","img_aluno.png"]:
        img = cv2.imread(f"Imagens/{nome}")
        espectro_fourier(img, f"fft_{nome}.png")

    for nome in ["teste.tif","img_aluno.png"]:
        img = cv2.imread(f"Imagens/{nome}")
        H_low = filtro_gaussiano(img.shape[:2], sigma=30, tipo="low")
        H_high = filtro_gaussiano(img.shape[:2], sigma=30, tipo="high")
        aplicar_filtro(img, H_low, f"{nome}_low.png")
        aplicar_filtro(img, H_high, f"{nome}_high.png")

    img = cv2.imread("Imagens/arara.png")
    filtro_img = cv2.imread("Imagens/arara_filtro.png")
    aplicar_filtro_imagem(img, filtro_img, "arara_rejeita_banda.png")

    for nome in ["teste.tif","img_aluno.png"]:
        img = cv2.imread(f"Imagens/{nome}")
        H_pb = filtro_passa_banda(img.shape[:2], d0=50, w=20)
        H_rb = filtro_rejeita_banda(img.shape[:2], d0=50, w=20)
        aplicar_filtro(img, H_pb, f"{nome}_passa_banda.png")
        aplicar_filtro(img, H_rb, f"{nome}_rejeita_banda.png")
