# Notes pour le Rapport de Projet - Prédicteur Électoral

## 1. Introduction
- **Objectif du projet :** Développer un modèle de Machine Learning capable de prédire le parti politique gagnant d'une élection par département en France.
- **Enjeu principal :** Mettre en place une méthodologie robuste pour traiter des données temporelles, en garantissant que le modèle soit évalué dans des conditions réalistes, similaires à une prédiction sur l'avenir.

## 2. Méthodologie et Pipeline de Données

### 2.1. Source et Agrégation des Données
- **Sources :** Les données proviennent de sources publiques variées (INSEE, Ministère de l'Intérieur) couvrant la période 2017-2024.
- **Caractéristiques :** Les données incluent des indicateurs socio-économiques (taux de chômage, pauvreté), sociaux (criminalité, immigration) et électoraux (résultats, participation).
- **Agrégation :** Toutes les données ont été nettoyées, harmonisées et consolidées au niveau départemental et annuel dans une table centrale `ELECTIONS_ALL` de la base de données SQLite.

### 2.2. Le Défi de la Fuite de Données Temporelles (Data Leakage)
- **Problème identifié :** Une première approche par division aléatoire des données a produit un score d'exactitude trompeur de ~71%. Ce score était artificiellement élevé car le modèle s'entraînait sur des données de 2022 et était testé sur d'autres données de la même année.
- **Solution implémentée :** Adoption d'une **division temporelle stricte**.
  - **Jeu d'entraînement (`train_df`) :** Contient uniquement les données des années **antérieures à 2024**.
  - **Jeu de test (`test_df`) :** Contient uniquement les données de l'année **2024**.
- **Impact :** Cette approche garantit que le modèle est évalué sur sa capacité à généraliser sur une année future qu'il n'a jamais vue, fournissant une mesure de performance honnête.

### 2.3. Prétraitement et Ingénierie des Caractéristiques
- **Nettoyage :** Gestion des valeurs manquantes par `forward-fill` pour la colonne `WINNER` afin de propager le dernier vainqueur connu.
- **Transformation :** Utilisation d'un `ColumnTransformer` de Scikit-learn pour appliquer des traitements spécifiques aux types de colonnes :
  - `StandardScaler` sur les caractéristiques numériques pour les normaliser.
  - `OneHotEncoder` sur les caractéristiques catégorielles (ex: `DEPARTMENT_CODE`) pour les transformer en format numérique.
- **Cible (Target) :** La colonne `WINNER` a été encodée en valeurs numériques à l'aide d'un `LabelEncoder`.
- **Sauvegarde des transformateurs :** Le `ColumnTransformer` (`preprocessor_X.joblib`) et le `LabelEncoder` (`label_encoder_y.joblib`) ont été sauvegardés pour être réutilisés à l'identique lors de la phase de prédiction.

### 2.4. Entraînement et Sélection du Modèle
- **Algorithmes testés :** Régression Logistique, Random Forest, Decision Tree, SVM.
- **Métrique d'évaluation :** L'**exactitude (accuracy)** a été choisie comme métrique principale, complétée par la **précision pondérée (weighted precision)** pour tenir compte du déséquilibre entre les partis.
- **Résultats :** Le modèle **Random Forest** a obtenu le meilleur score d'exactitude (~48%) sur le jeu de test de 2024.
- **Automatisation :** Le script d'entraînement a été conçu pour **identifier et sauvegarder automatiquement** le meilleur modèle, garantissant la reproductibilité et la robustesse du pipeline.

## 3. Génération des Prédictions et Interprétation

### 3.1. L'Hypothèse de la Simulation pour 2027
- **Principe :** Le modèle n'a pas conscience du temps (la colonne `YEAR` étant retirée). Pour prédire 2027, nous faisons l'hypothèse que les conditions socio-économiques seront similaires à celles de 2024.
- **Démarche :** Nous fournissons au modèle entraîné les données de 2024 et lui demandons de prédire le vainqueur. Le résultat est une simulation, pas une prophétie.

### 3.2. Interprétation du Score de Performance (~48%)
- **Validité :** Bien que inférieur au score initial trompeur, ce résultat est significativement **meilleur qu'un choix aléatoire** (qui serait de 25% avec 4 partis).
- **Signification :** Ce score représente la **performance réelle et fiable** de notre modèle face à des données futures inconnues. Il confirme que les caractéristiques socio-économiques choisies ont un pouvoir prédictif.

### 3.3. Création de la Table Finale pour l'Analyse BI
- **Objectif :** Faciliter la visualisation et la comparaison des tendances.
- **Action :** Un script (`generate_predictions.ipynb`) combine les résultats électoraux historiques (2017, 2022...) avec les prédictions générées pour l'année 2027.
- **Table de sortie :** `ELECTION_RESULTS_FOR_BI`. Cette table est la source de données unique et propre pour des outils comme Power BI ou Tableau, permettant de filtrer par année et de comparer le passé et le futur prédit.

## 4. Conclusion et Perspectives
- **Réalisation :** Le projet a abouti à la création d'un pipeline de machine learning de bout en bout, méthodologiquement sain, pour la prédiction de résultats électoraux. La mise en place de la division temporelle et l'automatisation de la sélection du modèle sont les points forts du projet.
- **Pistes d'amélioration futures :**
  - **Enrichir les données :** Intégrer des données plus granulaires (par circonscription), des données sur les sondages d'opinion, ou des indicateurs de sentiment sur les réseaux sociaux.
  - **Explorer d'autres modèles :** Tester des modèles plus complexes comme XGBoost ou des approches de deep learning.
  - **Projections démographiques :** Au lieu d'utiliser les données de 2024 comme proxy, rechercher et intégrer de véritables projections démographiques de l'INSEE pour 2027 afin d'améliorer la pertinence de la simulation.