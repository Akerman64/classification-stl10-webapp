# Organisation DevOps Azure

## Méthodologie Agile / Scrum

Nous utilisons un Board Azure DevOps pour gérer le projet selon la méthode Scrum.

### Membres de l'équipe et Rôles
- **Product Owner** : Définit les fonctionnalités (User Stories) et priorise le Backlog.
- **Scrum Master** : Facilite les cérémonies (Daily, Sprint Planning, Review, Retrospective).
- **Développeurs** : Implémentent les tâches (Data Science, Backend, Frontend).

### Structure du Board
- **Epics** : 
  - "Création du modèle Deep Learning"
  - "Développement de l'application Web"
  - "Déploiement et CI/CD"
- **Backlog** : Liste des User Stories.
- **Sprints** : Cycles de 2 semaines.
  - *Sprint 1* : Exploration des données, Data Augmentation, Premier CNN.
  - *Sprint 2* : Transfer Learning, Optimisation, Création de l'API Flask.
  - *Sprint 3* : Frontend, Intégration, Mise en production.

## Pipelines CI/CD

Nous avons mis en place des pipelines Azure pour l'intégration continue et le déploiement continu.

### Continuous Integration (CI)
Déclenché à chaque `push` sur la branche `main` ou `develop`.

1. **Build** :
   - Installation des dépendances Python.
   - Vérification du code (Linting avec `flake8`).
2. **Test** :
   - Exécution des tests unitaires (ex: `python test_app.py`).
   - Vérification que le modèle se charge correctement.

### Continuous Deployment (CD)
Déclenché après un succès du pipeline CI sur la branche `main`.

1. **Packaging** :
   - Création d'un conteneur Docker contenant l'application Flask et le modèle.
2. **Deploy** :
   - Pousse l'image Docker sur Azure Container Registry (ACR).
   - Déploie l'instance de conteneur sur Azure App Service (Web App for Containers).
   - L'application est alors accessible via une URL publique Azure.

## Monitoring
- Utilisation d'Azure Application Insights pour surveiller les performances et les erreurs de l'application en production.
