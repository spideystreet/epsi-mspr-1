import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import plotly.express as px
import json

# =============================================================================
# Configuration de la page
# =============================================================================
st.set_page_config(
    page_title="Dashboard Élections 🇫🇷",
    page_icon="🗳️",
    layout="wide"
)

# =============================================================================
# Connexion à la base de données (avec cache pour la performance)
# =============================================================================
@st.cache_resource
def get_db_engine():
    """Crée et retourne une connexion à la base de données."""
    load_dotenv()
    pg_user = os.getenv("PG_USER")
    pg_password = os.getenv("PG_PASSWORD")
    pg_host = os.getenv("PG_HOST")
    pg_port = os.getenv("PG_PORT")
    pg_dbname = os.getenv("PG_DBNAME")
    
    if not all([pg_user, pg_password, pg_host, pg_port, pg_dbname]):
        st.error("Les informations de connexion à la base de données sont manquantes. Vérifiez votre fichier .env.")
        st.stop()
        
    db_url = f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_dbname}"
    try:
        engine = create_engine(db_url)
        # Test connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return engine
    except Exception as e:
        st.error(f"Erreur de connexion à la base de données : {e}")
        st.stop()

# =============================================================================
# Chargement des données (avec cache pour la performance)
# =============================================================================
@st.cache_data
def load_data():
    """Charge les données depuis la vue PostgreSQL."""
    engine = get_db_engine()
    try:
        # La vue `election_data_for_bi` contient les données historiques ET les prédictions pour 2027
        query = "SELECT * FROM election_data_for_bi;"
        df = pd.read_sql(query, engine)
        # Assurer que les types de données sont corrects
        df['YEAR'] = df['YEAR'].astype(int)
        df['DEPARTMENT_CODE'] = df['DEPARTMENT_CODE'].astype(str).str.zfill(2)
        return df
    except Exception as e:
        st.error(f"Erreur lors du chargement des données depuis la vue 'election_data_for_bi' : {e}")
        return pd.DataFrame()

@st.cache_data
def load_geojson():
    """Charge le fichier GeoJSON des départements."""
    geojson_path = 'data/departements.geojson'
    if not os.path.exists(geojson_path):
        st.error(f"Le fichier '{geojson_path}' est introuvable. Ce fichier est nécessaire pour la carte.")
        return None
    try:
        with open(geojson_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier GeoJSON : {e}")
        return None

# =============================================================================
# Application Principale
# =============================================================================
st.title("🇫🇷 Tableau de Bord des Élections Présidentielles")
st.markdown("Analyse des résultats historiques et prédictions pour **2027**.")

# Chargement des données
election_df = load_data()
geojson = load_geojson()

if election_df.empty or geojson is None:
    st.warning("Impossible d'afficher le tableau de bord car les données ou le fichier GeoJSON n'ont pas pu être chargés.")
    st.stop()

# --- Barre latérale avec les filtres ---
st.sidebar.header("Filtres")

# Sélecteur d'année
available_years = [2027, 2024, 2023, 2017]
selected_year = st.sidebar.selectbox("Choisissez une année", available_years)

# Filtrer les données en fonction de l'année sélectionnée
df_filtered = election_df[election_df['YEAR'] == selected_year].copy()

# --- Affichage principal ---
header_text = f"Résultats pour l'année {selected_year}"
if selected_year == 2027:
    header_text = f"Prédictions pour l'année {selected_year}"
st.header(header_text)

# Si 2027 est sélectionnée, afficher une note spéciale
if selected_year == 2027:
    st.info("✨ Les résultats affichés pour 2027 sont des **prédictions** basées sur un modèle de Machine Learning.")

# Définir une palette de couleurs pour les partis
color_map = {
    'DROITE': '#0066CC',      # Bleu
    'GAUCHE': '#FF0000',      # Rouge
    'CENTRE': '#FF8C00',      # Orange
    'E.DROITE': '#00008B',  # Bleu foncé
    'E.GAUCHE': '#8B0000'   # Rouge foncé
}

# --- Layout en colonnes ---
col1, col2 = st.columns((2, 1))

with col1:
    st.subheader("📍 Carte des résultats par département")
    
    fig_map = px.choropleth_mapbox(
        df_filtered,
        geojson=geojson,
        locations='DEPARTMENT_CODE',
        featureidkey="properties.code",
        color='WINNER',
        color_discrete_map=color_map,
        mapbox_style="carto-positron",
        zoom=4.5,
        center={"lat": 46.603354, "lon": 1.888334},
        opacity=0.7,
        hover_name='DEPARTMENT_CODE', # Amélioration du survol
        hover_data={'WINNER': True, 'DEPARTMENT_CODE': False},
        labels={'WINNER': 'Parti Gagnant'}
    )
    fig_map.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        legend_title_text='Parti Gagnant'
    )
    st.plotly_chart(fig_map, use_container_width=True)

