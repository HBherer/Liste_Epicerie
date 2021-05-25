import mysql.connector

def obtenir_connexion():
  try:
    conn = mysql.connector.connect(
              user="root",
              password="",
              host="127.0.0.1",
              port=3306, 
              database="tp4")
    return conn
  except mysql.connector.Error as e:
    print(e)