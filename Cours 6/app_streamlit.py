import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# ==============================================================================
# CONFIGURATION GÉNÉRALE DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="HortiData — Dashboard Botanique",
    layout="wide",
)

st.title("Système d'Aide à la Décision : Contrôle Qualité des Iris")
st.markdown(
    "Outil de calibrage des seuils morphologiques pour le tri en usine."
)


# ==============================================================================
# ÉTAPE 1 : CHARGEMENT DES DONNÉES (MISE EN CACHE)
# ==============================================================================
# TODO 1 : Décorez la fonction avec @st.cache_data pour éviter de recharger le dataset à chaque clic
def charger_donnees():
  df = sns.load_dataset("iris")
  # TODO 2 : Ajoutez la colonne 'surface_petale' (longueur * largeur du pétale) arrondie à 2 décimales
  # df['surface_petale'] = ...
  return df


df_iris = charger_donnees()

# ==============================================================================
# ÉTAPE 2 : PANNEAU LATÉRAL & FILTRES (SIDEBAR)
# ==============================================================================
st.sidebar.header("🎛️ Filtres de production")

# TODO 3 : Créez un sélecteur multiple (st.sidebar.multiselect) permettant de choisir les espèces à afficher
# - Label : "Sélectionner les espèces :"
# - Options : les valeurs uniques de df_iris['species']
# - Défaut : toutes les espèces sélectionnées par défaut
especes_selectionnees = ...  # st.sidebar.multiselect(...)

# Sécurité si l'étudiant décoche tout
if not especes_selectionnees:
  st.warning("Veuillez sélectionner au moins une espèce.")
  st.stop()

# TODO 4 : Filtrez df_iris pour ne garder que les lignes correspondant aux espèces sélectionnées
df_filtre = ...

# TODO 5 : Créez un slider (st.sidebar.slider) pour tester le seuil de décision sur la surface du pétale
# - Label : "Seuil de coupure Surface (cm²) :"
# - Borne min : 4.0, Borne max : 12.0, Valeur initiale : 7.5, Pas : 0.1
seuil_surface = ...

# ==============================================================================
# ÉTAPE 3 : BANDEAU DES INDICATEURS CLÉS (KPIS)
# ==============================================================================
# TODO 6 : Découpez l'écran en 3 colonnes avec st.columns(3)
# Dans col1 : affichez le nombre total de spécimens analysés (st.metric)
# Dans col2 : affichez la longueur moyenne des pétales (en cm, arrondi à 2 décimales)
# Dans col3 : affichez la surface médiane des pétales (en cm², arrondi à 2 décimales)
col1, col2, col3 = ...

# col1.metric(...)
# col2.metric(...)
# col3.metric(...)

st.markdown("---")

# ==============================================================================
# ÉTAPE 4 : ONGLETS D'ANALYSE & GRAPHIQUES
# ==============================================================================
# TODO 7 : Créez 2 onglets avec st.tabs :
# Onglet 1 : "🎯 Décision Bivariée"
# Onglet 2 : "📊 Distribution & Seuil d'Usine"
tab1, tab2 = ...

with tab1:
  st.subheader("Frontière de décision : Longueur vs Largeur du pétale")

  # TODO 8 : Créez une figure Matplotlib (fig1, ax1 = plt.subplots(figsize=(9, 4)))
  # Tracez un sns.scatterplot sur ax1 avec :
  # - data = df_filtre
  # - x = 'petal_length', y = 'petal_width'
  # - hue = 'species'
  # Ajoutez une ligne verticale rouge en pointillés à x=2.5 pour matérialiser la règle Setosa (ax1.axvline)
  # Affichez la figure dans Streamlit avec st.pyplot(fig1)

  # fig1, ax1 = ...
  # sns.scatterplot(...)
  # ax1.axvline(...)
  # st.pyplot(fig1)
  # plt.close(fig1)

  st.info(
      "💡 **Règle n°1 :** Les fleurs avec une longueur de pétale < 2.5 cm"
      " sont 100% Setosa."
  )

with tab2:
  st.subheader("Répartition des surfaces et impact du seuil sélectionné")

  # TODO 9 : Créez une seconde figure (fig2, ax2)
  # Tracez un sns.histplot sur 'surface_petale' avec kde=True et hue='species'
  # Tracez une ligne verticale noire (ax2.axvline) positionnée sur la variable 'seuil_surface' du slider
  # Affichez la figure avec st.pyplot(fig2)

  # fig2, ax2 = ...
  # sns.histplot(...)
  # ax2.axvline(...)
  # st.pyplot(fig2)
  # plt.close(fig2)

  # TODO 10 : Calculez combien de spécimens de l'échantillon filtré dépassent le seuil choisi
  # et affichez le résultat avec un st.write ou st.success