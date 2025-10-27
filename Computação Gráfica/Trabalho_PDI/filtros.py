import numpy as np
import matplotlib.pyplot as plt
import math

def nivelDeCinza(img):
    img = img.astype(np.float16)
    if len(img.shape) == 2:
        return img.astype(np.uint8)
    c = img[:,:,0]/3 + img[:,:,1]/3 + img[:,:,2]/3
    c = c.astype(np.uint8)
    return c

def negativo(img):
    c = 255 - img
    return c

def histograma(img):
    h, w = img.shape
    hist = np.zeros(256, dtype=np.int32)
    for y in range(h):
        for x in range(w):
            hist[img[y, x]] += 1
    return hist

def salvar_histograma(hist, titulo, nome_arquivo):
    plt.figure()
    plt.title(titulo)
    plt.bar(range(256), hist, width=1, color='black')
    plt.savefig(nome_arquivo)
    plt.close()

def otsu(img):
    hist = histograma(img)
    hist_norm = hist / hist.sum()
    
    bins = np.arange(256)
    
    omega = np.cumsum(hist_norm)
    mu = np.cumsum(bins * hist_norm)
    mu_t = mu[-1]
    
    sigma_b_squared = np.zeros(256)
    
    for t in range(256):
        if omega[t] == 0 or omega[t] == 1:
            continue
        
        omega_0 = omega[t]
        omega_1 = 1 - omega_0
        mu_0 = mu[t] / omega_0 if omega_0 > 0 else 0
        mu_1 = (mu_t - mu[t]) / omega_1 if omega_1 > 0 else 0
        
        sigma_b_squared[t] = omega_0 * omega_1 * (mu_0 - mu_1) ** 2
    
    limiar = np.argmax(sigma_b_squared)
    
    img_bin = np.where(img >= limiar, 255, 0).astype(np.uint8)
    
    return img_bin, limiar

def filtro_media(img, tamanho=3):
    h, w = img.shape[:2]
    offset = tamanho // 2
    
    if len(img.shape) == 2:
        img_filtrada = np.zeros_like(img, dtype=np.float32)
        
        for y in range(offset, h - offset):
            for x in range(offset, w - offset):
                janela = img[y-offset:y+offset+1, x-offset:x+offset+1]
                img_filtrada[y, x] = np.mean(janela)
    else:
        img_filtrada = np.zeros_like(img, dtype=np.float32)
        
        for c in range(img.shape[2]):
            for y in range(offset, h - offset):
                for x in range(offset, w - offset):
                    janela = img[y-offset:y+offset+1, x-offset:x+offset+1, c]
                    img_filtrada[y, x, c] = np.mean(janela)
    
    return img_filtrada.astype(np.uint8)

def filtro_mediana(img, tamanho=3):
    h, w = img.shape[:2]
    offset = tamanho // 2
    
    if len(img.shape) == 2:
        img_filtrada = np.zeros_like(img)
        
        for y in range(offset, h - offset):
            for x in range(offset, w - offset):
                janela = img[y-offset:y+offset+1, x-offset:x+offset+1]
                img_filtrada[y, x] = np.median(janela)
    else:
        img_filtrada = np.zeros_like(img)
        
        for c in range(img.shape[2]):
            for y in range(offset, h - offset):
                for x in range(offset, w - offset):
                    janela = img[y-offset:y+offset+1, x-offset:x+offset+1, c]
                    img_filtrada[y, x, c] = np.median(janela)
    
    return img_filtrada.astype(np.uint8)

