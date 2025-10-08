import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

if not os.path.exists('Imagens_Resultado'):
    os.makedirs('Imagens_Resultado')

def salvar_imagem(img, nome):
    cv2.imwrite(os.path.join('Imagens_Resultado', nome), img)

# Exercício 2 - Erosão e Dilatação em quadrados
def exercicio_2():
    img = cv2.imread('Imagens/quadrados.png', cv2.IMREAD_GRAYSCALE)
    
    # Elemento estruturante quadrado de tamanho 45x45 (maior que 40, menor que 60)
    kernel = np.ones((45, 45), np.uint8)
    
    # Erosão para eliminar quadrados de 20 e 40 pixels
    eroded = cv2.erode(img, kernel, iterations=1)
    
    # Dilatação para restaurar os quadrados de 60 e 80 ao tamanho original
    restored = cv2.dilate(eroded, kernel, iterations=1)
    
    salvar_imagem(img, 'e2_original.png')
    salvar_imagem(eroded, 'e2_erosao.png')
    salvar_imagem(restored, 'e2_restaurado.png')
    print("Exercício 2 concluído")

# Exercício 3 - Implementação de Abertura e Fechamento
def abertura(img, kernel):
    """Abertura = Erosão seguida de Dilatação"""
    eroded = cv2.erode(img, kernel, iterations=1)
    opened = cv2.dilate(eroded, kernel, iterations=1)
    return opened

def fechamento(img, kernel):
    """Fechamento = Dilatação seguida de Erosão"""
    dilated = cv2.dilate(img, kernel, iterations=1)
    closed = cv2.erode(dilated, kernel, iterations=1)
    return closed

def exercicio_3():
    img = cv2.imread('Imagens/ruidos.png', cv2.IMREAD_GRAYSCALE)
    
    # Kernel para abertura (remove ruído de fundo)
    kernel_abertura = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    img_abertura = abertura(img, kernel_abertura)
    
    # Kernel para fechamento (remove ruído no objeto)
    kernel_fechamento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    img_fechamento = fechamento(img, kernel_fechamento)
    
    salvar_imagem(img, 'e3_original.png')
    salvar_imagem(img_abertura, 'e3_abertura.png')
    salvar_imagem(img_fechamento, 'e3_fechamento.png')
    print("Exercício 3 concluído")

# Exercício 4 - Extração de Fronteiras (Bordas Internas e Externas)
def borda_interna(img, kernel):
    """Borda Interna = Imagem - Erosão(Imagem)"""
    erosion = cv2.erode(img, kernel, iterations=1)
    return cv2.subtract(img, erosion)

def borda_externa(img, kernel):
    """Borda Externa = Dilatação(Imagem) - Imagem"""
    dilation = cv2.dilate(img, kernel, iterations=1)
    return cv2.subtract(dilation, img)

