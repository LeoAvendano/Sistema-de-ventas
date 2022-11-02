import tkinter
from tkinter import *
from tkinter import messagebox

import pymysql

def vista_login():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("400x500")
    pantalla.title("Login")
    Label(text="INICIO DE SESION", bg="navy", fg="white", width="100", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()
    global usuario_verify
    global password_verify
    usuario_verify = StringVar()
    password_verify = StringVar()

    global usuario_entry
    global password_entry
    Label(text="Usuario", font=("Calibri", 13)).pack()
    usuario_entry = Entry(pantalla,  width=25, font=("Calibri", 13), textvariable=usuario_verify)
    usuario_entry.pack()
    Label(pantalla).pack()

    Label(text="Contraseña", font=("Calibri", 13)).pack()
    password_entry = Entry(pantalla, width=25, font=("Calibri", 13), textvariable=password_verify)
    password_entry.pack()
    Label(pantalla).pack()



    Button(pantalla, text="Ingresar", height="2", width="15", font=("Calibri", 12), bg="BLUE").pack()
    pantalla.mainloop()

def inserta_datos():
    bd = pymysql.connect(
        host: "localhost",
        user: "root",
        password: "",
        db: "sistema_ventas"
    )


if __name__ == "__main__":
    vista_login()