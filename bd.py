import mysql.connector

def obtenir_connexion():
  try:
    conn = mysql.connector.connect(
              user="root",
              password="root",
              host="127.0.0.1",
              port=3306, 
              database="epicerie")
    return conn
  except mysql.connector.Error as e:
    print(e)