import tkinter as tk

def imprimir_informacion(r):
    altura = r.winfo_reqheight()
    anchura = r.winfo_reqwidth()
    altura_pantalla = r.winfo_screenheight()
    anchura_pantalla = r.winfo_screenwidth()
    print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")


raiz = tk.Tk()
raiz.etiqueta = tk.Label(
    raiz, text="Hola Tkinter!\nProgramando en Python\nparzibyte.me"*5)
raiz.etiqueta.pack(side="top")
app = tk.Frame()
app.pack()
raiz.update()
imprimir_informacion(raiz)
app.mainloop()