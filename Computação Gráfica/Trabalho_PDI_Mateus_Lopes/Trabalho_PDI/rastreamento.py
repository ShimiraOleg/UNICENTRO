import cv2
import numpy as np
import pygame
import cubo_magico as cubo_magico
from tkinter import messagebox

class Rastreamento:
    def __init__(self):
        self.rastreador = None
        self.esta_rastreando = False
        
        self.esta_detectando_cubo = False
        self.musica_tocando = False

        self.esta_selecionando_roi = False
        self.ponto_inicio_roi = None
        self.ponto_fim_roi = None

        self._iniciar_musica()

    def _iniciar_musica(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load("Assets/audio/musica_track.mp3") 
        except Exception as e:
            print(f"Erro ao carregar música: {e}")
            messagebox.showwarning("Aviso de Música", 
                                   "Não foi possível carregar 'musica_track.mp3'.\n"
                                   "A função de música não funcionará.")

    def processar_quadro(self, quadro_original, quadro_processado):
        
        if self.esta_rastreando and self.rastreador is not None:
            try:
                sucesso, bbox = self.rastreador.update(quadro_original) 
                
                if sucesso:
                    (x, y, w, h) = [int(v) for v in bbox]
                    cv2.rectangle(quadro_processado, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(quadro_processado, "Objeto (6a)", (x, y - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                else:
                    self.parar_rastreamento()
            except Exception as e:
                print(f"Erro no rastreador: {e}")
                self.parar_rastreamento()

        if self.esta_detectando_cubo:
            bboxes = cubo_magico.detectar_cubos_magicos(quadro_original)
            
            if bboxes:
                for bbox in bboxes:
                    (x, y, w, h) = [int(v) for v in bbox]
                    cv2.rectangle(quadro_processado, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(quadro_processado, "Cubo Magico", (x, y - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                if not self.musica_tocando:
                    pygame.mixer.music.play(-1)
                    self.musica_tocando = True
            else:
                if self.musica_tocando:
                    pygame.mixer.music.stop()
                    self.musica_tocando = False
        
        return quadro_processado

    def iniciar_rastreamento(self, quadro, bbox):
        if self.esta_rastreando:
            self.parar_rastreamento()
            
        try:
            self.rastreador = cv2.legacy.TrackerCSRT_create()
            self.rastreador.init(quadro, bbox)
            self.esta_rastreando = True
            print(f"Iniciando rastreamento (6a) no BBox: {bbox}")
        except Exception as e:
            print(f"Erro ao iniciar rastreador 6a: {e}")
            self.rastreador = None
            self.esta_rastreando = False

    def parar_rastreamento(self):
        self.esta_rastreando = False
        self.rastreador = None

    def alternar_deteccao(self):
        if self.esta_detectando_cubo:
            self.parar_deteccao()
            return "Detectar Cubo(s)"
        else:
            self.parar_rastreamento()
            
            self.esta_detectando_cubo = True
            return "Parar Detecção"

    def parar_deteccao(self):
        if self.musica_tocando:
            pygame.mixer.music.stop()
            self.musica_tocando = False
        
        self.esta_detectando_cubo = False

    def iniciar_selecao_roi(self):
        self.parar_tudo()
        self.esta_selecionando_roi = True
        print("Modo de seleção de ROI ativado.")
    
    def parar_selecao_roi(self):
        self.esta_selecionando_roi = False
        self.ponto_inicio_roi = None
        self.ponto_fim_roi = None
    
    def get_esta_selecionando_roi(self):
        return self.esta_selecionando_roi
        
    def set_inicio_roi(self, ponto):
        if self.esta_selecionando_roi:
            self.ponto_inicio_roi = ponto
            self.ponto_fim_roi = ponto
            
    def set_fim_roi(self, ponto):
        if self.esta_selecionando_roi:
            self.ponto_fim_roi = ponto
        return self.ponto_inicio_roi, self.ponto_fim_roi
        
    def get_pontos_roi(self):
        return self.ponto_inicio_roi, self.ponto_fim_roi
    
    def parar_tudo(self):
        self.parar_rastreamento()
        self.parar_deteccao()
        self.parar_selecao_roi()
        
    def limpar(self):
        if self.musica_tocando:
            pygame.mixer.music.stop()