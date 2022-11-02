import tkinter
from tkinter import *
from tkinter import messagebox
from Conexion import *

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
    password_entry = Entry(pantalla, show="*", width=25, font=("Calibri", 13), textvariable=password_verify)
    password_entry.pack()
    Label(pantalla).pack()



    Button(pantalla, text="Ingresar", height="2", width="15", font=("Calibri", 12), bg="BLUE", command=validar_datos).pack()
    pantalla.mainloop()

def validar_datos():
    bd = pymysql.connect(
        host= "localhost",
        port=2974,
        user= "root",
        password= "",
        db= "sistema_ventas"
    )
    fcursor = bd.cursor()
    sql = "SELECT COUNT(*) FROM usuario"
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Conexion exitosa", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="Fallo en la conexion", title="Aviso")
    bd.close()



