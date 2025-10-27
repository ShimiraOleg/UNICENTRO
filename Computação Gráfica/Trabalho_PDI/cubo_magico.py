import cv2
import numpy as np

def detectar_cubos_magicos(quadro):
    hsv = cv2.cvtColor(quadro, cv2.COLOR_BGR2HSV)

    vermelho_min1 = np.array([0, 180, 120])
    vermelho_max1 = np.array([10, 255, 255])
    vermelho_min2 = np.array([170, 180, 120])
    vermelho_max2 = np.array([180, 255, 255])
    
    verde_min = np.array([40, 180, 120])
    verde_max = np.array([80, 255, 255])
    
    azul_min = np.array([90, 180, 120])
    azul_max = np.array([130, 255, 255])
    
    amarelo_min = np.array([20, 180, 120])
    amarelo_max = np.array([35, 255, 255])
    
    laranja_min = np.array([11, 180, 120])
    laranja_max = np.array([19, 255, 255])
    
    mascara_vermelho1 = cv2.inRange(hsv, vermelho_min1, vermelho_max1)
    mascara_vermelho2 = cv2.inRange(hsv, vermelho_min2, vermelho_max2)
    mascara_vermelho = cv2.bitwise_or(mascara_vermelho1, mascara_vermelho2)
    mascara_verde = cv2.inRange(hsv, verde_min, verde_max)
    mascara_azul = cv2.inRange(hsv, azul_min, azul_max)
    mascara_amarelo = cv2.inRange(hsv, amarelo_min, amarelo_max)
    mascara_laranja = cv2.inRange(hsv, laranja_min, laranja_max)
    
    mascara = cv2.bitwise_or(mascara_vermelho, mascara_verde)
    mascara = cv2.bitwise_or(mascara, mascara_azul)
    mascara = cv2.bitwise_or(mascara, mascara_amarelo)
    mascara = cv2.bitwise_or(mascara, mascara_laranja)
    
    kernel_abertura = np.ones((5, 5), np.uint8)
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel_abertura, iterations=1)
    kernel_fechamento = np.ones((20, 20), np.uint8)
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel_fechamento, iterations=1) 

    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contornos:
        return [] 

    caixas_delimitadoras = []
    area_minima = 1000
    
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        
        if area > area_minima:
            caixas_delimitadoras.append(cv2.boundingRect(contorno))
            
    return caixas_delimitadoras