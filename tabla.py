import sqlite3

# Creamos una conexión con la base de datos
con = sqlite3.connect('tickerdb.db')

# Creamos el curso para interactuar con los datos
cursor = con.cursor()


# Ejecutar comandos de SQL crear campos
cursor.execute(
    """CREATE TABLE IF NOT EXISTS tickerdb(
        ticker TEXT PRIMARY KEY,
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

con.commit()
# Cerramos la conexión
con.close()