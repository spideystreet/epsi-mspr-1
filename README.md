# Prédicteur de Résultats Électoraux

## Aperçu
Ce projet vise à prédire les résultats électoraux en utilisant des techniques d'apprentissage automatique. Il analyse les données électorales historiques pour identifier des modèles et prédire les vainqueurs dans les circonscriptions électorales.

## Structure du Projet
- `data/` : Contient les jeux de données électorales
  - `elections_prepared.csv` : Données électorales nettoyées et prétraitées
- `notebooks/` : Notebooks Jupyter pour l'exploration des données et le développement de modèles
  - `model_training.ipynb` : Développement et évaluation des modèles d'apprentissage automatique
- `models/` : Modèles entraînés sauvegardés
- `src/` : Code source de l'application
- `venv/` : Environnement virtuel (non suivi dans git)

## Fonctionnalités
- Exploration des données et visualisation des tendances électorales
- Ingénierie des caractéristiques à partir de données démographiques et historiques de vote
- Modèles d'apprentissage automatique pour prédire les résultats électoraux
- Métriques d'évaluation de performance

## Installation

### Prérequis
- Python 3.13+
- pip

### Configuration
1. Cloner ce dépôt :
   ```bash
   git clone [repository-url]
   ```

2. Naviguer vers le répertoire du projet :
   ```bash
   cd election-result-predictor
   ```

3. Créer et activer un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   ```

4. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation
1. Assurez-vous que votre environnement est correctement configuré
2. Ouvrez et exécutez les notebooks Jupyter :
   ```bash
   jupyter notebook
   ```
3. Naviguez vers le répertoire `notebooks` pour commencer à explorer les données et les modèles

## Modèles
Le projet explore plusieurs algorithmes d'apprentissage automatique, notamment :
- Random Forest Classifier (Forêts aléatoires)
- Gradient Boosting Classifier (Boosting par gradient)
- Logistic Regression (Régression logistique)
- Support Vector Machines (Machines à vecteurs de support)
- K-Nearest Neighbors (K plus proches voisins)
- Decision Trees (Arbres de décision)

## Données
Le jeu de données contient des informations électorales avec des caractéristiques telles que :
- Code et nom du département
- Nombre d'électeurs inscrits
- Participation électorale
- Répartition des votes entre différents partis politiques
- Vainqueurs historiques

## Licence
Ce projet est sous licence selon les termes inclus dans le fichier LICENSE.

## Contributeurs
- @spideystreet