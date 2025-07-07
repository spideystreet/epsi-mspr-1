# Prédiction des Résultats Électoraux par Département : Pipeline de Machine Learning et Tableau de Bord Interactif

**Projet MSPR - TPRE813**  
**Master 1 EISI - EPSI Grenoble**  
**Année académique 2024-2025**

---

**Auteurs :**
- HICHAM [@spideystreet](https://github.com/spideystreet)
- AMINE [@testt753](https://github.com/testt753)  
- WASSIM [@Wassim38](https://github.com/Wassim38)

**Encadrement :** [Mohamed Mechri]  
**Date de soutenance :** [11 Juillet 2025]

---

## Table des Matières

1. [Résumé Exécutif](#1-résumé-exécutif)
2. [Introduction et Contexte](#2-introduction-et-contexte)
3. [Revue de Littérature](#3-revue-de-littérature)
4. [Méthodologie](#4-méthodologie)
5. [Architecture Technique](#5-architecture-technique)
6. [Collecte et Préparation des Données](#6-collecte-et-préparation-des-données)
7. [Modélisation et Machine Learning](#7-modélisation-et-machine-learning)
8. [Résultats et Évaluation](#8-résultats-et-évaluation)
9. [Interface Utilisateur et Visualisation](#9-interface-utilisateur-et-visualisation)
10. [Déploiement et Infrastructure](#10-déploiement-et-infrastructure)
11. [Discussion et Limites](#11-discussion-et-limites)
12. [Conclusion et Perspectives](#12-conclusion-et-perspectives)
13. [Références](#13-références)
14. [Annexes](#14-annexes)

---

## 1. Résumé Exécutif

### 1.1 Objectifs du Projet
Ce projet vise à développer un système de prédiction des résultats électoraux français par département, en s'appuyant sur des techniques de machine learning et des données socio-économiques. L'objectif principal est de construire un pipeline de données robuste et reproductible alimentant un tableau de bord interactif pour la visualisation des résultats historiques et des prédictions futures.

### 1.2 Approche Méthodologique
Notre approche repose sur trois piliers fondamentaux :
- **Pipeline de données automatisé** : Traitement séquentiel via Jupyter notebooks
- **Modélisation prédictive** : Utilisation d'algorithmes de machine learning supervisé
- **Interface de visualisation** : Tableau de bord interactif développé avec Streamlit

### 1.3 Résultats Principaux
- Développement d'un pipeline complet de traitement des données électorales
- Création d'un modèle prédictif Random Forest avec une précision de **48,94%** sur les données de test 2024
- Déploiement d'une interface web interactive permettant la visualisation des prédictions pour 2027
- Génération de **94 prédictions départementales** pour l'année 2027

```mermaid
graph TD
    A["🏛️ Government APIs<br/>data.gouv.fr"] --> B["📊 Raw Data Collection<br/>Elections, Crime, Employment, Immigration"]
    B --> C["🔧 Dataiku Preprocessing<br/>Cleaning & Normalization"]
    C --> D["🐳 Docker Environment<br/>PostgreSQL + Python"]
    
    D --> E["📓 Notebook 1<br/>data_preprocessing.ipynb"]
    E --> F["🗄️ PostgreSQL Database<br/>Structured Tables + Views"]
    
    F --> G["📓 Notebook 2<br/>model_training.ipynb"]
    G --> H["🤖 ML Models<br/>Random Forest, GB, LR"]
    H --> I["💾 Best Model<br/>Joblib Persistence"]
    
    I --> J["📓 Notebook 3<br/>prediction.ipynb"]
    J --> K["🔮 2027 Predictions<br/>election_results_for_bi"]
    
    K --> L["🌐 Streamlit Dashboard<br/>Interactive Visualization"]
    L --> M["👤 End User<br/>Electoral Analysis"]
    
    style A fill:#e1f5fe
    style L fill:#f3e5f5
    style M fill:#e8f5e8
```

---

## 2. Introduction et Contexte

### 2.1 Problématique
L'analyse et la prédiction des comportements électoraux constituent un enjeu majeur pour la compréhension des dynamiques politiques contemporaines. Dans un contexte où les données ouvertes gouvernementales françaises offrent une richesse d'informations inédite, il devient possible de développer des modèles prédictifs sophistiqués combinant variables électorales et indicateurs socio-économiques.

### 2.2 Enjeux Techniques et Scientifiques
Ce projet s'inscrit dans la convergence de plusieurs domaines :
- **Science des données** : Extraction, transformation et analyse de grandes quantités de données
- **Machine Learning** : Application d'algorithmes prédictifs à des données temporelles
- **Ingénierie logicielle** : Développement d'un pipeline reproductible et scalable
- **Visualisation de données** : Création d'interfaces intuitives pour l'exploration des résultats

### 2.3 Objectifs Académiques
Dans le cadre du Master EISI à EPSI Grenoble, ce projet permet de démontrer :
- La maîtrise des technologies de containerisation (Docker)
- L'application pratique des techniques de machine learning
- Le développement d'applications web interactives
- La gestion de projets informatiques complexes

```mermaid
graph LR
    subgraph "Data Sources"
        A1["Elections Data<br/>2017-2024"]
        A2["Crime Statistics<br/>Victims Count"]
        A3["Employment Data<br/>Unemployment Rate"]
        A4["Immigration Data<br/>Immigration Rate"]
        A5["Poverty Data<br/>Poverty Rate"]
    end
    
    subgraph "Database Layer"
        B1["election_data"]
        B2["crime_data"]
        B3["unemployment_data"]
        B4["immigration_data"]
        B5["poverty_data"]
        B6["elections_all VIEW"]
    end
    
    subgraph "ML Pipeline"
        C1["Feature Engineering<br/>StandardScaler + OneHot"]
        C2["Train/Test Split<br/>2017-2023 / 2024"]
        C3["Model Training<br/>Random Forest"]
        C4["Model Evaluation<br/>F1-Score, Accuracy"]
    end
    
    subgraph "Prediction & Viz"
        D1["2027 Predictions"]
        D2["Interactive Map"]
        D3["Statistical Dashboard"]
    end
    
    A1 --> B1
    A2 --> B2
    A3 --> B3
    A4 --> B4
    A5 --> B5
    
    B1 --> B6
    B2 --> B6
    B3 --> B6
    B4 --> B6
    B5 --> B6
    
    B6 --> C1
    C1 --> C2
    C2 --> C3
    C3 --> C4
    
    C3 --> D1
    D1 --> D2
    D1 --> D3
    
    style B6 fill:#fff2cc
    style C3 fill:#d5e8d4
    style D1 fill:#f8cecc
```

---

## 3. Revue de Littérature

### 3.1 Prédiction Électorale et Machine Learning
Les travaux académiques récents montrent l'efficacité des approches de machine learning pour la prédiction électorale. Silver (2016) démontre l'importance de la combinaison de multiples sources de données, tandis que Wang et al. (2018) explorent l'utilisation des algorithmes d'ensemble pour améliorer la précision prédictive.

### 3.2 Variables Socio-économiques et Comportement Électoral
La littérature établit des corrélations significatives entre indicateurs socio-économiques et choix électoraux :
- **Chômage** : Impact direct sur les votes protestataires (Hernández & Kriesi, 2016)
- **Immigration** : Influence sur les votes d'extrême droite (Lubbers & Scheepers, 2017)
- **Criminalité** : Corrélation avec les préoccupations sécuritaires (Green & McFarlane, 2016)

### 3.3 Technologies de Pipeline de Données
L'émergence des pratiques MLOps (Machine Learning Operations) souligne l'importance des pipelines automatisés pour la reproductibilité des modèles (Sculley et al., 2015).

---

## 4. Méthodologie

### 4.1 Approche Générale
Notre méthodologie suit le cycle de vie standard des projets de data science, adapté aux spécificités de la prédiction électorale :

1. **Définition du problème** : Prédiction binaire/multiclasse des partis gagnants
2. **Collecte des données** : Agrégation de sources gouvernementales françaises
3. **Exploration et préparation** : Nettoyage et ingénierie des features
4. **Modélisation** : Entraînement et sélection d'algorithmes
5. **Évaluation** : Validation sur données de test temporelles
6. **Déploiement** : Interface utilisateur et visualisation

```mermaid
graph TD
    A["📥 Data Collection<br/>Government APIs"] --> B["🔧 Data Preprocessing<br/>Dataiku Platform"]
    B --> C["🧹 Data Cleaning<br/>Missing Values, Outliers"]
    C --> D["🔄 Data Integration<br/>PostgreSQL Database"]
    D --> E["⚙️ Feature Engineering<br/>Encoding, Scaling"]
    E --> F["📊 Exploratory Analysis<br/>Statistics, Distributions"]
    F --> G["🤖 Model Training<br/>Multiple Algorithms"]
    G --> H["📈 Model Evaluation<br/>Validation Metrics"]
    H --> I{"Best Model?"}
    I -->|No| G
    I -->|Yes| J["💾 Model Persistence<br/>Joblib Storage"]
    J --> K["🔮 Future Predictions<br/>2027 Electoral Map"]
    K --> L["🌐 Dashboard Development<br/>Streamlit Interface"]
    L --> M["🚀 Deployment<br/>Docker Containers"]
    M --> N["✅ Final Validation<br/>User Testing"]
    
    style A fill:#e1f5fe
    style G fill:#f3e5f5
    style J fill:#e8f5e8
    style L fill:#fff3e0
```

### 4.2 Division Temporelle
Approche de validation temporelle rigoureuse :
- **Données d'entraînement** : 2017-2023 (652 échantillons)
- **Données de test** : 2024 (94 échantillons)
- **Prédictions** : 2027 (projection future)

### 4.3 Critères d'Évaluation
- **Précision globale** : Pourcentage de prédictions correctes
- **F1-Score** : Mesure équilibrée pour classes déséquilibrées
- **Matrice de confusion** : Analyse détaillée des erreurs par parti

---

## 5. Architecture Technique

### 5.1 Vue d'Ensemble de l'Architecture
L'architecture du système repose sur une approche modulaire et containerisée, garantissant la reproductibilité et la scalabilité.

```mermaid
graph TB
    subgraph "Container: PostgreSQL DB"
        DB["🗄️ PostgreSQL 13<br/>Port: 5432<br/>Data Persistence"]
    end
    
    subgraph "Container: Python Application"
        APP["🐍 Python 3.11<br/>Jupyter + ML Libraries<br/>Pipeline Execution"]
    end
    
    subgraph "Host System"
        DASHBOARD["🌐 Streamlit Dashboard<br/>Port: 8501<br/>Interactive UI"]
        USER["👤 User Browser<br/>http://localhost:8501"]
    end
    
    subgraph "Data Flow"
        CSV["📄 CSV Files<br/>/data directory"]
        MODELS["🤖 Trained Models<br/>/models directory"]
        ARTIFACTS["💾 ML Artifacts<br/>/database directory"]
    end
    
    APP --> DB
    DB --> APP
    CSV --> APP
    APP --> MODELS
    APP --> ARTIFACTS
    
    DB --> DASHBOARD
    MODELS --> DASHBOARD
    DASHBOARD --> USER
    
    style DB fill:#e3f2fd
    style APP fill:#f3e5f5
    style DASHBOARD fill:#e8f5e8
    style USER fill:#fff3e0
```

### 5.2 Composants Principaux

#### 5.2.1 Pipeline de Données
- **Notebooks Jupyter** : Traitement séquentiel automatisé
- **PostgreSQL** : Base de données relationnelle pour stockage structuré
- **Docker Compose** : Orchestration des services

#### 5.2.2 Stack Technologique
```
Backend:
├── Python 3.11
├── PostgreSQL 13
├── Jupyter
├── Scikit-learn
├── Pandas/NumPy
└── SQLAlchemy

Frontend:
├── Streamlit
├── Plotly
├── Folium (cartes interactives)
└── Bootstrap (styling)

Infrastructure:
├── Docker & Docker Compose
├── Git (versioning)
└── Joblib (persistance modèles)
```

### 5.3 Flux de Données
Le flux de données suit une architecture ETL (Extract, Transform, Load) rigoureuse :

1. **Extraction** : APIs gouvernementales → Fichiers CSV locaux
2. **Transformation** : Notebooks Jupyter → Données nettoyées
3. **Chargement** : PostgreSQL → Tables relationnelles
4. **Modélisation** : Scikit-learn → Modèles persistés
5. **Visualisation** : Streamlit → Interface utilisateur

```mermaid
graph LR
    subgraph "Input Features"
        F1["Department Code<br/>01, 02, 03..."]
        F2["Year<br/>2017-2024"]
        F3["Unemployment Rate<br/>%"]
        F4["Crime Victims<br/>Count"]
        F5["Immigration Rate<br/>%"]
        F6["Poverty Rate<br/>%"]
    end
    
    subgraph "Preprocessing"
        P1["OneHot Encoder<br/>Categorical"]
        P2["Standard Scaler<br/>Numerical"]
    end
    
    subgraph "Random Forest Model"
        RF["🌲 Random Forest<br/>n_estimators=100<br/>max_depth=10"]
    end
    
    subgraph "Output"
        O1["Winning Party<br/>RN, LR, PS, LFI, Others"]
        O2["Probability Scores<br/>Confidence Levels"]
    end
    
    F1 --> P1
    F2 --> P1
    F3 --> P2
    F4 --> P2
    F5 --> P2
    F6 --> P2
    
    P1 --> RF
    P2 --> RF
    
    RF --> O1
    RF --> O2
    
    style RF fill:#d5e8d4
    style O1 fill:#f8cecc
```

---

## 6. Collecte et Préparation des Données

### 6.1 Sources de Données

Notre jeu de données combine plusieurs sources officielles françaises :

#### 6.1.1 Données Électorales
- **Source** : [data.gouv.fr - Données des élections](https://www.data.gouv.fr/fr/pages/donnees-des-elections/)
- **Période** : 2017-2024
- **Variables** : Nombre d'inscrits, votants, résultats par parti
- **Granularité** : Départementale

#### 6.1.2 Données Socio-économiques
- **Emploi** : [data.gouv.fr - Données emploi](https://www.data.gouv.fr/fr/pages/donnees-emploi/)
- **Sécurité** : [data.gouv.fr - Données sécurité](https://www.data.gouv.fr/fr/pages/donnees-securite/)
- **Démographie** : [INSEE](https://www.data.gouv.fr/fr/organizations/institut-national-de-la-statistique-et-des-etudeseconomiques-insee/)

### 6.2 Prétraitement avec Dataiku
Phase initiale de nettoyage réalisée sur la plateforme Dataiku :
- **Normalisation** des formats de dates
- **Harmonisation** des codes départementaux
- **Détection et traitement** des valeurs aberrantes
- **Standardisation** des noms de colonnes

![Processus de Prétraitement](../assets/images/dataiku_pipeline_real.png)

### 6.3 Pipeline de Traitement Automatisé

#### 6.3.1 Notebook 1 : data_preprocessing.ipynb
```python
# Chargement et intégration des données
TABLE_CONFIG = {
    "unemployment_data": {...},
    "crime_data": {...},
    "election_data": {...},
    "immigration_data": {...},
    "poverty_data": {...}
}

# Création de la vue unifiée
CREATE VIEW elections_all AS
SELECT ed."YEAR", ed."DEPARTMENT_CODE", ed."WINNER",
       cd."NUMBER_OF_VICTIMS", id."IMMIGRATION_RATE",
       pd."POVERTY_RATE", ud."UNEMPLOYMENT_RATE"
FROM election_data ed
LEFT JOIN crime_data cd ON ...
```

#### 6.3.2 Gestion des Valeurs Manquantes
Stratégie d'imputation progressive :
- **Forward Fill** par département pour continuité temporelle
- **Suppression** des lignes sans variable cible
- **Validation** de l'intégrité finale (0 valeurs nulles détectées)

### 6.4 Résultats du Prétraitement

| Statistique | Valeur |
|-------------|--------|
| **Échantillons totaux** | 752 lignes |
| **Échantillons d'entraînement** | 652 lignes (2017-2023) |
| **Échantillons de test** | 94 lignes (2024) |
| **Features numériques** | 4 (taux chômage, immigration, pauvreté, victimes) |
| **Features catégorielles** | 1 (code département) |
| **Valeurs manquantes** | 0 (après imputation) |

---

## 7. Modélisation et Machine Learning

### 7.1 Préparation des Features

#### 7.1.1 Encodage des Variables
```python
# Configuration du préprocesseur
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_features),
    ('cat', OneHotEncoder(), categorical_features)
])

# Encodage de la variable cible
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y_train)
```

#### 7.1.2 Variables Explicatives
- **Variables numériques** : Taux de chômage, immigration, pauvreté, nombre de victimes
- **Variables catégorielles** : Code département (OneHot encodé en 95 features)
- **Variable cible** : Parti gagnant (5 classes : DROITE, PS, RN, LFI, GAUCHE)

### 7.2 Algorithmes Testés et Performances

#### 7.2.1 Comparaison des Modèles
Quatre algorithmes ont été entraînés et évalués :

| Modèle | Accuracy | Weighted Precision | Rang |
|--------|----------|-------------------|------|
| **Random Forest** | **48.94%** | **66.34%** | 🥇 |
| Decision Tree | 44.68% | 60.25% | 🥈 |
| Logistic Regression | 29.79% | 62.13% | 🥉 |
| SVM | 23.40% | 62.98% | 4 |

#### 7.2.2 Modèle Sélectionné : Random Forest
```python
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

**Avantages du Random Forest** :
- **Meilleure performance** : 48.94% d'accuracy
- **Robustesse aux outliers**
- **Gestion native des variables mixtes**
- **Interprétabilité** via importance des features

### 7.3 Entraînement et Validation

#### 7.3.1 Protocole d'Évaluation
- **Validation temporelle** : Train sur 2017-2023, test sur 2024
- **Métriques** : Accuracy, Weighted Precision
- **Persistance** : Sauvegarde du meilleur modèle en `random_forest_predictor.joblib`

#### 7.3.2 Architecture des Features
Après preprocessing, le modèle utilise **99 features** :
- 4 features numériques standardisées
- 95 features catégorielles (OneHot encoding des départements)

![Comparaison des Modèles](../assets/images/model_comparison_chart.png)

---

## 8. Résultats et Évaluation

### 8.1 Performance du Modèle Random Forest

#### 8.1.1 Métriques Globales
- **Précision globale** : **48.94%** sur le jeu de test 2024
- **Weighted Precision** : **66.34%**
- **Nombre de prédictions correctes** : 46/94 départements

#### 8.1.2 Analyse de Performance
Le modèle Random Forest montre des performances modérées mais cohérentes :
- **Supériorité claire** par rapport aux autres algorithmes testés
- **Robustesse** face à la complexité des données électorales
- **Capacité de généralisation** sur données temporelles futures

### 8.2 Prédictions 2027

#### 8.2.1 Génération des Prédictions
- **Base de données** : Utilisation des données 2024 comme référence
- **Prédictions générées** : 94 départements français
- **Consolidation** : 375 lignes totales (historique + prédictions)

#### 8.2.2 Pipeline de Prédiction
```python
# Preprocessing des données 2024 pour prédiction 2027
X_processed = preprocessor_X.transform(features_to_predict)
predictions_encoded = model.predict(X_processed)
predictions_decoded = label_encoder_y.inverse_transform(predictions_encoded)
```

#### 8.2.3 Intégration Business Intelligence
- **Vue consolidée** : `election_data_for_bi` créée dans PostgreSQL
- **Données historiques** : 281 lignes (2017-2024)
- **Prédictions futures** : 94 lignes (2027)
- **Période totale** : 2017-2027 (11 années)

![Prédictions 2027 Map](../assets/images/predictions_2027_map.png)

### 8.3 Analyse des Limites

#### 8.3.1 Performance Modérée
L'accuracy de 48.94% s'explique par :
- **Complexité intrinsèque** des phénomènes électoraux
- **Variables manquantes** (réseaux sociaux, événements conjoncturels)
- **Simplification** des dynamiques politiques locales

#### 8.3.2 Points d'Amélioration Identifiés
- **Enrichissement des données** : Intégration de nouvelles sources
- **Feature engineering** : Création de variables composites
- **Ensemble methods** : Combinaison de plusieurs modèles

---

## 9. Interface Utilisateur et Visualisation

### 9.1 Architecture du Dashboard Streamlit

Le tableau de bord interactif offre une exploration intuitive des données et prédictions :

```python
# Structure principale du dashboard
def main():
    st.title("🗳️ Prédicteur Electoral France")
    
    # Sidebar pour filtres
    year_filter = st.sidebar.selectbox("Année", options)
    
    # Visualisations principales
    display_map(filtered_data)
    display_statistics(filtered_data)
    display_predictions(model_results)
```

### 9.2 Fonctionnalités Principales

#### 9.2.1 Carte Interactive
- **Technologie** : Folium + Streamlit
- **Features** :
  - Visualisation par département
  - Code couleur par parti gagnant
  - Tooltips avec données détaillées
  - Zoom et navigation interactifs

#### 9.2.2 Filtres Temporels
- **Années historiques** : 2017-2024
- **Prédictions** : 2027
- **Comparaisons** : Évolution temporelle

#### 9.2.3 Statistiques Agrégées
- **Graphiques en barres** : Répartition nationale
- **Tableaux détaillés** : Données par département
- **Métriques clés** : Participation, margins

![Interface Dashboard](../assets/images/dashboard_main_interface.png)

### 9.3 Experience Utilisateur

#### 9.3.1 Design Responsif
- **Layout adaptatif** : Desktop et mobile
- **Thème moderne** : Bootstrap styling
- **Navigation intuitive** : Menu latéral

#### 9.3.2 Performance
- **Chargement optimisé** : Cache Streamlit
- **Requêtes efficaces** : Indexation PostgreSQL
- **Mise à jour temps réel** : Connexion directe DB

---

## 10. Déploiement et Infrastructure

### 10.1 Containerisation Docker

#### 10.1.1 Architecture Multi-Conteneurs
```yaml
# docker-compose.yml
services:
  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=${PG_USER}
      - POSTGRES_PASSWORD=${PG_PASSWORD}
  
  app:
    build: .
    depends_on:
      - db
    volumes:
      - .:/app
```

#### 10.1.2 Pipeline d'Exécution
```bash
#!/bin/bash
# run_project.sh

echo "STEP 1: Data Preprocessing..."
jupyter nbconvert --execute notebooks/data_preprocessing.ipynb

echo "STEP 2: Model Training..."
jupyter nbconvert --execute notebooks/model_training.ipynb

echo "STEP 3: Predictions..."
jupyter nbconvert --execute notebooks/prediction.ipynb
```

### 10.2 Reproductibilité

#### 10.2.1 Gestion des Dépendances
```txt
# requirements.txt
streamlit==1.28.0
pandas==2.0.3
scikit-learn==1.3.0
psycopg2-binary==2.9.7
folium==0.14.0
plotly==5.15.0
```

#### 10.2.2 Variables d'Environnement
```env
# .env
PG_USER=postgres
PG_PASSWORD=secure_password
PG_HOST=localhost
PG_PORT=5432
PG_DBNAME=elections
```

### 10.3 Déploiement Production

#### 10.3.1 Options de Déploiement
- **Local** : Docker Compose (développement)
- **Cloud** : Streamlit Cloud, Heroku, Railway
- **Enterprise** : Kubernetes, AWS ECS

#### 10.3.2 Monitoring et Maintenance
- **Logs** : Centralisés via Docker
- **Backup** : PostgreSQL dump automatique
- **Updates** : Pipeline CI/CD potentiel

```mermaid
graph TB
    subgraph "🏠 Local Development Environment"
        subgraph "📱 User Interface"
            BROWSER["🌐 Web Browser<br/>http://localhost:8501"]
            USER["👤 Data Scientist / Analyst"]
        end
        
        subgraph "🐳 Docker Compose Services"
            direction TB
            DB_CONTAINER["🗄️ PostgreSQL Container<br/>postgres:13<br/>Port: 5432<br/>Volume: db_data"]
            APP_CONTAINER["🐍 Python App Container<br/>Python 3.11 + Jupyter<br/>Notebooks Execution"]
        end
        
        subgraph "📁 Local File System"
            DATA_FILES["📄 CSV Data Files<br/>/data/"]
            MODELS["🤖 ML Models<br/>/models/"]
            ARTIFACTS["💾 Preprocessors<br/>/database/"]
            NOTEBOOKS["📓 Jupyter Notebooks<br/>/notebooks/"]
        end
        
        subgraph "🚀 Streamlit Application"
            STREAMLIT["🌟 Streamlit Dashboard<br/>Port: 8501<br/>Interactive UI"]
        end
    end
    
    subgraph "☁️ Production Options"
        CLOUD_OPTIONS["🌐 Cloud Deployment<br/>• Streamlit Cloud<br/>• Heroku<br/>• Railway<br/>• AWS ECS"]
    end
    
    %% User interactions
    USER --> BROWSER
    BROWSER --> STREAMLIT
    
    %% Docker internal communications
    APP_CONTAINER <--> DB_CONTAINER
    APP_CONTAINER --> DATA_FILES
    APP_CONTAINER --> MODELS
    APP_CONTAINER --> ARTIFACTS
    APP_CONTAINER --> NOTEBOOKS
    
    %% Streamlit connections
    STREAMLIT --> DB_CONTAINER
    STREAMLIT --> MODELS
    STREAMLIT --> DATA_FILES
    
    %% Deployment path
    STREAMLIT -.-> CLOUD_OPTIONS
    
    style DB_CONTAINER fill:#e3f2fd
    style APP_CONTAINER fill:#f3e5f5
    style STREAMLIT fill:#e8f5e8
    style BROWSER fill:#fff3e0
    style USER fill:#f0f4c3
    style CLOUD_OPTIONS fill:#fce4ec
```

---

## 11. Discussion et Limites

### 11.1 Forces du Projet

#### 11.1.1 Reproductibilité
- **Pipeline automatisé** : Notebooks séquentiels
- **Containerisation** : Environnement isolé
- **Documentation** : Code commenté et structuré

#### 11.1.2 Scalabilité
- **Architecture modulaire** : Composants indépendants
- **Base de données** : PostgreSQL performant
- **Interface web** : Streamlit responsive

### 11.2 Limitations Identifiées

#### 11.2.1 Données
- **Granularité temporelle** : Données annuelles uniquement
- **Variables manquantes** : Certains indicateurs sociaux indisponibles
- **Biais géographique** : Surreprésentation de certaines régions

#### 11.2.2 Modélisation
- **Performance modérée** : 48.94% d'accuracy
- **Complexité électorale** : Réduction à des variables quantitatives
- **Événements exceptionnels** : Difficile à prédire (crises, scandales)
- **Dynamiques locales** : Variables non capturées

#### 11.2.3 Techniques
- **Validation temporelle** : Un seul point de test (2024)
- **Features engineering** : Potentiel d'amélioration
- **Ensembling** : Combinaison de modèles non explorée

### 11.3 Biais et Considérations Éthiques

#### 11.3.1 Biais de Sélection
- **Sources de données** : Limitées aux données publiques
- **Période d'étude** : 2017-2024, évolutions récentes

#### 11.3.2 Implications Éthiques
- **Influence démocratique** : Risque de prophétie auto-réalisatrice
- **Transparence** : Nécessité d'explicabilité des prédictions
- **Usage responsable** : Cadre d'utilisation défini

---

## 12. Conclusion et Perspectives

### 12.1 Synthèse des Réalisations

Ce projet a permis de développer avec succès un système complet de prédiction électorale, démontrant :

#### 12.1.1 Objectifs Atteints
- ✅ **Pipeline automatisé** : Traitement de bout en bout des données
- ✅ **Modèle prédictif** : Précision de 48.94% sur données 2024
- ✅ **Interface utilisateur** : Dashboard interactif fonctionnel
- ✅ **Infrastructure** : Déploiement containerisé reproductible
- ✅ **Prédictions 2027** : 94 prédictions départementales générées

#### 12.1.2 Compétences Développées
- **Data Engineering** : ETL, bases de données, APIs
- **Machine Learning** : Preprocessing, modeling, evaluation
- **DevOps** : Docker, containerisation, orchestration
- **Full-Stack Development** : Backend Python, Frontend Streamlit

### 12.2 Perspectives d'Amélioration

#### 12.2.1 Court Terme
- **Optimisation modèle** : Hyperparameter tuning pour améliorer les 48.94%
- **Enrichissement des données** : Réseaux sociaux, sondages
- **Interface utilisateur** : UX améliorée, nouvelles visualisations

#### 12.2.2 Moyen Terme
- **Temps réel** : Intégration de données dynamiques
- **Multi-échelle** : Prédictions communales et régionales
- **API REST** : Service de prédiction externalisé

#### 12.2.3 Long Terme
- **Deep Learning** : Réseaux de neurones pour patterns complexes
- **NLP** : Analyse de sentiment des discours politiques
- **Systèmes multi-agents** : Modélisation des interactions électorales

### 12.3 Impact Académique et Professionnel

#### 12.3.1 Contribution Académique
- **Méthodologie reproductible** : Open source disponible
- **Cas d'étude** : Pipeline MLOps complet
- **Documentation** : Ressource pédagogique

#### 12.3.2 Préparation Professionnelle
- **Portfolio technique** : Démonstration de compétences
- **Expérience projet** : Gestion complète de A à Z
- **Technologies actuelles** : Stack moderne et demandée

---

## 13. Licence et Propriété Intellectuelle

### 13.1 Licence MIT
Ce projet est distribué sous licence MIT, garantissant une utilisation libre et ouverte :

```
MIT License

Copyright (c) 2024 HICHAM, AMINE, WASSIM - EPSI Grenoble

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 13.2 Avantages de la Licence MIT
- **Liberté d'utilisation** : Utilisation libre pour projets commerciaux et non-commerciaux
- **Modification autorisée** : Adaptation et personnalisation du code
- **Distribution libre** : Partage sans restriction
- **Transparence** : Code source ouvert et auditable

### 13.3 Contributions Open Source
- **Repository GitHub** : Code source accessible publiquement
- **Documentation complète** : Facilite la réutilisation et l'apprentissage
- **Reproductibilité** : Pipeline entièrement documenté et containerisé
- **Impact pédagogique** : Ressource pour la communauté académique

### 13.4 Protection et Attribution
- **Attribution requise** : Mention des auteurs originaux obligatoire
- **Disclaimer** : Limitation de responsabilité clairement établie
- **Copyright** : Droits d'auteur préservés pour les auteurs originaux

---

## 14. Références

### Articles Académiques

1. Silver, N. (2016). *The Signal and the Noise: Why So Many Predictions Fail—But Some Don't*. Penguin Books.

2. Wang, W., Rothschild, D., Goel, S., & Gelman, A. (2018). Forecasting elections with non-representative polls. *International Journal of Forecasting*, 34(2), 183-194.

3. Hernández, E., & Kriesi, H. (2016). The electoral consequences of the financial and economic crisis in Europe. *European Journal of Political Research*, 55(2), 203-224.

4. Lubbers, M., & Scheepers, P. (2017). Explaining the growth of the radical right in Western Europe. *European Journal of Political Research*, 56(2), 365-390.

5. Sculley, D., et al. (2015). Hidden technical debt in machine learning systems. *Advances in Neural Information Processing Systems*, 28.

### Sources de Données

6. Data.gouv.fr. (2024). *Données des élections*. Retrieved from https://www.data.gouv.fr/fr/pages/donnees-des-elections/

7. Data.gouv.fr. (2024). *Données sécurité*. Retrieved from https://www.data.gouv.fr/fr/pages/donnees-securite/

8. Data.gouv.fr. (2024). *Données emploi*. Retrieved from https://www.data.gouv.fr/fr/pages/donnees-emploi/

9. INSEE. (2024). *Institut National de la Statistique*. Retrieved from https://www.data.gouv.fr/fr/organizations/institut-national-de-la-statistique-et-des-etudeseconomiques-insee/

### Documentation Technique

10. Streamlit Documentation. (2024). *Building Data Apps*. Retrieved from https://docs.streamlit.io/

11. Scikit-learn Documentation. (2024). *Machine Learning in Python*. Retrieved from https://scikit-learn.org/

12. Docker Documentation. (2024). *Containerization Platform*. Retrieved from https://docs.docker.com/

---

## 15. Annexes

### Annexe A : Configuration Technique

#### A.1 Structure Complète du Projet
```
epsi-mspr-1/
├── assets/
│   └── images/
├── data/
│   ├── 2017_2024_CHOMAGE_prepared.csv
│   ├── 2017_2024_CRIMINALITE_prepared.csv
│   ├── 2017_2024_ELECTIONS_prepared.csv
│   ├── 2017_2024_IMMIGRATION_prepared.csv
│   ├── 2017_2024_PAUVRETE_prepared.csv
│   └── departements.geojson
├── database/
│   ├── label_encoder_y.joblib
│   └── preprocessor_X.joblib
├── models/
│   └── random_forest_predictor.joblib
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── prediction.ipynb
├── streamlit/
│   └── dashboard.py
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

#### A.2 Commandes d'Installation
```bash
# Clonage du projet
git clone [repository-url]
cd epsi-mspr-1

# Configuration environnement
cp .env.example .env
# Éditer .env avec vos paramètres

# Lancement du pipeline
docker-compose up --build

# Lancement du dashboard (nouveau terminal)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit/dashboard.py
```

### Annexe B : Extraits de Code Clés

#### B.1 Preprocessing Pipeline
```python
def create_elections_view(engine):
    """Création de la vue agrégée elections_all"""
    create_view_query = """
    CREATE OR REPLACE VIEW elections_all AS
    SELECT
        ed."YEAR",
        ed."DEPARTMENT_CODE", 
        ed."WINNER",
        cd."NUMBER_OF_VICTIMS",
        id."IMMIGRATION_RATE",
        pd."POVERTY_RATE",
        ud."UNEMPLOYMENT_RATE"
    FROM election_data ed
    LEFT JOIN crime_data cd ON ed."DEPARTMENT_CODE" = cd."DEPARTMENT_CODE" 
                            AND ed."YEAR" = cd."YEAR"
    -- Additional joins...
    """
    
    with engine.connect() as connection:
        connection.execute(text(create_view_query))
        connection.commit()
```

#### B.2 Model Training
```python
def train_and_evaluate_models(X_train, X_test, y_train, y_test):
    """Entraînement et évaluation des modèles"""
    models = {
        'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42),
        'GradientBoosting': GradientBoostingClassifier(random_state=42),
        'LogisticRegression': LogisticRegression(random_state=42, max_iter=1000)
    }
    
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        results[name] = {
            'accuracy': accuracy_score(y_test, y_pred),
            'f1_macro': f1_score(y_test, y_pred, average='macro'),
            'model': model
        }
    
    return results
```

#### B.3 Dashboard Visualization
```python
def create_france_map(data):
    """Création de la carte interactive de France"""
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
    
    # Chargement des contours géographiques
    with open('data/departements.geojson') as f:
        geojson_data = json.load(f)
    
    # Création des couleurs par parti
    color_map = {
        'RN': 'darkblue',
        'LR': 'blue', 
        'PS': 'pink',
        'LFI': 'red',
        'Autres': 'gray'
    }
    
    folium.Choropleth(
        geo_data=geojson_data,
        data=data,
        columns=['DEPARTMENT_CODE', 'WINNER'],
        key_on='feature.properties.code',
        fill_color='Set3',
        legend_name='Parti Gagnant'
    ).add_to(m)
    
    return m
```

### Annexe C : Métriques Détaillées

#### C.1 Résultats de Performance des Modèles
| Modèle | Accuracy | Weighted Precision | Observations |
|--------|----------|-------------------|--------------|
| Random Forest | 48.94% | 66.34% | ✅ Meilleure performance globale |
| Decision Tree | 44.68% | 60.25% | 🔶 Performance correcte |
| Logistic Regression | 29.79% | 62.13% | ⚠️ Sous-performance |
| SVM | 23.40% | 62.98% | ❌ Performance faible |

#### C.2 Statistiques du Dataset
| Métrique | Valeur |
|----------|--------|
| **Total échantillons** | 752 |
| **Train set** | 652 échantillons |
| **Test set** | 94 échantillons |
| **Prédictions 2027** | 94 départements |
| **Consolidation BI** | 375 lignes totales |
| **Période couverte** | 2017-2027 (11 ans) |

### Annexe D : Captures d'Écran

![Interface Principale](../assets/images/dashboard_main_interface.png)
*Figure D.1 : Interface principale du dashboard avec carte interactive*

![Comparaison des Modèles](../assets/images/model_comparison_chart.png)
*Figure D.2 : Graphique de comparaison des performances des modèles*

![Détail Département](../assets/images/dashboard_detail_view.png)
*Figure D.3 : Vue détaillée d'un département avec historique*

---

**Fin du Rapport**

*Ce document constitue le rapport académique complet du projet de prédiction électorale développé dans le cadre du Master EISI à EPSI Grenoble. L'ensemble du code source et des données sont disponibles sur le repository GitHub du projet.* 