import tkinter
from tkinter import *
from tkinter import messagebox
from Conexion import *


class Principal():

    def __init__(self):
        pass

    def ventana(self):
        ventana = Tk()
        ventana.title("Ejemplo Frame")
        ventana.geometry("200x70")

        frame1 = Frame(ventana, bg="blue")
        frame1.pack(expand=True, fill='both')

        frame2 = Frame(ventana, bg="yellow")
        frame2.pack(expand=True, fill='both')

        ventana.mainloop()

    def ventana_principal(self):
        master = Tk()
        master.geometry("350x400")
        self.master = master
        Label(text="VISTA PRINCIPAL", bg="navy", fg="white", width="100", height="3", font=("Calibri", 15)).pack()
        Label(text="").pack()
        global usuario_verify
        global password_verify
        usuario_verify = StringVar()
        password_verify = StringVar()
        global usuario_entry
        global password_entry
        Label(text="Usuario", font=("Calibri", 13)).pack()
        usuario_entry = Entry(master, width=25, font=("Calibri", 12), textvariable=usuario_verify)
        usuario_entry.pack()
        Label(master).pack()
        Label(text="Contraseña", font=("Calibri", 13)).pack()
        password_entry = Entry(master, show="*", width=25, font=("Calibri", 12), textvariable=password_verify)
        password_entry.pack()
        Label(master).pack()
        Label(master).pack()
        Button(master, text="Ingresar", height="2", width="15", font=("Calibri", 15), bg="BLUE",
               command=self.login).pack()
        self.pack()
        self.create_widgets()
        master.mainloop()
