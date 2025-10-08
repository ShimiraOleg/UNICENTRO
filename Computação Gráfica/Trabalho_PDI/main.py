import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import cv2
from PIL import Image, ImageTk
import numpy as np

class SistemaPDI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Processamento Digital de Imagens")
        self.root.geometry("1280x720")

        # Variáveis
        self.imagem_original = None
        self.imagem_processada = None
        self.cap = None
        self.video_ativo = False

        # Criar interface
        self.criar_menu()
        self.criar_interface()

    # ==================== GUI ====================

    def criar_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menu Arquivo
        menu_arquivo = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=menu_arquivo)
        menu_arquivo.add_command(label="Carregar Imagem", command=self.carregar_imagem)
        menu_arquivo.add_command(label="Salvar Imagem", command=self.salvar_imagem)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.root.quit)

        # Menu Vídeo
        menu_video = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Vídeo", menu=menu_video)
        menu_video.add_command(label="Iniciar Câmera", command=self.iniciar_camera)
        menu_video.add_command(label="Parar Câmera", command=self.parar_camera)

    def criar_interface(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Controles
        frame_controles = ttk.LabelFrame(main_frame, text="Controles", padding=10)
        frame_controles.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))

        ttk.Label(frame_controles, text="Aquisição:", font=('Arial', 10, 'bold')).pack(pady=(0, 5))
        ttk.Button(frame_controles, text="Carregar Imagem", command=self.carregar_imagem).pack(fill=tk.X, pady=2)
        ttk.Button(frame_controles, text="Iniciar Câmera", command=self.iniciar_camera).pack(fill=tk.X, pady=2)
        ttk.Button(frame_controles, text="Parar Câmera", command=self.parar_camera).pack(fill=tk.X, pady=2)

        # Exibição
        frame_exibicao = ttk.LabelFrame(main_frame, text="Visualização", padding=10)
        frame_exibicao.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(frame_exibicao, bg='gray25')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Informações
        frame_info = ttk.LabelFrame(self.root, text="Informações", padding=10)
        frame_info.pack(fill=tk.X, padx=10, pady=(0, 10))
        self.label_info = ttk.Label(frame_info, text="Carregue uma imagem ou inicie a câmera para começar")
        self.label_info.pack()

    # ==================== IMAGEM E CÂMERA ====================

    def carregar_imagem(self):
        arquivo = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.tiff"), ("Todos", "*.*")]
        )
        if arquivo:
            self.imagem_original = cv2.imread(arquivo)
            self.imagem_processada = self.imagem_original.copy()
            self.exibir_imagem(self.imagem_processada)
            self.label_info.config(text=f"Imagem carregada: {arquivo}")

    def salvar_imagem(self):
        if self.imagem_processada is not None:
            arquivo = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("Todos", "*.*")]
            )
            if arquivo:
                cv2.imwrite(arquivo, self.imagem_processada)
                messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nenhuma imagem para salvar")

    def iniciar_camera(self):
        if not self.video_ativo:
            self.cap = cv2.VideoCapture(0)
            if self.cap.isOpened():
                self.video_ativo = True
                self.label_info.config(text="Câmera ativa - processamento em tempo real")
                self.processar_video()
            else:
                messagebox.showerror("Erro", "Não foi possível acessar a câmera")

    def parar_camera(self):
        self.video_ativo = False
        if self.cap:
            self.cap.release()
        self.label_info.config(text="Câmera desativada")

    def processar_video(self):
        if self.video_ativo and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                self.imagem_processada = frame
                self.exibir_imagem(frame)
                self.root.after(10, self.processar_video)

    def exibir_imagem(self, imagem):
        if imagem is None:
            return

        if len(imagem.shape) == 3:
            imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        else:
            imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_GRAY2RGB)

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if canvas_width > 1 and canvas_height > 1:
            h, w = imagem_rgb.shape[:2]
            aspect = w / h
            if w > canvas_width or h > canvas_height:
                if canvas_width / canvas_height > aspect:
                    new_h = canvas_height
                    new_w = int(aspect * new_h)
                else:
                    new_w = canvas_width
                    new_h = int(new_w / aspect)
                imagem_rgb = cv2.resize(imagem_rgb, (new_w, new_h))

        imagem_pil = Image.fromarray(imagem_rgb)
        imagem_tk = ImageTk.PhotoImage(imagem_pil)
        self.canvas.delete("all")
        self.canvas.create_image(
            canvas_width // 2, 
            canvas_height // 2, 
            image=imagem_tk, 
            anchor=tk.CENTER
        )
        self.canvas.image = imagem_tk

# ==================== MAIN ====================

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaPDI(root)
    root.mainloop()
