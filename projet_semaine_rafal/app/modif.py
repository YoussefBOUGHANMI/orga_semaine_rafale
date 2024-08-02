import streamlit as st
import yaml
import time
import os
from datetime import datetime



def manage_modif(activity_info):
    return()
    
    # Chemin du fichier YAML
    yaml_file = "/Users/youssefboughanmi/projet_semaine_rafal/utils/activites.yaml"

    # Charger les données existantes si le fichier existe
    if os.path.exists(yaml_file):
        with open(yaml_file, 'r') as file:
            activites = yaml.safe_load(file) or []
    else:
        activites = []
    
    with st.form(key='create_activity_form' , clear_on_submit=True):
        nom_activite = st.text_input("Nom de l'activité" , value=activity_info["nom"])
        description = st.text_area("Description" , value=activity_info["description"])
        duree = st.selectbox("Durée de l'activité", ["Matin", "Apres-midi", "Toute la journée"]  , index=["Matin", "Apres-midi", "Toute la journée"].index(activity_info["duree"]) )
        date_activite = st.date_input("Date de l'activité", datetime.strptime(activity_info["date"], '%Y-%m-%d'), min_value=datetime(2024, 8, 10), max_value=datetime(2024, 8, 18))
        submit_button = st.form_submit_button(label='modifier')
        
        
    if submit_button:
        #drop the old one
        activites = [acti for acti in activites if acti["nom"] != activity_info["nom"]]
        
        #save the new infos 
        activite = {
                "nom": nom_activite,
                "description": description,
                "date": date_activite.strftime('%Y-%m-%d'),
                "duree": duree,
                "image": activity_info["image"],
                "initiateur" : activity_info["initiateur"],
                "inscrits" : activity_info["inscrits"] ,
                "nb_inscrits" : activity_info["nb_inscrits"]
            }
        activites.append(activite)
        print(activites)
        with open(yaml_file, 'w') as file:
            yaml.safe_dump(activites, file)

