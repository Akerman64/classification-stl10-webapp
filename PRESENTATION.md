# Support de Présentation

## Slide 1 : Titre
**Classification d'Images pour l'Association de Protection des Animaux**
*Sous-titre : Automatisation de l'indexation des pensionnaires via Deep Learning*
*Auteurs : Votre Équipe*

---

## Slide 2 : Contexte & Problématique
**Le Besoin**
- Association avec une base de données grandissante de photos d'animaux.
- Manque de temps pour l'indexation manuelle.
- **Objectif** : Algorithme capable de classer automatiquement les images (ici démontré sur les 10 classes STL-10 incluant chiens, chats, etc.).

---

## Slide 3 : Les Données (STL-10)
**Le Dataset**
- Utilisation de STL-10 pour l'entraînement.
- 10 classes : Avion, Oiseau, Voiture, Chat, Cerf, Chien, Cheval, Singe, Bateau, Camion.
- **Pré-traitement** : 
  - Redimensionnement (Resize).
  - Data Augmentation (Rotation, Zoom, Flip) pour enrichir le dataset et éviter l'overfitting.

---

## Slide 4 : Approche 1 - CNN "Maison"
**Architecture Personnalisée**
- Construction d'un réseau de neurones convolutif (CNN) à partir de zéro.
- Couches : Conv2D, MaxPooling, Flatten, Dense.
- **Résultats** :
  - Précision atteinte : X %
  - Temps d'entraînement : Long
  - Difficulté : Nécessite beaucoup de données pour bien généraliser.

---

## Slide 5 : Approche 2 - Transfer Learning
**La Solution Retenue**
- Utilisation d'un modèle pré-entraîné : **MobileNet**.
- **Pourquoi ?** 
  - Déjà entraîné sur ImageNet (millions d'images).
  - Capable d'extraire des features complexes (formes, textures).
  - Ré-entraînement (Fine-tuning) uniquement des dernières couches pour nos 10 classes.

---

## Slide 6 : Comparaison & Résultats
**Performance**
- **CNN Maison** : Précision modérée (~60-70%), apprentissage lent.
- **Transfer Learning** : Précision excellente (>90%), apprentissage très rapide.
- **Choix Final** : MobileNet pour sa rapidité et sa robustesse, idéal pour une application web.

---

## Slide 7 : L'Application Web
**Interface Utilisateur**
- Développement d'une WebApp simple et intuitive.
- **Fonctionnement** :
  1. Le bénévole upload une photo.
  2. Le modèle analyse l'image en temps réel.
  3. L'application affiche le Top 3 des catégories probables.

---

## Slide 8 : Déploiement & Architecture
**Mise en Production**
- **Backend** : Python / Flask.
- **Frontend** : HTML / CSS.
- **DevOps** : 
  - Code hébergé sur GitHub.
  - CI/CD via Azure Pipelines.
  - Déploiement possible sur Azure Web App.

---

## Slide 9 : Impact pour l'Association
**Bénéfices Concrets**
- **Gain de temps** : Indexation quasi-instantanée.
- **Simplicité** : Aucune compétence technique requise pour les bénévoles.
- **Scalabilité** : Peut gérer des milliers de photos sans effort supplémentaire.

---

## Slide 10 : Conclusion & Perspectives
**Bilan**
- Objectif atteint : Solution fonctionnelle et performante.
- **Futur** :
  - Étendre à plus de races de chiens (Stanford Dogs).
  - Application mobile pour prise de photo directe.
  - Intégration directe à la base de données de l'association.
