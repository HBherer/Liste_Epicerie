# ListeÉpicerie

### Progressive web app développée avec Flask, Vue.JS et MySQL

Dans le cadre du cours Techniques d'Intégration 2 - Cégep Garneau

## Pour utiliser ce projet localement avec MacOS

1. Fork/Clone le dépôt

1. Créez une base de donnée locale MySQL nommée epicerie et importez les données fournies

1. Lancez le backend Python en utilisant un terminal

    ```sh
    $ python3.9 -m venv venv 
    $ source venv/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ python3.9 app.py
    ```

    Naviguez à l'adresse suivante : [http://localhost:5000](http://localhost:5000)

1. Lancez l'application Vue.JS en utilisant un terminal différent

    ```sh
    $ npm install
    $ npm run serve
    ```

    Naviguez à l'adresse suivante : [http://localhost:8080](http://localhost:8080)

1. Modifiez le fichier bd.py à la ligne 7 et ajoutez le mot de passe root

## Pour utiliser ce projet localement avec Windows

1. Fork/Clone le dépôt

1. Créez une base de donnée locale MySQL nommée epicerie et importez les données fournies

1. Lancez le backend Python en utilisant un terminal

    ```sh
    $ python -m venv venv 
    $ .\venv\Scripts\activate
    (env)$ pip install -r requirements.txt
    (env)$ python .\app.py
    ```

    Naviguez à l'adresse suivante : [http://localhost:5000](http://localhost:5000)

1. Lancez l'application Vue.JS en utilisant un terminal différent

    ```sh
    $ npm install
    $ npm run serve
    ```

    Naviguez à l'adresse suivante : [http://localhost:8080](http://localhost:8080)
