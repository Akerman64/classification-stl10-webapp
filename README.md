# Classification d'images avec Deep Learning (STL-10)

Ce projet implémente une application web pour classifier des images selon les 10 classes du dataset STL-10 en utilisant un modèle de Deep Learning basé sur le Transfer Learning (MobileNet).

## Prérequis

- Python 3.8+
- TensorFlow
- Flask
- Pillow

## Installation

1. Clonez ce dépôt.
2. Créez un environnement virtuel (recommandé pour éviter les conflits et les erreurs de chemin long sur Windows) :
   ```bash
   # Sur Windows, créez l'environnement dans un chemin court (ex: C:\env) pour éviter les erreurs de limite de chemin
   python -m venv C:\Users\User\tf_env
   
   # Activez l'environnement
   C:\Users\User\tf_env\Scripts\activate
   ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Lancement de l'application

1. Assurez-vous que le modèle `mobilenet_stl10_transfer_learning.keras` est présent à la racine du projet.
2. Lancez le serveur Flask (assurez-vous que votre venv est activé) :
   ```bash
   python app.py
   ```
3. Ouvrez votre navigateur à l'adresse : `http://127.0.0.1:5000`

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

## Organisation DevOps

Voir le fichier [DEVOPS.md](DEVOPS.md) pour les détails sur l'organisation Agile et les pipelines CI/CD.
