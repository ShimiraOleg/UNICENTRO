import cv2
import numpy as np
import os
from collections import deque

def salvar_imagem(img, nome, pasta="Imagens_Resultado"):
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    cv2.imwrite(os.path.join(pasta, nome), img)

def nivelDeCinza(img):
    img = img.astype(np.float16)
    c = img[:,:,0]/3 + img[:,:,1]/3 + img[:,:,2]/3
    c = c.astype(np.uint8)
    return c

def aplicar_mediana(img, vezes=3, ksize=3):
    resultado = []
    atual = img.copy()
    for _ in range(vezes):
        atual = cv2.medianBlur(atual, ksize)
        resultado.append(atual.copy())
    return resultado

def detectar_pontos_isolados(img, thresh=200):
    gray = nivelDeCinza(img)
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]], dtype=np.float32)
    filtrada = cv2.filter2D(gray, ddepth=-1, kernel=kernel)
    _, limiarizada = cv2.threshold(filtrada, thresh, 255, cv2.THRESH_BINARY)
    return filtrada, limiarizada

def detectar_linhas(img, thresh=150):
    gray = nivelDeCinza(img)

    kernel_horizontal = np.array([[-1, -1, -1],
                                  [ 2,  2,  2],
                                  [-1, -1, -1]], dtype=np.float32)
    kernel_45 = np.array([[-1, -1,  2],
                          [-1,  2, -1],
                          [ 2, -1, -1]], dtype=np.float32)
    kernel_vertical = np.array([[-1,  2, -1],
                                [-1,  2, -1],
                                [-1,  2, -1]], dtype=np.float32)
    kernel_neg45 = np.array([[ 2, -1, -1],
                             [-1,  2, -1],
                             [-1, -1,  2]], dtype=np.float32)

    h = cv2.filter2D(gray, ddepth=-1, kernel=kernel_horizontal)
    d45 = cv2.filter2D(gray, ddepth=-1, kernel=kernel_45)
    v = cv2.filter2D(gray, ddepth=-1, kernel=kernel_vertical)
    dneg45 = cv2.filter2D(gray, ddepth=-1, kernel=kernel_neg45)

    _, h_bin = cv2.threshold(h, thresh, 255, cv2.THRESH_BINARY)
    _, d45_bin = cv2.threshold(d45, thresh, 255, cv2.THRESH_BINARY)
    _, v_bin = cv2.threshold(v, thresh, 255, cv2.THRESH_BINARY)
    _, dneg45_bin = cv2.threshold(dneg45, thresh, 255, cv2.THRESH_BINARY)

    combinado = cv2.bitwise_or(h_bin, d45_bin)
    combinado = cv2.bitwise_or(combinado, v_bin)
    combinado = cv2.bitwise_or(combinado, dneg45_bin)

    return {"horizontal": h_bin, "45": d45_bin, "vertical": v_bin, "neg45": dneg45_bin}, combinado

def aplicar_canny(img, t1=100, t2=200):
    gray = nivelDeCinza(img)
    edges = cv2.Canny(gray, t1, t2)
    return edges

def region_growing(image, seed, thresh=15):
    h, w = image.shape
    mask = np.zeros((h, w), np.uint8)
    seed_value = int(image[seed[1], seed[0]])

    queue = deque([seed])
    mask[seed[1], seed[0]] = 255

    neighbors = [(-1,-1), (-1,0), (-1,1),
                 ( 0,-1),         ( 0,1),
                 ( 1,-1), ( 1,0), ( 1,1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and mask[ny, nx] == 0:
                if abs(int(image[ny, nx]) - seed_value) <= thresh:
                    mask[ny, nx] = 255
                    queue.append((nx, ny))
    return mask

def aplicar_region_growing(img, seed, thresh=15):
    gray = nivelDeCinza(img)
    mask = region_growing(gray, seed, thresh)
    overlay = img.copy()
    overlay[mask == 255] = [255, 0, 0]  # região em azul
    return mask, overlay

def aplicar_otsu(img):
    gray = nivelDeCinza(img)
    _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return otsu

if __name__ == "__main__":
    img = cv2.imread("Imagens/circuito.tif", cv2.IMREAD_GRAYSCALE)
    for i, res in enumerate(aplicar_mediana(img, vezes=3, ksize=3), start=1):
        salvar_imagem(res, f"q1_circuito_mediana_{i}.png")

    img = cv2.imread("Imagens/pontos.png")
    filtrada, limiarizada = detectar_pontos_isolados(img, thresh=200)
    salvar_imagem(filtrada, "q2_pontos_filtrada.png")
    salvar_imagem(limiarizada, "q2_pontos_detectados.png")

    img = cv2.imread("Imagens/linhas.png")
    resultados, combinado = detectar_linhas(img, thresh=150)
    for nome, r in resultados.items():
        salvar_imagem(r, f"q3_linhas_{nome}.png")
    salvar_imagem(combinado, "q3_linhas_combinado.png")

    img = cv2.imread("Imagens/igreja.png")
    edges = aplicar_canny(img, 100, 200)
    salvar_imagem(edges, "q4_igreja_canny.png")

    img = cv2.imread("Imagens/root.jpg")
    mask, overlay = aplicar_region_growing(img, seed=(100,150), thresh=15)
    salvar_imagem(mask, "q5_root_mask.png")
    salvar_imagem(overlay, "q5_root_overlay.png")

    for nome in ["harewood.jpg", "nuts.jpg", "snow.jpg", "img_aluno.png"]:
        img = cv2.imread(f"Imagens/{nome}")
        otsu = aplicar_otsu(img)
        salvar_imagem(otsu, f"q6_otsu_{nome}.png")

