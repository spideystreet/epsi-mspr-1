# 🗳️ Prédicteur de Résultats Électoraux & Tableau de Bord Interactif

## ✨ Aperçu
Ce projet a pour but de prédire les résultats des élections françaises par département en utilisant des techniques de machine learning. L'objectif n'est pas seulement de prédire, mais de construire un **pipeline de données robuste et reproductible** qui alimente un **tableau de bord interactif** pour visualiser les résultats historiques et les prédictions futures.

## 🚀 Notre Pipeline de Travail
Le projet est structuré en 3 notebooks séquentiels qui forment un pipeline complet et automatisé, de la donnée brute au résultat final.

1.  `notebooks/data_preprocessing.ipynb`
    *   **Rôle :** Préparer et nettoyer les données.
    *   **Actions :** Agréger les données brutes, les charger dans une base de données PostgreSQL, appliquer la division temporelle (train < 2024, test = 2024), et sauvegarder les jeux de données traités ainsi que les outils de transformation (`preprocessor`).

2.  `notebooks/model_training.ipynb`
    *   **Rôle :** Entraîner et sélectionner le meilleur modèle.
    *   **Actions :** Tester plusieurs algorithmes (Random Forest, etc.), les évaluer sur le jeu de test de 2024, et **sauvegarder automatiquement le modèle le plus performant**.

3.  `notebooks/prediction.ipynb`
    *   **Rôle :** Générer les prédictions finales et préparer les données pour la BI.
    *   **Actions :** Charger le meilleur modèle, prédire les gagnants de "2027", et créer une table finale `election_results_for_bi` dans la base de données, combinant tous les résultats historiques et futurs pour une analyse facile.

## 📊 Visualisation avec le Tableau de Bord
Une fois le pipeline de données exécuté, un tableau de bord Streamlit est disponible pour explorer les résultats. Il permet de :
-   Visualiser les partis gagnants par département sur une carte interactive de la France.
-   Filtrer les résultats par année, y compris les **prédictions pour 2027**.
-   Consulter des statistiques agrégées et les données détaillées pour chaque année.

## 📂 Structure des Fichiers
```
.
├── data/                 # Jeux de données bruts (.csv)
├── database/
│   ├── preprocessor_X.joblib # Outil de transformation sauvegardé
│   └── label_encoder_y.joblib  # Encodeur de la cible sauvegardé
├── models/
│   └── random_forest_predictor.joblib # Meilleur modèle de prédiction
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── prediction.ipynb
├── streamlit/
│   └── dashboard.py      # Code du tableau de bord interactif
├── .env.example          # Fichier d'exemple pour les variables d'environnement
├── .env                  # Fichier de configuration (ignoré par git)
├── Dockerfile            # Définit l'environnement de l'application
├── docker-compose.yml    # Orchestre les services Docker
├── run_project.sh        # Script d'exécution du pipeline
├── README.md               # Ce fichier
└── requirements.txt        # Dépendances du projet
```

## 📊 Données Utilisées
Notre jeu de données comprend :
- Résultats électoraux historiques (participation, inscrits, votes par parti).
- Indicateurs socio-économiques (chômage, pauvreté).
- Données sociales (criminalité, immigration).

## 🐳 Installation et Lancement

### Prérequis
- [Docker](https://www.docker.com/get-started) & [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.9+](https://www.python.org/downloads/) sur votre machine locale (pour lancer le tableau de bord).

### Étape 1 : Exécuter le Pipeline de Données
Cette étape utilise Docker pour créer la base de données, traiter les données et entraîner le modèle.
1.  **Clonez le dépôt** et naviguez dans le dossier.
2.  **Configurez votre environnement :**
    -   Créez un fichier `.env` en copiant le modèle ` .env.example`.
    -   Remplissez les variables d'environnement (`PG_USER`, `PG_PASSWORD`, `PG_DBNAME`, `PG_PORT`) avec vos informations.
3.  **Lancez le projet :**
    -   Ouvrez un terminal à la racine du projet et exécutez la commande suivante :
      ```bash
      docker-compose up --build
      ```
    -   Cette unique commande va construire et démarrer les conteneurs. Le script `run_project.sh` s'exécutera automatiquement pour peupler la base de données.
    -   **Laissez ce terminal ouvert.**

### Étape 2 : Lancer le Tableau de Bord Interactif
Une fois le pipeline de l'étape 1 terminé (vous verrez les logs de l'exécution des notebooks), vous pouvez lancer le tableau de bord.
1.  **Installez les dépendances** (dans un nouveau terminal) :
    -   Il est recommandé de créer un environnement virtuel Python.
      ```bash
      python -m venv venv
      source venv/bin/activate  # Sur macOS/Linux
      # venv\Scripts\activate   # Sur Windows
      ```
    -   Installez les librairies nécessaires :
      ```bash
      pip install -r requirements.txt
      ```
2.  **Lancez le tableau de bord :**
    ```bash
    streamlit run streamlit/dashboard.py
    ```
    -   Le tableau de bord sera accessible dans votre navigateur à l'adresse indiquée (généralement `http://localhost:8501`).

### Arrêter les services
-   Pour arrêter le tableau de bord, appuyez sur `Ctrl + C` dans le terminal correspondant.
-   Pour arrêter la base de données, retournez dans le terminal de Docker et appuyez sur `Ctrl + C`, puis exécutez :
      ```bash
      docker-compose down
      ```

## 📄 Licence
Ce projet est sous licence selon les termes du fichier LICENSE.

## 👥 L'Équipe
- [@hicham](https://github.com/spideystreet)
- [@amine](https://github.com/testt753)
- [@wassim](https://github.com/Wassim38)

## 💬 Feedback
Vous avez des suggestions ou des questions ? N'hésitez pas à ouvrir une issue ou à nous contacter directement ! 