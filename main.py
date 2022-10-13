import requests as r
import json
from pprint import pprint
import sqlite3
import os
import numpy as np
import matplotlib.pyplot as plt



def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)

        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)

# Conexión con la base de datos
conexion = crear_conexion('tickerdb.db')



## Actualizacion de datos: Ingresar valor de un ticker, fecha inicio y fecha fin, enviar valores a la Api y guardarlo

multiplier = "1"
timespan = "day"
apiKey = "1ZpTnYWjNq5UmhH8hEhx0xNozdKtEg_9"
stocksticker = ""
datefrom = ""
dateto = ""




def pedirDatos():
    stocksticker = input ('Ingrese ticker a pedir: ')
    datefrom = input ('Ingrese Fecha inicial AAAA-MM-DD: ')
    dateto = input ('Ingrese fecha final AAAA-MM-DD: ')
    

    url = f"https://api.polygon.io/v2/aggs/ticker/{stocksticker}/range/{multiplier}/{timespan}/{datefrom}/{dateto}?adjusted=true&sort=asc&limit=120&apiKey={apiKey}"


    ## Request GET a la API
    lista = []  
    response = r.get(url)

    if response.status_code==200:
        json_obj = json.loads(response.text)
    #   print(json_obj)
    #   pprint(json_obj)
        
        if json_obj["queryCount"] != 0:
            print("Pidiendo datos...")
            for i in json_obj["results"]:
                v=i["v"]
                vw=i["vw"]
                o=i["o"]
                c=i["c"]
                h=i["h"]
                l=i["l"]
                t=i["t"]
                n=i["n"]
                dic = {"tickername": {stocksticker},"fecha_inicio":{datefrom},"fecha_fin":{dateto},"v":v,"vw":vw,"o":o,"c":c,"h":h,"l":l,"t":t,"n":n}
                lista.append(dic)
                
                # Creamos el curso para interactuar con los datos
                cursor = conexion.cursor()

                cursor.execute(
                """CREATE TABLE IF NOT EXISTS tickerdb(
                    ticker TEXT NOT NULL,
                    fecha_inicio DATE NOT NULL,
                    fecha_fin DATE NOT NULL,
                    v DECIMAL,
                    vw DECIMAL,
                    o DECIMAL,
                    c DECIMAL,
                    h DECIMAL,
                    l DECIMAL,
                    t DECIMAL,
                    n DECIMAL) """)

                cursor.execute(
                    f"INSERT OR IGNORE INTO tickerdb (ticker, fecha_inicio, fecha_fin, v, vw, o, c, h, l, t, n) VALUES ('{stocksticker}','{datefrom}','{dateto}','{v}','{vw}','{o}','{c}','{h}','{l}','{t}','{n}')")

                conexion.commit()
                # Cerramos la conexión
                conexion.close()
                print ("Datos guardados crrectamente")
        else:
            print ("No se pudo guardar este ticker porque no tenia valores")

            #print(json_obj)
    #print(lista)


    #guardo en un json
    with open("archivo.json", "wb") as fp:
        fp.write(response.content)


def leer_resumen (conexion):
    sql = 'SELECT * FROM tickerdb'

    cursor = conexion.cursor()
    cursor.execute(sql)

    todoslostickers = cursor.fetchall()

    for u in todoslostickers:
        print (u[0], u[1], u[2])
    #conexion.close()

def graficardatos(conexion):
    sql = "SELECT * FROM tickerdb ORDER BY fecha_inicio DESC"
    cursor = conexion.cursor()
    cursor.execute(sql)

    todoslostickers = cursor.fetchall()
    plt.title("Grafico de todos los tickers")
    
    
    x = np.linspace(0, 20, 100)  


    x= []
    n = []
    for i in todoslostickers:
        a = i[4]
        b = i[1]
        n.append(a)
        x.append(b)
    plt.plot(x, n)
    plt.show()

    #print(todoslostickers)
    #conexion.close()



def menu():
    """Limpia la pantalla y muestra nuevamente el menu"""
    os.system('cls') # para windows clear por cls, Mac clear
    print ("Selecciona una opción")
    print ("\t1 - Actualizacion de datos")
    print ("\t2 - Visualizacion de datos")
    print ("\t3 - salir")

def submenu():
    """Limpia la pantalla y muestra nuevamente el menu"""
    os.system('cls') # para windows clear por cls, Mac clear
    print ("Selecciona una opción")
    print ("\t1 - Resumen")
    print ("\t2 - Grafico de ticker")
    print ("\t3 - salir")

while True:
    # Mostramos el menu
    menu()
 
    # solicitamos una opción al usuario
    opcionMenu = input("Ingresa una opcion >> ")
 
    if opcionMenu=="1":
        pedirDatos()
        print ("")
        input("Seleccionaste la opción 1...\ningresa una tecla para continuar")
    elif opcionMenu=="2":
        submenu()
        opcionMenu = input("Ingresa una opcion >> ")
        if opcionMenu=="1":
            print ("RESUMEN")
            leer_resumen(conexion)
            print ("")
            input("Seleccionaste la opción 1 - Resumen \ningresa una tecla para volver al menu principal ")
        elif opcionMenu=="2":
            graficardatos(conexion)
            print("")
            input("Seleccionaste la opción 2 - Grafico de ticker \ningresa una tecla para volver al menu principal ")
        elif opcionMenu=="3":
            break
        else:
            print ("")
            input("Por favor ingresa una opción correcta...\ningresa una tecla para continuar")        
    elif opcionMenu=="3":
        break
    else:
        print ("")
        input("Por favor ingresa una opción correcta...\ningresa una tecla para continuar")