def filtro_gaussiano(image, sigma):

    k = int(6 * sigma + 1)
    if k % 2 == 0:
         k += 1
    ax = np.linspace(-(k // 2), k // 2, k)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    gauss = gauss / np.sum(gauss)
    kernel = np.outer(gauss, gauss)
    rows, cols = image.shape
    padded = np.pad(image, k//2, mode='reflect')
    result = np.zeros_like(image)
    for i in range(rows):
        for j in range(cols):
            region = padded[i:i+k, j:j+k]
            result[i, j] = np.sum(region * kernel)
    return result
    
def gradiente_sobel(img):
    h, w = img.shape
    
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    grad_x = np.zeros_like(img, dtype=np.float32)
    grad_y = np.zeros_like(img, dtype=np.float32)
    
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            janela = img[y-1:y+2, x-1:x+2]
            grad_x[y, x] = np.sum(janela * Gx)
            grad_y[y, x] = np.sum(janela * Gy)
    
    magnitude = np.sqrt(grad_x**2 + grad_y**2)
    direcao = np.arctan2(grad_y, grad_x)
    
    return magnitude, direcao

def supressao_nao_maxima(magnitude, orientation):
    suppressed_magnitude = np.copy(magnitude)
    rows, cols = magnitude.shape
    
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            angle = orientation[i][j]
            q = [0, 0]
            if (-np.pi/8 <= angle < np.pi/8) or (7*np.pi/8 <= angle):
                q[0] = magnitude[i][j+1]
                q[1] = magnitude[i][j-1]
            elif (np.pi/8 <= angle < 3*np.pi/8):
                q[0] = magnitude[i+1][j+1]
                q[1] = magnitude[i-1][j-1]
            elif (3*np.pi/8 <= angle < 5*np.pi/8):
                q[0] = magnitude[i+1][j]
                q[1] = magnitude[i-1][j]
            else:
                q[0] = magnitude[i-1][j+1]
                q[1] = magnitude[i+1][j-1]
            
            if magnitude[i][j] < max(q[0], q[1]):
                suppressed_magnitude[i][j] = 0
    
    return suppressed_magnitude

def limiar_duplo(magnitude, low_threshold, high_threshold):
    rows, cols = magnitude.shape
    edge_map = np.zeros((rows, cols), dtype=np.uint8)
    
    strong_edge_i, strong_edge_j = np.where(magnitude >= high_threshold)
    weak_edge_i, weak_edge_j = np.where((magnitude >= low_threshold) & (magnitude < high_threshold))
    
    edge_map[strong_edge_i, strong_edge_j] = 255

    for i, j in zip(weak_edge_i, weak_edge_j):
        if (edge_map[i-1:i+2, j-1:j+2] == 255).any():
            edge_map[i, j] = 255
    
    return edge_map

def canny(img, limiar_baixo=20, limiar_alto=80, sigma=0.6):
    if len(img.shape) == 3:
        img = nivelDeCinza(img)
    img_suav = filtro_gaussiano(img, sigma)
    magnitude, direcao = gradiente_sobel(img_suav)
    img_suprimida = supressao_nao_maxima(magnitude, direcao)
    img_final = limiar_duplo(img_suprimida, limiar_baixo, limiar_alto)
    
    return img_final

def erosao(img, elemento_estruturante=None):
    if elemento_estruturante is None:
        elemento_estruturante = np.ones((3, 3), dtype=np.uint8)
    
    h, w = img.shape
    eh, ew = elemento_estruturante.shape
    offset_y = eh // 2
    offset_x = ew // 2
    
    img_erodida = np.zeros_like(img)
    
    for y in range(offset_y, h - offset_y):
        for x in range(offset_x, w - offset_x):
            janela = img[y-offset_y:y+offset_y+1, x-offset_x:x+offset_x+1]
            if np.all((janela[elemento_estruturante == 1]) == 255):
                img_erodida[y, x] = 255
    
    return img_erodida

def dilatacao(img, elemento_estruturante=None):
    if elemento_estruturante is None:
        elemento_estruturante = np.ones((3, 3), dtype=np.uint8)
    
    h, w = img.shape
    eh, ew = elemento_estruturante.shape
    offset_y = eh // 2
    offset_x = ew // 2
    
    img_dilatada = np.zeros_like(img)
    
    for y in range(offset_y, h - offset_y):
        for x in range(offset_x, w - offset_x):
            janela = img[y-offset_y:y+offset_y+1, x-offset_x:x+offset_x+1]
            if np.any((janela[elemento_estruturante == 1]) == 255):
                img_dilatada[y, x] = 255
    
    return img_dilatada

def abertura(img, elemento_estruturante=None):
    img_erodida = erosao(img, elemento_estruturante)
    img_aberta = dilatacao(img_erodida, elemento_estruturante)
    return img_aberta

def fechamento(img, elemento_estruturante=None):
    img_dilatada = dilatacao(img, elemento_estruturante)
    img_fechada = erosao(img_dilatada, elemento_estruturante)
    return img_fechada

def calcular_area(img_bin):
    return np.sum(img_bin == 255)

def calcular_perimetro(img_bin):
    h, w = img_bin.shape
    perimetro = 0
    
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if img_bin[y, x] == 255:
                vizinhanca = img_bin[y-1:y+2, x-1:x+2]
                if np.any(vizinhanca == 0):
                    perimetro += 1
    
    return perimetro

def calcular_diametro(img_bin):
    pontos = np.argwhere(img_bin == 255)
    
    if len(pontos) == 0:
        return 0
    
    diametro_max = 0
    n = len(pontos)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = np.sqrt((pontos[i][0] - pontos[j][0])**2 + 
                          (pontos[i][1] - pontos[j][1])**2)
            if dist > diametro_max:
                diametro_max = dist
    
    return diametro_max

def crescimento_regiao(img_bin, y_seed, x_seed, rotulo, img_rotulada):
    h, w = img_bin.shape
    pilha = [(y_seed, x_seed)]
    
    while pilha:
        y, x = pilha.pop()
        
        if y < 0 or y >= h or x < 0 or x >= w:
            continue
        
        if img_bin[y, x] == 0 or img_rotulada[y, x] != 0:
            continue
        
        img_rotulada[y, x] = rotulo
        
        pilha.append((y - 1, x))
        pilha.append((y + 1, x))
        pilha.append((y, x - 1))
        pilha.append((y, x + 1))
        pilha.append((y - 1, x - 1))
        pilha.append((y - 1, x + 1))
        pilha.append((y + 1, x - 1))
        pilha.append((y + 1, x + 1))

def contar_objetos(img_bin):
    h, w = img_bin.shape
    img_rotulada = np.zeros_like(img_bin, dtype=np.int32)
    rotulo = 0
    
    for y in range(h):
        for x in range(w):
            if img_bin[y, x] == 255 and img_rotulada[y, x] == 0:
                rotulo += 1
                crescimento_regiao(img_bin, y, x, rotulo, img_rotulada)
    
    return rotulo, img_rotulada