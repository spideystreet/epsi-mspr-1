import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import plotly.express as px
import json

# =============================================================================
# Configuration de la page
# =============================================================================
st.set_page_config(
    page_title="Dashboard Élections",
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
        return None
        
    db_url = f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_dbname}"
    return create_engine(db_url)

# =============================================================================
# Chargement des données (avec cache pour la performance)
# =============================================================================
@st.cache_data
def load_data():
    """Charge les données depuis la vue PostgreSQL."""
    engine = get_db_engine()
    if engine:
        try:
            query = "SELECT * FROM election_data_for_bi;"
            df = pd.read_sql(query, engine)
            # Assurer que les types de données sont corrects
            df['YEAR'] = df['YEAR'].astype(int)
            df['DEPARTMENT_CODE'] = df['DEPARTMENT_CODE'].astype(str).str.zfill(2)
            return df
        except Exception as e:
            st.error(f"Erreur lors du chargement des données : {e}")
            return pd.DataFrame()
    return pd.DataFrame()

@st.cache_data
def load_geojson():
    """Charge le fichier GeoJSON des départements."""
    try:
        with open('data/departements.geojson', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Le fichier 'data/departements.geojson' est introuvable. Ce fichier est nécessaire pour la carte.")
        return None

# =============================================================================
# Application Principale
# =============================================================================
st.title("🇫🇷 Tableau de Bord des Élections Présidentielles")

# Chargement des données
election_df = load_data()
geojson = load_geojson()

if not election_df.empty and geojson:
    
    # --- Barre latérale avec les filtres ---
    st.sidebar.header("Filtres")
    
    # Sélecteur d'année
    available_years = sorted(election_df['YEAR'].unique(), reverse=True)
    selected_year = st.sidebar.selectbox("Choisissez une année", available_years)
    
    # Filtrer les données en fonction de l'année sélectionnée
    df_filtered = election_df[election_df['YEAR'] == selected_year]
    
    # --- Affichage principal ---
    st.header(f"Résultats pour l'année {selected_year}")
    
    # Définir une palette de couleurs pour les partis
    color_map = {
        'DROITE': 'blue',
        'GAUCHE': 'red',
        'CENTRE': 'orange',
        'E.DROITE': 'darkblue',
        'E.GAUCHE': 'darkred'
    }
    
    # Carte de France
    st.subheader("Carte des résultats par département")
    
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
        opacity=0.6,
        labels={'WINNER': 'Parti Gagnant'}
    )
    fig_map.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        legend_title_text='Parti Gagnant'
    )
    st.plotly_chart(fig_map, use_container_width=True)

else:
    st.warning("Impossible d'afficher le tableau de bord car les données ou le fichier GeoJSON n'ont pas pu être chargés.")

st.info("Ce tableau de bord est généré avec Streamlit et Plotly, en utilisant les données de la base PostgreSQL.") 