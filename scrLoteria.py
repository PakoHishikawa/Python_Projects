from tkinter import ttk, messagebox, font
import tkinter as tk
import os.path
from loterias.mod_loterias.LoteriaX import *

class MenuBarraGeral(tk.Tk):

	def __init__(self):

		super().__init__()
		self.__icMenu=os.path.abspath(r"C:\Users\user\OneDrive\Escritorio\Projetos Phyton\loterias\img_loterias\cef001.ico")
		#C:\Users\user\Desktop\Projetos Phyton\loterias\img_loterias\cef001.ico
		self.__icMegasena=os.path.abspath(r"C:\Users\user\OneDrive\Escritorio\Projetos Phyton\loterias\img_loterias\megasena3.png")
		
		self.inicializar_GUI()
	

	def inicializar_GUI(self):

		mnPrincipal=tk.Menu(self)
		mnArquivo=tk.Menu(mnPrincipal, tearoff=0)
		mnRegistros=tk.Menu(mnPrincipal, tearoff=0)

		img_Megasena=tk.PhotoImage(file=self.__icMegasena)
		

		altura_pantalla=mnPrincipal.winfo_screenheight()
		anchura_pantalla=mnPrincipal.winfo_screenwidth()

		self.title("Lotérica Caixa Econômica Federal")
		self.iconbitmap(self.__icMenu)
		self.geometry("%dx%d+0+0" % (anchura_pantalla, altura_pantalla))


		mnPrincipal.add_cascade(label="Loterias", menu=mnArquivo)
		mnPrincipal.add_cascade(label="Registros", menu=mnRegistros)
		mnPrincipal.add_command(label="Sair", command=self.destroy)

		mnArquivo.add_command(label="milhonaria",
			command=self.f_milhonaria,
			image=img_Megasena,
			compound=tk.LEFT)

		mnArquivo.add_command(label="megasena",
			command=self.f_megasena,
			image=img_Megasena,
			compound=tk.LEFT)
  
		mnArquivo.add_command(label="quina",
            command=self.f_quina,
			image=img_Megasena,
			compound=tk.LEFT)
  
		mnArquivo.add_command(label="lotofacil",
            command=self.f_lotofacil,
			image=img_Megasena,
			compound=tk.LEFT)
  
		mnArquivo.add_command(label="lotomania",
            command=self.f_lotomania,
			image=img_Megasena,
			compound=tk.LEFT)
  
		mnArquivo.add_command(label="timemania")
  
		mnArquivo.add_command(label="dupla sena",
            command=self.f_duplasena,
			image=img_Megasena,
			compound=tk.LEFT)
  
		mnArquivo.add_command(label="federal")
  
		mnArquivo.add_command(label="loteca")
  
		mnArquivo.add_command(label="dia da sorte",
            command=self.f_diadasorte,
			image=img_Megasena,
			compound=tk.LEFT)
  
		mnArquivo.add_command(label="super sete")
		self.config(menu=mnPrincipal)

	def f_milhonaria(self):		
		cLoteria=LoteriaX()
		print(cLoteria.getMilhonaria())		

	def f_megasena(self):		
		cLoteria=LoteriaX()
		print(cLoteria.getMegasena())

	def f_quina(self):	
		cLoteria=LoteriaX()
		print(cLoteria.getQuina())			

	def f_lotofacil(self):		
		cLoteria=LoteriaX()
		print(cLoteria.getLotofacil())

	def f_lotomania(self):		
		cLoteria=LoteriaX()
		print(cLoteria.getLotomania())

	def f_diadasorte(self):		
		cLoteria=LoteriaX()
		print(cLoteria.getDiadasorte())

	def f_duplasena(self):		
		cLoteria=LoteriaX()
		print(cLoteria.getDuplasena())

def main():
	app = MenuBarraGeral()
	app.mainloop()

if __name__ == '__main__':
	main()
