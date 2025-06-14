# 🗳️ Prédicteur de Résultats Électoraux

## ✨ Aperçu
Ce projet a pour but de prédire les résultats des élections françaises par département en utilisant des techniques de machine learning. L'objectif n'est pas seulement de prédire, mais de construire un **pipeline robuste et méthodologiquement correct** qui évite les pièges courants de l'analyse de données temporelles.

##  핵심 La Démarche Clé du Projet
Le défi principal de ce projet est de prédire un événement futur (une élection) en se basant sur des données passées. Pour cela, notre démarche repose sur trois piliers :

1.  **Division Temporelle Stricte :** Pour éviter toute "fuite de données" du futur vers le passé, nous entraînons nos modèles exclusivement sur les données **antérieures à 2024** et nous les évaluons sur les données de **2024**.
2.  **Score d'Exactitude Honnête :** Le score de performance de notre modèle (~48%) peut sembler modeste, mais il est **réaliste**. Il représente la véritable capacité du modèle à prédire une année qu'il n'a jamais vue, ce qui est bien plus fiable qu'un score artificiellement élevé.
3.  **Simulation pour 2027 :** Nous ne prétendons pas "prédire l'avenir". Nous utilisons nos données les plus récentes (2024) comme une estimation des conditions socio-économiques de 2027, et nous demandons au modèle : *"selon les tendances apprises, qui gagnerait si une élection avait lieu dans ces conditions ?"*.

## 🚀 Notre Pipeline de Travail
Le projet est structuré en 3 notebooks séquentiels qui forment un pipeline complet, de la donnée brute au résultat final.

1.  `notebooks/data_preprocessing.ipynb`
    *   **Rôle :** Préparer et nettoyer les données.
    *   **Actions :** Agréger les données brutes, appliquer la division temporelle (train < 2024, test = 2024), et sauvegarder les jeux de données traités ainsi que les outils de transformation (`preprocessor`).

2.  `notebooks/model_training.ipynb`
    *   **Rôle :** Entraîner et sélectionner le meilleur modèle.
    *   **Actions :** Tester plusieurs algorithmes (Random Forest, etc.), les évaluer sur le jeu de test de 2024, et **sauvegarder automatiquement le modèle le plus performant**.

3.  `notebooks/generate_predictions.ipynb`
    *   **Rôle :** Générer les prédictions finales et préparer les données pour la BI.
    *   **Actions :** Charger le meilleur modèle, prédire les gagnants de "2027", et créer une table finale `ELECTION_RESULTS_FOR_BI` dans la base de données, combinant tous les résultats historiques et futurs pour une analyse facile.

## 📂 Structure des Fichiers
```
.
├── data/                 # Jeux de données bruts (.csv)
├── database/
│   ├── ELECTIONS.db        # Base de données SQLite centrale
│   ├── preprocessor_X.joblib # Outil de transformation sauvegardé
│   └── label_encoder_y.joblib  # Encodeur de la cible sauvegardé
├── models/
│   └── random_forest_predictor.joblib # Meilleur modèle de prédiction
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── generate_predictions.ipynb
├── project/
│   └── notes.md            # Notes détaillées pour le rapport
├── README.md               # Ce fichier
└── requirements.txt        # Dépendances du projet
```

## 📊 Données Utilisées
Notre jeu de données comprend :
- Résultats électoraux historiques (participation, inscrits, votes par parti).
- Indicateurs socio-économiques (chômage, pauvreté).
- Données sociales (criminalité, immigration).

## 🛠️ Installation et Utilisation

### Prérequis
- Python 3.10+
- pip

### Lancement
1. Clonez le dépôt et naviguez dans le dossier.
2. Créez et activez un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Lancez Jupyter et suivez les notebooks dans l'ordre du pipeline :
   ```bash
   jupyter notebook
   ```

## 📄 Licence
Ce projet est sous licence selon les termes du fichier LICENSE.

## 👥 L'Équipe
- [@hicham](https://github.com/spideystreet)
- [@amine](https://github.com/testt753)
- [@wassim](https://github.com/Wassim38)

## 💬 Feedback
Vous avez des suggestions ou des questions ? N'hésitez pas à ouvrir une issue ou à nous contacter directement !

- on a un .env.example 