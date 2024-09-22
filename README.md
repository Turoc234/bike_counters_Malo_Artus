Description
Cette application Bike Counter est une interface web développée avec Streamlit pour visualiser des données de comptage de vélos sur le boulevard de Sébastopol à Paris. Elle permet d'afficher les tendances et statistiques des passages de vélos sur une période donnée.

Démarche de création
1. Développement de l'application Streamlit
L'application a été développée à l'aide de Streamlit, un framework simple et rapide pour créer des interfaces utilisateur web en Python. Voici les étapes principales du développement :

Lecture et analyse des données de comptage de vélos (fichier CSV).
Filtrage des données selon des critères spécifiques (dates, lieux).
Création de visualisations interactives avec Matplotlib et Pandas.
Construction d'une interface utilisateur avec des contrôles permettant de choisir les dates, le lieu et d'autres paramètres.
Le fichier principal de l'application est app.py, qui contient tout le code pour charger les données et générer les visualisations.

2. Gestion des dépendances
Un fichier requirements.txt a été créé pour lister toutes les bibliothèques Python nécessaires au fonctionnement de l'application, comme Streamlit, Pandas, et Matplotlib. Cela permet de facilement installer les dépendances avec pip :

bash
Copier le code
pip install -r requirements.txt
3. Conteneurisation avec Docker
Pour rendre l'application facilement portable et déployable, nous l'avons conteneurisée avec Docker. Cela permet de s'assurer que l'application s'exécute de manière cohérente, indépendamment de l'environnement dans lequel elle est déployée.

Étapes de conteneurisation :
Création d'un Dockerfile qui spécifie l'environnement et les étapes de construction de l'image Docker.
L'image est basée sur Python et installe toutes les dépendances listées dans requirements.txt.
L'application Streamlit est configurée pour s'exécuter dans le conteneur et être accessible depuis un port défini (par exemple, 8501).
Le Dockerfile ressemble à ceci :

Dockerfile
Copier le code
# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel Streamlit fonctionnera
EXPOSE 8501

# Démarrer l'application Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
4. Lancement du conteneur
Pour exécuter l'application dans un conteneur Docker, les étapes suivantes ont été suivies :

Construire l'image Docker :

bash
Copier le code
docker build -t bike_counter_app .
Exécuter l'image en exposant le port de l'application :

bash
Copier le code
docker run -p 8501:8501 bike_counter_app
L'application est maintenant accessible via un navigateur à l'adresse http://localhost:8501.

Conclusion
Cette démarche permet de facilement développer, tester et déployer une application web de visualisation de données en Python avec Streamlit et Docker, rendant ainsi l'application portable et simple à partager ou déployer dans des environnements variés.
