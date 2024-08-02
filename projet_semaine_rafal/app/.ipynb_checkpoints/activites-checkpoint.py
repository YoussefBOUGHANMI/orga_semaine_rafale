import streamlit as st
from PIL import Image
from streamlit_navigation_bar import st_navbar
import pandas as pd
import yaml
import time
import os
from app.modif import *
from app.inscription import *



def ft_supprimer(activity_info):
    
    yaml_file = "/Users/youssefboughanmi/projet_semaine_rafal/utils/activites.yaml"
    if os.path.exists(yaml_file):
        with open(yaml_file, 'r') as file:
            activites = yaml.safe_load(file) or []
    else:
        activites = []
        
    activites = [acti for acti in activites if acti["nom"] != activity_info["nom"]]

    with open(yaml_file, 'w') as file:
        yaml.safe_dump(activites, file)

    st.rerun()
        
        

def display_creator_button(activity_info):
    
    if st.button('Modifier' , key = activity_info["nom"] + "modif"):
        st.write("en développement")
        manage_modif(activity_info)
    if st.button('Supprimer', key = activity_info["nom"] + "supp"):
        ft_supprimer(activity_info)

            
def display_user_button(activity_info):
    
    liste_inscrits = [x for x in activity_info["inscrits"].split(",")]
    
    if(st.session_state["name"] not in liste_inscrits):
        if st.button('S\'inscrire' ,key =activity_info["nom"] + "insc"):
                ft_inscription(activity_info)
    else:
        if st.button('Se désinscrire', key = activity_info["nom"] + "desi"):
                ft_desinscription(activity_info)
                
                
    
def display_one_activite(activity_info):
    
    
    # Créer une colonne pour les informations de l'activité et une autre pour les actions
    col1, col2 = st.columns([5, 3])

    with col1:
        # Utiliser une mise en page en colonnes pour aligner l'image et les informations
        img_col, info_col = st.columns([1, 2])
        t1 = time.time()
        with img_col:
            image = Image.open(activity_info["image"])  # Remplacez par le chemin de votre photo
            st.image(image, caption='Photo de l\'activité', use_column_width=True)
        print(time.time() - t1)
        t1 = time.time()
        with info_col:
            st.write("**Nom**: " +  activity_info["nom"])
            st.write("**Description**: " +  activity_info["description"])
            st.write("**Date** : " + activity_info["date"])
            st.write("**Durée de l'activité** : " + activity_info["duree"])
            st.write("**Liste des inscrits** : " +  activity_info["inscrits"])
            st.write("**Nombre d'inscrits**: " + str(activity_info["nb_inscrits"]))
        print(time.time() - t1)

    with col2:
        # creator 
        if (activity_info["initiateur"] == st.session_state["name"] or st.session_state["name"] == "admin" ):
            display_creator_button(activity_info)
        #users
        else :
            display_user_button(activity_info)
            


            
    for i in range(6):
        st.write("\n")
    return("")


def ft_activites():
    
    # Chemin vers votre fichier YAML
    file_path = '/Users/youssefboughanmi/projet_semaine_rafal/utils/activites.yaml'

    # Initialiser une liste pour stocker les dictionnaires
    activites = []

    # Lire le fichier YAML
    with open(file_path, 'r') as file:
        # Charger tout le contenu du fichier dans une liste
        activites = yaml.safe_load(file)
        
    #sort activité avant display
    activites = sorted(activites, key=lambda x: x['nom'])
    
    st.title("Listes des activités")
    
    if(len(activites) == 0):
        return()
    for i in range(10):
        st.write("\n")

    for activ in activites:
        display_one_activite(activ)
        st.write("\n")
    