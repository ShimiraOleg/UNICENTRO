import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import cv2
import numpy as np
import rastreamento
import filtros

class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Processador de Imagem e Vídeo")
        self.geometry("1000x700")

        self.imagem_original = None
        self.imagem_processada = None
        self.captura_video = None
        self.e_video = False
        self.e_camera = False
        self.vars_filtros = {}

        self.rastreador = rastreamento.Rastreamento()

        self.info_exibicao = {}
        self.imagem_pil_atual = None

        self.widgets_filtros = []
        
        self.widgets_analise_imagem = []
        self.widgets_rastreamento_video = []

        self.painel_controle = tk.Frame(self, width=250, relief=tk.RAISED, bd=2)
        self.painel_controle.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.painel_controle.pack_propagate(False) 

        self.rotulo_imagem = tk.Label(self)
        self.rotulo_imagem.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.rotulo_imagem.bind("<Button-1>", self.ao_clicar_mouse)
        self.rotulo_imagem.bind("<B1-Motion>", self.ao_arrastar_mouse)
        self.rotulo_imagem.bind("<ButtonRelease-1>", self.ao_soltar_mouse)
        
        self.criar_widgets_controle()
        self.desabilitar_controles()

    def criar_widgets_controle(self):
        frame_carregar = ttk.LabelFrame(self.painel_controle, text="1. Carregar Mídia")
        frame_carregar.pack(fill=tk.X, padx=5, pady=5)

        self.botao_carregar_imagem = tk.Button(frame_carregar, text="Carregar Imagem", command=self.carregar_imagem)
        self.botao_carregar_imagem.pack(fill=tk.X, pady=2)

        self.botao_carregar_video = tk.Button(frame_carregar, text="Carregar Vídeo", command=self.carregar_video)
        self.botao_carregar_video.pack(fill=tk.X, pady=2)

        self.botao_iniciar_camera = tk.Button(frame_carregar, text="Abrir Câmera", command=self.iniciar_camera)
        self.botao_iniciar_camera.pack(fill=tk.X, pady=2)

        self.botao_resetar = tk.Button(frame_carregar, text="Resetar Original", command=self.resetar_original)
        self.botao_resetar.pack(fill=tk.X, pady=2)

        frame_filtros = ttk.LabelFrame(self.painel_controle, text="2. Filtros e Conversões")
        frame_filtros.pack(fill=tk.X, padx=5, pady=5)

        lista_filtros = [
            "Níveis de Cinza", "Negativo", "Binarização - Otsu",
            "Media", "Mediana", "Bordas de Canny",
            "Erosão", "Dilatação", "Abertura", "Fechamento"
        ]

        for nome_filtro in lista_filtros:
            var = tk.BooleanVar(value=False)
            checkbox = tk.Checkbutton(frame_filtros, text=nome_filtro, variable=var, 
                                anchor=tk.W, command=self.ao_mudar_filtro)
            checkbox.pack(fill=tk.X)
            self.vars_filtros[nome_filtro] = var
            self.widgets_filtros.append(checkbox)

        frame_analise = ttk.LabelFrame(self.painel_controle, text="3. Análise e Rastreamento")
        frame_analise.pack(fill=tk.X, padx=5, pady=5)

        self.botao_histograma = tk.Button(frame_analise, text="Histograma", command=self.mostrar_histograma)
        self.botao_histograma.pack(fill=tk.X, pady=2)
        self.widgets_analise_imagem.append(self.botao_histograma)

        self.botao_calcular = tk.Button(frame_analise, text="Cálculo de Área, Perímetro e Diâmetro", command=self.analisar_imagem_binaria)
        self.botao_calcular.pack(fill=tk.X, pady=2)
        self.widgets_analise_imagem.append(self.botao_calcular)

        self.botao_contar_objetos = tk.Button(frame_analise, text="Contar Objetos", command=self.contar_objetos)
        self.botao_contar_objetos.pack(fill=tk.X, pady=2)
        self.widgets_analise_imagem.append(self.botao_contar_objetos)

        self.botao_rastrear = tk.Button(frame_analise, text="Selecionar Objeto", command=self.iniciar_selecao_roi)
        self.botao_rastrear.pack(fill=tk.X, pady=2)
        self.widgets_rastreamento_video.append(self.botao_rastrear)

        self.botao_rastrear = tk.Button(frame_analise, text="Detectar Cubo(s)", command=self.alternar_deteccao_cubo)
        self.botao_rastrear.pack(fill=tk.X, pady=2)
        self.widgets_rastreamento_video.append(self.botao_rastrear)

        self.botao_sair = tk.Button(self.painel_controle, text="Sair", command=self.sair)
        self.botao_sair.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=(10, 5))

    def atualizar_estado_controles(self):
        for widget in self.widgets_filtros:
            widget.config(state=tk.NORMAL)

        if self.e_video:
            for widget in self.widgets_analise_imagem:
                widget.config(state=tk.DISABLED)
        else:
            for widget in self.widgets_analise_imagem:
                widget.config(state=tk.NORMAL)
                
        if self.e_video:
            for widget in self.widgets_rastreamento_video:
                widget.config(state=tk.NORMAL)
        else:
            for widget in self.widgets_rastreamento_video:
                widget.config(state=tk.DISABLED)

    def desabilitar_controles(self):
        todos_widgets = (self.widgets_filtros + 
                       self.widgets_analise_imagem + 
                       self.widgets_rastreamento_video)
                       
        for widget in todos_widgets:
            widget.config(state=tk.DISABLED)
        
        for var in self.vars_filtros.values():
            var.set(False)

    def carregar_imagem(self):
        self.parar_midia()
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp"), ("Todos", "*.*")])
        if not caminho_arquivo:
            return

        self.imagem_original = cv2.imread(caminho_arquivo)
        self.imagem_processada = self.imagem_original.copy()
        self.e_video = False
        self.e_camera = False
        self.atualizar_exibicao(self.imagem_processada)
        self.atualizar_estado_controles()

    def carregar_video(self):
        self.parar_midia()
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("Vídeos", "*.mp4 *.avi *.mkv"), ("Todos", "*.*")])
        if not caminho_arquivo:
            return

        self.captura_video = cv2.VideoCapture(caminho_arquivo)
        if not self.captura_video.isOpened():
            print("Erro ao abrir o vídeo.")
            return
        
        self.e_video = True
        self.e_camera = False
        self.atualizar_estado_controles()
        self.transmitir_video()

    def iniciar_camera(self):
        self.parar_midia()
        self.captura_video = cv2.VideoCapture(0)
        if not self.captura_video.isOpened():
            print("Erro ao abrir a câmera.")
            return
            
        self.e_video = True
        self.e_camera = True
        self.atualizar_estado_controles()
        self.botao_iniciar_camera.config(text="Fechar Câmera", command=self.parar_midia)
        self.transmitir_video()

    def transmitir_video(self):
        if not self.e_video or not self.captura_video.isOpened():
            return

        retorno, quadro = self.captura_video.read()
        
        if retorno:
            self.imagem_original = quadro
            
            self.aplicar_logica_filtros()

            self.imagem_processada = self.rastreador.processar_quadro(
                self.imagem_original, 
                self.imagem_processada
            )
            
            self.atualizar_exibicao(self.imagem_processada)
            self.after(15, self.transmitir_video)
        else:
            if self.e_video and not self.e_camera:
                self.captura_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                self.after(15, self.transmitir_video)
            else:
                self.parar_midia()

    def atualizar_exibicao(self, quadro):
        if quadro is None:
            return

        try:
            if len(quadro.shape) == 2:
                imagem_cv = cv2.cvtColor(quadro, cv2.COLOR_GRAY2RGB)
            else:
                imagem_cv = cv2.cvtColor(quadro, cv2.COLOR_BGR2RGB)
            
            imagem_pil = Image.fromarray(imagem_cv)
            
            largura_rotulo = self.rotulo_imagem.winfo_width()
            altura_rotulo = self.rotulo_imagem.winfo_height()
            
            if largura_rotulo < 50 or altura_rotulo < 50:
                 largura_rotulo, altura_rotulo = 700, 600

            largura_img, altura_img = imagem_pil.size
            escala = min(largura_rotulo / largura_img, altura_rotulo / altura_img)
            nova_largura, nova_altura = int(largura_img * escala), int(altura_img * escala)
            
            preenchimento_x = (largura_rotulo - nova_largura) // 2
            preenchimento_y = (altura_rotulo - nova_altura) // 2
            
            if nova_largura > 0 and nova_altura > 0:
                imagem_pil = imagem_pil.resize((nova_largura, nova_altura), Image.Resampling.LANCZOS)

            self.imagem_pil_atual = imagem_pil
            self.info_exibicao = {
                'scale_w': largura_img / nova_largura if nova_largura > 0 else 1,
                'scale_h': altura_img / nova_altura if nova_altura > 0 else 1,
                'pad_x': preenchimento_x,
                'pad_y': preenchimento_y
            }
            
            imagem_tk = ImageTk.PhotoImage(image=imagem_pil)
            self.rotulo_imagem.config(image=imagem_tk)
            self.rotulo_imagem.image = imagem_tk
        except Exception as e:
            print(f"Erro ao atualizar exibição: {e}")

    def resetar_original(self):
        for var in self.vars_filtros.values():
            var.set(False)
            
        self.rastreador.parar_tudo() 

        if self.imagem_original is not None and not self.e_video:
            self.imagem_processada = self.imagem_original.copy()
            self.atualizar_exibicao(self.imagem_processada)
    
    def parar_midia(self):
        if self.captura_video:
            self.captura_video.release()
        self.captura_video = None
        self.e_video = False
        self.e_camera = False
        
        self.rastreador.parar_tudo()
        self.desabilitar_controles()
        self.botao_iniciar_camera.config(text="Abrir Câmera", command=self.iniciar_camera)

    def ao_mudar_filtro(self):
        if self.e_video:
            return
        
        if self.imagem_original is not None:
            self.aplicar_logica_filtros()
            self.atualizar_exibicao(self.imagem_processada)

    def aplicar_logica_filtros(self):
        if self.imagem_original is None:
            return

        self.imagem_processada = self.imagem_original.copy()

        if self.e_video:
            self.aplicar_filtros_cv2()
        else:
            self.aplicar_filtros_customizados()

    def aplicar_filtros_cv2(self):
        img = self.imagem_processada
        
        if self.vars_filtros["Negativo"].get():
            img = cv2.bitwise_not(img)
            
        if self.vars_filtros["Media"].get():
            img = cv2.blur(img, (5, 5))
            
        if self.vars_filtros["Mediana"].get():
            img = cv2.medianBlur(img, 5)

        e_cinza = len(img.shape) == 2

        if self.vars_filtros["Níveis de Cinza"].get() and not e_cinza:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            e_cinza = True

        if self.vars_filtros["Binarização - Otsu"].get():
            if not e_cinza:
                cinza_para_otsu = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            else:
                cinza_para_otsu = img
            _, img = cv2.threshold(cinza_para_otsu, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            e_cinza = True

        if self.vars_filtros["Bordas de Canny"].get():
            if not e_cinza:
                cinza_para_canny = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            else:
                cinza_para_canny = img
            img = cv2.Canny(cinza_para_canny, 100, 200)
            e_cinza = True

        kernel = np.ones((5, 5), np.uint8)
        
        if self.vars_filtros["Erosão"].get():
            img = cv2.erode(img, kernel, iterations=1)
            
        if self.vars_filtros["Dilatação"].get():
            img = cv2.dilate(img, kernel, iterations=1)
            
        if self.vars_filtros["Abertura"].get():
            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
            
        if self.vars_filtros["Fechamento"].get():
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

        self.imagem_processada = img
        
    def aplicar_filtros_customizados(self):
        img = self.imagem_processada.copy()
        e_cinza = len(img.shape) == 2

        if self.vars_filtros["Negativo"].get():
            img = filtros.negativo(img)
            
        if self.vars_filtros["Media"].get():
            img = filtros.filtro_media(img, 5)
            
        if self.vars_filtros["Mediana"].get():
            img = filtros.filtro_mediana(img, 5)

        if self.vars_filtros["Níveis de Cinza"].get() and not e_cinza:
            img = filtros.nivelDeCinza(img)
            e_cinza = True

        precisa_cinza = (self.vars_filtros["Binarização - Otsu"].get() or
                      self.vars_filtros["Bordas de Canny"].get() or
                      self.vars_filtros["Erosão"].get() or
                      self.vars_filtros["Dilatação"].get() or
                      self.vars_filtros["Abertura"].get() or
                      self.vars_filtros["Fechamento"].get())
        
        if precisa_cinza and not e_cinza:
            img = filtros.nivelDeCinza(img)
            e_cinza = True

        if self.vars_filtros["Binarização - Otsu"].get():
            img, _ = filtros.otsu(img)
            
        if self.vars_filtros["Bordas de Canny"].get():
            img = filtros.canny(img, 50, 150) 

        kernel = np.ones((5, 5), np.uint8)
        
        if self.vars_filtros["Erosão"].get():
            img = filtros.erosao(img, kernel)
            
        if self.vars_filtros["Dilatação"].get():
            img = filtros.dilatacao(img, kernel)
            
        if self.vars_filtros["Abertura"].get():
            img = filtros.abertura(img, kernel)
            
        if self.vars_filtros["Fechamento"].get():
            img = filtros.fechamento(img, kernel)

        self.imagem_processada = img

    def obter_cinza_processado(self):
        if self.imagem_processada is None:
            messagebox.showerror("Erro", "Nenhuma imagem carregada.")
            return None
        
        if len(self.imagem_processada.shape) == 3:
            return filtros.nivelDeCinza(self.imagem_processada)
        else:
            return self.imagem_processada.copy()

    def obter_binario_processado(self):
        img_cinza = self.obter_cinza_processado()
        if img_cinza is None:
            return None, -1
            
        if np.array_equal(img_cinza, img_cinza.astype(bool).astype(np.uint8) * 255):
             return img_cinza, -1
        
        img_bin, limiar = filtros.otsu(img_cinza)
        return img_bin, limiar

    def mostrar_histograma(self):
        img_cinza = self.obter_cinza_processado()
        if img_cinza is None:
            return

        try:
            hist = filtros.histograma(img_cinza)
            caminho_salvar = "histograma.png"
            filtros.salvar_histograma(hist, "Histograma da Imagem Processada", caminho_salvar)
            
            messagebox.showinfo("Histograma", 
                                f"Histograma salvo com sucesso como '{caminho_salvar}'.\n"
                                "(Verifique a pasta do projeto)")
        except Exception as e:
            messagebox.showerror("Erro no Histograma", f"Não foi possível gerar o histograma: {e}")

    def analisar_imagem_binaria(self):
        img_bin, limiar = self.obter_binario_processado()
        if img_bin is None:
            return

        try:
            area = filtros.calcular_area(img_bin)
            perimetro = filtros.calcular_perimetro(img_bin)
            diametro = filtros.calcular_diametro(img_bin)
            
            if limiar == -1:
                cabecalho_info = "Análise da Imagem:\n\n"
            else:
                cabecalho_info = f"Análise da Imagem (Binarizada com Otsu, L={limiar}):\n\n"
            
            info = (cabecalho_info +
                    f"Área (pixels brancos): {area}\n"
                    f"Perímetro (aprox.): {perimetro}\n"
                    f"Diâmetro (aprox.): {diametro:.2f}")
            
            messagebox.showinfo("Análise Binária", info)

        except Exception as e:
            messagebox.showerror("Erro na Análise", f"Não foi possível analisar a imagem: {e}")

    def contar_objetos(self):
        img_bin, limiar = self.obter_binario_processado()
        if img_bin is None:
            return

        try:
            kernel = np.ones((5, 5), np.uint8)
            img_limpa = filtros.abertura(img_bin, kernel)
            img_limpa = filtros.fechamento(img_limpa, kernel)
            
            num_obj, img_rotulada = filtros.contar_objetos(img_limpa)
            
            if limiar == -1:
                cabecalho_info = "Contagem de Objetos (Presumidamente Binária):\n\n"
            else:
                cabecalho_info = f"Contagem de Objetos (Binarizada com Otsu, L={limiar}):\n\n"
            
            info = (cabecalho_info +
                    f"Número de objetos encontrados: {num_obj}\n"
                    "(Após limpeza morfológica Abertura+Fechamento 5x5)")
            
            messagebox.showinfo("Contagem de Objetos", info)

        except Exception as e:
            messagebox.showerror("Erro na Contagem", f"Não foi possível contar os objetos: {e}")

    def alternar_deteccao_cubo(self):
        if not self.e_video:
            messagebox.showerror("Erro", "Inicie um vídeo ou a câmera.")
            return
            
        novo_texto = self.rastreador.alternar_deteccao()
        self.botao_rastrear.config(text=novo_texto)

    def iniciar_selecao_roi(self):
        if not self.e_video:
            messagebox.showerror("Erro", "Inicie um vídeo ou a câmera antes de selecionar.")
            return
            
        self.rastreador.iniciar_selecao_roi()
        
        messagebox.showinfo("Selecionar Objeto", 
                            "Clique e arraste no vídeo para selecionar um objeto.")
                            
    def ao_clicar_mouse(self, evento):
        if not self.rastreador.get_esta_selecionando_roi():
            return
        
        self.rastreador.set_inicio_roi((evento.x, evento.y))

    def ao_arrastar_mouse(self, evento):
        if not self.rastreador.get_esta_selecionando_roi():
            return
            
        ponto_inicio, ponto_fim = self.rastreador.set_fim_roi((evento.x, evento.y))

        if self.imagem_pil_atual and ponto_inicio:
            copia_img = self.imagem_pil_atual.copy()
            desenho = ImageDraw.Draw(copia_img)
            
            x0 = min(ponto_inicio[0], ponto_fim[0])
            y0 = min(ponto_inicio[1], ponto_fim[1])
            x1 = max(ponto_inicio[0], ponto_fim[0])
            y1 = max(ponto_inicio[1], ponto_fim[1])
            
            desenho.rectangle([(x0, y0), (x1, y1)],  
                           outline="red", width=2)
            
            imagem_tk = ImageTk.PhotoImage(image=copia_img)
            self.rotulo_imagem.config(image=imagem_tk)
            self.rotulo_imagem.image = imagem_tk

    def ao_soltar_mouse(self, evento):
        if not self.rastreador.get_esta_selecionando_roi():
            return
            
        ponto_inicio, ponto_fim = self.rastreador.get_pontos_roi()
        self.rastreador.parar_selecao_roi()
        
        if ponto_inicio is None or ponto_fim is None:
            return

        try:
            info = self.info_exibicao
            
            x1_label = ponto_inicio[0] - info['pad_x']
            y1_label = ponto_inicio[1] - info['pad_y']
            x2_label = ponto_fim[0] - info['pad_x']
            y2_label = ponto_fim[1] - info['pad_y']

            orig_x1 = x1_label * info['scale_w']
            orig_y1 = y1_label * info['scale_h']
            orig_x2 = x2_label * info['scale_w']
            orig_y2 = y2_label * info['scale_h']
            
            x = int(min(orig_x1, orig_x2))
            y = int(min(orig_y1, orig_y2))
            w = int(abs(orig_x1 - orig_x2))
            h = int(abs(orig_y1 - orig_y2))

            if w == 0 or h == 0:
                print("Seleção inválida (tamanho 0).")
                self.atualizar_exibicao(self.imagem_processada)
                return

            bbox = (x, y, w, h)
            
            self.rastreador.iniciar_rastreamento(self.imagem_original, bbox)
            
            self.atualizar_exibicao(self.imagem_processada)
            
        except Exception as e:
            print(f"Erro ao converter ROI: {e}")
            self.rastreador.parar_selecao_roi()

    def sair(self):
        self.rastreador.limpar()
        self.parar_midia()
        self.destroy()

if __name__ == "__main__":
    app = Aplicativo()
    app.mainloop()