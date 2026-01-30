# Classification d'images avec Deep Learning (STL-10)

Ce projet implémente une application web pour classifier des images selon les 10 classes du dataset STL-10 en utilisant un modèle de Deep Learning basé sur le Transfer Learning (MobileNet).

## Prérequis

- [Python 3.8+](https://www.python.org/downloads/)
- [TensorFlow](https://www.tensorflow.org/install?hl=fr)
- Flask
- Pillow
- [Docker](https://docs.docker.com/get-started/get-docker/) (si vous souhaiter lancer l'application sous docker)

## Lancement de l'application avec Docker
1. Clonez ce dépôt.
    ```bash
         git clone https://github.com/Akerman64/classification-stl10-webapp.git

         #entrer dans le repertoire du projet à adapter selon le système
         cd ./classification-stl10-webapp
    
    ```
2. Lancer l'application Django avec Docker puis passer à l'étape 4
  ```bash

  docker-compose up --build -d
  ```
2. Ouvrez votre navigateur à l'adresse : `http://localhost:5000`

   
## Installation normale 

1. Clonez ce dépôt.
    ```bash
         git clone https://github.com/Akerman64/classification-stl10-webapp.git

         #entrer dans le repertoire du projet à adapter selon le système
         cd ./classification-stl10-webapp
    
    ```
2. Créez un environnement virtuel (recommandé pour éviter les conflits et les erreurs de chemin long sur Windows) :
   ```bash
   python -m venv .venv
   
   # Activez l'environnement
   source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
   ```
3. Installez les dépendances :
   ```bash
   # pour l'installation des dépendances utiles au projet
   pip install -r requirements.txt
   ```
   

## Lancement de l'application

1. Assurez-vous que le modèle `mobilenet_stl10_transfer_learning.keras` est présent à la racine du projet.
3. Lancez le serveur Flask (assurez-vous que votre venv est activé) :
   ```bash
   python app.py
   ```

4. Ouvrez votre navigateur à l'adresse : `http://127.0.0.1:5000`



## Dépannage Windows (Erreur "Long Path")

Si vous rencontrez une erreur lors de l'installation de TensorFlow sur Windows (`Could not install packages due to an OSError...`), c'est souvent dû à la limite de 260 caractères des chemins de fichiers.
Solution : Installez l'environnement virtuel dans un dossier à la racine de votre disque (ex: `C:\tf_env`) plutôt que dans votre dossier utilisateur imbriqué.




## Utilisation

- Cliquez sur "Choisir un fichier" pour sélectionner une image (format .jpg, .jpeg, .png).
- Cliquez sur "Classify Image".
- Le modèle affichera les 3 classes les plus probables.

## Structure du projet

- `app.py` : Le backend Flask qui charge le modèle et gère les requêtes.
- `templates/index.html` : L'interface utilisateur.
- `requirements.txt` : Liste des dépendances.
- `mobilenet_stl10_transfer_learning.keras` : Le modèle entraîné (non inclus dans le dépôt git, à télécharger séparément si nécessaire).
- 'CNN-Transfert.ipynb' : Le notebook pour la création et l'entrainement du modèle
