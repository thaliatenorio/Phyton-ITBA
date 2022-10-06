
import sqlite3
#import numpy as np
import matplotlib.pyplot as plt


def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)

        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)

conexion = crear_conexion('tickerdb.db')

def leer_resumen (conexion):
    sql = 'SELECT * FROM tickerdb'

    cursor = conexion.cursor()
    cursor.execute(sql)

    todoslostickers = cursor.fetchall()

    for u in todoslostickers:
        print (u[0], u[1], u[2])

tickergraficar = input ('>>> Ingrese el ticker a graficar: ')

ax = plt.subplots(dpi=80, figsize=(7,5),facecolor='black')
plt.title("Grafico")
ax.set_xlabel("Fecha")
ax.set_ylabel("valores")

def obtenerdatos(self):
    self.cursor.execute("SELECT * FROM tickerdb")
    self.datos = self.cursor.fetchall()
    self.conexion.close()

    x= []
    n = []
    for i in self.datos:
        a = i[0]
        b = i[1]
        n.append(a)
        x.append(b)
    self.ax.plot(n, x)
    self.canvas.draw()
    plt.grid(alpha=0.5)

    print(n,x)
    

obtenerdatos()



