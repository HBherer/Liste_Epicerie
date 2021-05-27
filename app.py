from flask import Flask
from bd import obtenir_connexion
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)  # __name__ est une variable gérée par python
CORS(app)

@app.route('/')  # représente la racine du site
def index():  # le nom n’est pas important pour le système
    return 'Page d’accueil'

@cross_origin()
@app.route('/items')
def obtenir_items():
    connexion = obtenir_connexion()
    cur = connexion.cursor()
    cur.execute(
        "SELECT * FROM item")
    resultat = cur.fetchall() 	# retourne tous les résultats et on doit boucler dessus
    liste = []
    for rangee in resultat:
        liste.append({"id": rangee[0], "nom": rangee[1], "prix": rangee[2], "unite": rangee[3]})
    return json.dumps(liste)


@app.route('/items/<id>')
def obtenir_item(id):
    connexion = obtenir_connexion()
    cur = connexion.cursor()
    cur.execute(
        "SELECT * FROM item where id = %s", (id,))
    resultat = cur.fetchall() 	# retourne tous les résultats et on doit boucler dessus
    liste = []
    for rangee in resultat:
        liste.append({"id": rangee[0], "nom": rangee[1],
                  "prix": rangee[2], "unite": rangee[3]})
    return json.dumps(liste)



if __name__ == "__main__":  # lance l’application
    app.run(debug=True)