def exercicio_4():
    img = cv2.imread('Imagens/cachorro.png', cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    
    # Elemento estruturante 3x3
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    
    # Extrair bordas internas e externas
    b_interna = borda_interna(binary, kernel)
    b_externa = borda_externa(binary, kernel)
    
    salvar_imagem(binary, 'e4_original.png')
    salvar_imagem(b_interna, 'e4_borda_interna.png')
    salvar_imagem(b_externa, 'e4_borda_externa.png')
    print("Exercício 4 concluído")

# Exercício 5 - Preenchimento de Região
def preenchimento_regiao(img, seed_point):
    """Implementa preenchimento de região usando dilatação iterativa"""
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    
    # Complemento da imagem (para ter as bordas como barreiras)
    img_comp = cv2.bitwise_not(binary)
    
    # Criar máscara inicial com ponto semente
    h, w = binary.shape
    mask = np.zeros((h, w), np.uint8)
    mask[seed_point[1], seed_point[0]] = 255
    
    # Elemento estruturante para dilatação
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    
    # Dilatação condicional iterativa
    prev_mask = mask.copy()
    while True:
        # Dilatar e fazer AND com complemento (dilatação condicional)
        mask = cv2.dilate(mask, kernel, iterations=1)
        mask = cv2.bitwise_and(mask, img_comp)
        
        # Verificar convergência
        if np.array_equal(mask, prev_mask):
            break
        prev_mask = mask.copy()
    
    # Combinar com imagem original
    result = cv2.bitwise_or(binary, mask)
    return result

def exercicio_5():
    img = cv2.imread('Imagens/gato.png', cv2.IMREAD_GRAYSCALE)
    
    # Ponto semente no centro da imagem
    h, w = img.shape
    seed_point = (w // 2, h // 2)
    
    filled = preenchimento_regiao(img, seed_point)
    
    salvar_imagem(img, 'e5_original.png')
    salvar_imagem(filled, 'e5_preenchido.png')
    print("Exercício 5 concluído")

# Exercício 6 - Extração de Componentes Conectados
def componente_conectado(img, seed_point):
    """Extrai componente conectado a partir de um ponto semente"""
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    
    h, w = binary.shape
    mask = np.zeros((h, w), np.uint8)
    
    # Verificar se o ponto semente está em um objeto
    if binary[seed_point[1], seed_point[0]] == 0:
        print("Ponto semente não está em um objeto!")
        return mask
    
    # Inicializar com ponto semente
    mask[seed_point[1], seed_point[0]] = 255
    
    # Elemento estruturante para conectividade 8
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    
    # Dilatação condicional iterativa
    prev_mask = mask.copy()
    while True:
        # Dilatar e fazer AND com imagem binária
        mask = cv2.dilate(mask, kernel, iterations=1)
        mask = cv2.bitwise_and(mask, binary)
        
        # Verificar convergência
        if np.array_equal(mask, prev_mask):
            break
        prev_mask = mask.copy()
    
    return mask

def exercicio_6():
    img = cv2.imread('Imagens/quadrados.png', cv2.IMREAD_GRAYSCALE)
    
    print("\nExercício 6 - Extração de Componente Conectado")
    print("Informe um ponto dentro de um quadrado de 80 pixels")
    
    x = int(input("Coordenada X: "))
    y = int(input("Coordenada Y: "))
    
    # Extrair componente
    componente = componente_conectado(img, (x, y))
    
    # Criar imagem colorida com componente em amarelo
    result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    result[componente == 255] = (0, 255, 255)  # Amarelo em BGR
    
    salvar_imagem(img, 'e6_original.png')
    salvar_imagem(result, 'e6_componente_amarelo.png')
    print("Exercício 6 concluído")

# Exercício 7 - Gradiente Morfológico
def gradiente_morfologico(img, kernel):
    """Gradiente Morfológico = Dilatação - Erosão"""
    dilated = cv2.dilate(img, kernel, iterations=1)
    eroded = cv2.erode(img, kernel, iterations=1)
    return cv2.subtract(dilated, eroded)

def exercicio_7():
    img = cv2.imread('Imagens/img_aluno.png', cv2.IMREAD_GRAYSCALE)
    
    # Elemento estruturante
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    
    # Operações morfológicas
    dilated = cv2.dilate(img, kernel, iterations=1)
    eroded = cv2.erode(img, kernel, iterations=1)
    gradient = gradiente_morfologico(img, kernel)
    
    salvar_imagem(img, 'e7_original.png')
    salvar_imagem(dilated, 'e7_dilatada.png')
    salvar_imagem(eroded, 'e7_erodida.png')
    salvar_imagem(gradient, 'e7_gradiente.png')
    print("Exercício 7 concluído")

# Execução principal
if __name__ == "__main__":
    print("=" * 50)
    print("Lista 5 - Morfologia Matemática")
    print("=" * 50)
    
    print("\nExecutando Exercício 2...")
    exercicio_2()
    
    print("\nExecutando Exercício 3...")
    exercicio_3()
    
    print("\nExecutando Exercício 4...")
    exercicio_4()
    
    print("\nExecutando Exercício 5...")
    exercicio_5()
    
    print("\nExecutando Exercício 6...")
    exercicio_6()
    
    print("\nExecutando Exercício 7...")
    exercicio_7()
    
    print("\n" + "=" * 50)
    print("Todos os exercícios concluídos!")
    print("Resultados salvos na pasta 'Imagens_Resultado'")
    print("=" * 50)