with col2:
    st.subheader("📊 Résultats agrégés")
    
    # Calculer le nombre de départements gagnés
    results_summary = df_filtered['WINNER'].value_counts().reset_index()
    results_summary.columns = ['Parti', 'Départements Gagnés']
    
    # Afficher les métriques
    total_departments = len(df_filtered)
    if not results_summary.empty:
        winner_party = results_summary.iloc[0]['Parti']
        winner_count = results_summary.iloc[0]['Départements Gagnés']
        help_text = f"{winner_party} est arrivé en tête dans {winner_count} départements."
        
        st.metric(
            label="Parti en tête",
            value=winner_party,
            help=help_text
        )
    
    st.metric(
        label="Nombre de départements analysés",
        value=total_departments
    )

    # Diagramme en barres
    fig_bar = px.bar(
        results_summary,
        x='Parti',
        y='Départements Gagnés',
        color='Parti',
        color_discrete_map=color_map,
        text='Départements Gagnés'
    )
    fig_bar.update_layout(
        xaxis_title="Parti Politique",
        yaxis_title="Nombre de départements",
        showlegend=False
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# --- Section Évolution des Indicateurs ---
st.subheader("📈 Évolution des indicateurs socio-économiques (Moyenne Nationale)")

# Préparer les données - exclure 2027 car les indicateurs sont un proxy de 2024
evolution_df = election_df[election_df['YEAR'] < 2027].copy()

features_to_plot = {
    'NUMBER_OF_VICTIMS': 'Nombre de victimes (moyenne par département)',
    'IMMIGRATION_RATE': 'Taux d\'immigration (%)',
    'POVERTY_RATE': 'Taux de pauvreté (%)',
    'UNEMPLOYMENT_RATE': 'Taux de chômage (%)'
}

# Calculer la moyenne nationale pour chaque année
evolution_avg = evolution_df.groupby('YEAR')[list(features_to_plot.keys())].mean().reset_index()

# Mettre les données en format long pour Plotly
evolution_melted = evolution_avg.melt(
    id_vars=['YEAR'],
    value_vars=list(features_to_plot.keys()),
    var_name='Indicateur',
    value_name='Valeur'
)
evolution_melted['Indicateur'] = evolution_melted['Indicateur'].map(features_to_plot)

# Créer le graphique en lignes avec facettes
fig_evolution = px.line(
    evolution_melted,
    x='YEAR',
    y='Valeur',
    facet_row='Indicateur',
    height=800,
    labels={'YEAR': 'Année'},
    markers=True,
    title="Évolution des indicateurs clés en France (Moyenne nationale 2017-2024)"
)

# Mettre à jour les axes Y pour qu'ils soient indépendants et nettoyer les titres
fig_evolution.update_yaxes(matches=None, title_text="")
fig_evolution.update_layout(showlegend=False)
fig_evolution.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))

st.plotly_chart(fig_evolution, use_container_width=True)
st.info(
    "Ce graphique montre la moyenne nationale (non pondérée) pour chaque indicateur, calculée sur l'ensemble des départements. "
    "Les données de 2027 ne sont pas affichées ici car les indicateurs socio-économiques pour cette année prédictive sont basés sur les chiffres de 2024."
)

# Afficher la table des données
st.subheader("📄 Données détaillées")
st.dataframe(df_filtered)

st.sidebar.info("Ce tableau de bord est généré avec Streamlit et Plotly, en utilisant des données d'une base PostgreSQL.") 