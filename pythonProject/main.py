import tkinter as tk
from comunicare import comanda_trm

#Creez fereastra radacina
root = tk.Tk()
root.title("Control Servo")

f_canva = tk.Canvas(root, width=220, height=100, bg="white")
f_canva.pack(pady=20)

buton_deschide = f_canva.create_oval(10, 10, 90, 90, fill="blue", outline="black", width=2)
buton_inchide = f_canva.create_oval(120, 10, 200, 90, fill="red", outline="black", width=2)

f_canva.create_text(50, 50, text="deschide", font=("Arial", 10, "bold"), fill="black")
f_canva.create_text(160, 50,text="inchide", font=("Arial", 10, "bold"), fill="black")

def apasa_deschide(event):
    """Eveniment apăsare buton de deschidere"""
    comanda_trm("deschide")

def apasa_inchide(event):
    """Eveniment apăsare buton de închidere  """
    comanda_trm("inchide")

# Legătura evenimentelor pentru apăsarea butoanelor
f_canva.tag_bind(buton_deschide, "<ButtonPress-1>", apasa_deschide)
f_canva.tag_bind(buton_inchide, "<ButtonPress-1>", apasa_inchide)

#Rularea interfeței grafice pana cand o oprim
root.mainloop()
