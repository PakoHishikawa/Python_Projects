import tkinter as tk
from tkinter import ttk
import util.util_ventana as util_ven
import util.util_imagenes as util_img
import config as conf

class FormMaestroDesign(tk.Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.qr_guardado = None
        self.qr_img_base = util_img.leer_imagen("./imagenes/qr_base.png", (330,330))
        self.qr_mensaje = util_img.leer_imagen("./imagenes/escanea_me.png", (300,200))
        self.config_window()
        
    def config_window(self):
        self.title('QR Diseño de Código')
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 800, 450
        util_ven.centrar_ventana(self, w, h)