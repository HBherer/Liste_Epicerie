import mysql.connector

def obtenir_connexion():
    try:
        conn = mysql.connector.connect(

        )
        return conn
    except mysql.connector.Error as e:
        print(e)