from conexion import mariadb_conexion
from flask import render_template
from titulos import title6, titulo6
import mysql.connector as mariadb


def mostrar_DataBase():
    try:
        with mariadb_conexion.cursor() as cursor:
        # Mostrar registros
            cursor.execute("SHOW DATABASES")
            filaDB = cursor.fetchall()
            return render_template("lista_databases.html", filaDB=filaDB, title6=title6, titulo6=titulo6)

        # Finalizar
        cursor.commit()
        cursor.close()

    except mariadb.Error as e:
        print(f"Error al conectar {e}")