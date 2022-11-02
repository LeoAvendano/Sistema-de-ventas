import tkinter
from tkinter import *
from tkinter import messagebox
from Conexion import *

import pymysql

def vista_login():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("350x400")
    pantalla.title("Login")
    Label(text="INICIAR SESION", bg="navy", fg="white", width="100", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()
    global usuario_verify
    global password_verify
    usuario_verify = StringVar()
    password_verify = StringVar()

    global usuario_entry
    global password_entry
    Label(text="Usuario", font=("Calibri", 13)).pack()
    usuario_entry = Entry(pantalla,  width=25, font=("Calibri", 12), textvariable=usuario_verify)
    usuario_entry.pack()
    Label(pantalla).pack()
    Label(text="Contraseña", font=("Calibri", 13)).pack()
    password_entry = Entry(pantalla, show="*", width=25, font=("Calibri", 12), textvariable=password_verify)
    password_entry.pack()
    Label(pantalla).pack()
    Label(pantalla).pack()
    Button(pantalla, text="Ingresar", height="2", width="15", font=("Calibri", 15), bg="BLUE", command=login).pack()
    pantalla.mainloop()

def login():
    if validarDatos() == False:
        messagebox.showinfo(message="Faltan campos por rellenar", title="Aviso")
        return
    con = Conexion()
    bd = con.conectar()
    fcursor = bd.cursor()
    sql = "SELECT * FROM usuario WHERE " \
            "usuario = '"+usuario_verify.get()+"' and " \
            "clave = '"+password_verify.get()+"' and " \
            "estado = 1"
    try:
        fcursor.execute(sql)
        if(fcursor.fetchall()):
            messagebox.showinfo(message="Usuario y contraseña correctos", title="Aviso")
            bd.commit()
        else:
            messagebox.showinfo(message="Usuario y/o contraseña incorrectos", title="Aviso")
            bd.rollback()
    except:
        bd.rollback()
        messagebox.showinfo(message="Fallo en la conexion", title="Aviso")
    bd.close()

def validarDatos():
    usuario = usuario_verify.get()
    passw = password_verify.get()
    return len(usuario)>0 and len(passw)>0



