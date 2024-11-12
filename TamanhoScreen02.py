import tkinter as tk
w=tk.Tk()
w.title('FULL Y OVER')
w.geometry('400x300+0+0')
w.attributes('-fullscreen',0)

def desover():
    w.overrideredirect(0)
def over():
    w.overrideredirect(1)
def deszoom():
    w.attributes('-fullscreen',0)
def zoom():
    w.attributes('-fullscreen',1)

b0=tk.Button(w,text="SIN OVER",command=(desover)).pack()
b0=tk.Button(w,text="CON OVER",command=(over)).pack()
b0=tk.Button(w,text="SIN FULL",command=(deszoom)).pack()
b0=tk.Button(w,text="CON FULL",command=(zoom)).pack()
b1=tk.Button(w,text="EXIT",command=(exit)).pack()

w.mainloop()