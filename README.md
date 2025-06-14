# 🗳️ Prédicteur de Résultats Électoraux

## ✨ Aperçu
Ce projet a pour but de prédire les résultats des élections françaises par département en utilisant des techniques de machine learning. L'objectif n'est pas seulement de prédire, mais de construire un **pipeline robuste, reproductible et méthodologiquement correct** qui évite les pièges courants de l'analyse de données temporelles.

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

## 🐳 Installation et Lancement avec Docker

### Prérequis
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Lancement
1.  **Clonez le dépôt** et naviguez dans le dossier.
2.  **Configurez votre environnement :**
    -   Créez un fichier `.env` en copiant le modèle ` .env.example`.
    -   Remplissez les variables d'environnement (`PG_USER`, `PG_PASSWORD`, `PG_DBNAME`, `PG_PORT`) avec vos informations.
3.  **Lancez le projet :**
    -   Ouvrez un terminal à la racine du projet et exécutez la commande suivante :
      ```bash
      docker-compose up --build
      ```
    -   Cette unique commande va :
        1.  Construire l'image de votre application.
        2.  Démarrer un conteneur pour la base de données PostgreSQL.
        3.  Démarrer le conteneur de l'application qui exécutera automatiquement le script `run_project.sh`.
        4.  Le script attendra que la base de données soit prête, puis lancera les 3 notebooks en séquence, peuplant la base et entraînant le modèle.

4.  **Accéder aux résultats :**
    -   La base de données PostgreSQL est accessible depuis votre machine locale sur le port que vous avez défini dans le fichier `.env` (par exemple : `localhost:5432`).
    -   Les notebooks exécutés sont sauvegardés dans le dossier `notebooks/` avec le suffixe `.executed.ipynb`.

5.  **Pour arrêter les services :**
    -   Appuyez sur `Ctrl + C` dans le terminal, puis exécutez :
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