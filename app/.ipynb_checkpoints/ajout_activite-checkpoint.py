import streamlit as st
import yaml
import os
from PIL import Image
import io
from datetime import datetime

def ft_ajout_activite(): 
    # Dossier pour enregistrer les images
    image_dir = "/Users/youssefboughanmi/projet_semaine_rafal/utils/images_activites"
    os.makedirs(image_dir, exist_ok=True)

    # Chemin du fichier YAML
    yaml_file = "/Users/youssefboughanmi/projet_semaine_rafal/utils/activites.yaml"

    # Charger les données existantes si le fichier existe
    if os.path.exists(yaml_file):
        with open(yaml_file, 'r') as file:
            activites = yaml.safe_load(file) or []
    else:
        activites = []

    st.title("Créer une activité")

    # Formulaire pour créer une activité
    with st.form(key='create_activity_form' , clear_on_submit=True):
        nom_activite = st.text_input("Nom de l'activité")
        description = st.text_area("Description")
        duree = st.selectbox("Durée de l'activité", ["Matin", "Apres-midi", "Toute la journee"])
        date_activite = st.date_input("Date de l'activité", datetime(2024, 8, 10), min_value=datetime(2024, 8, 10), max_value=datetime(2024, 8, 18))
        image = st.file_uploader("Charger une image", type=["png", "jpg", "jpeg"])
        submit_button = st.form_submit_button(label='Créer')

    # Action lors du clic sur le bouton 'Créer'
    if submit_button:
        if nom_activite and description and duree:
            # Vérifier si le nom d'activité existe déjà
            if any(act["nom"].lower() == nom_activite.lower() for act in activites):
                st.error(f"L'activité '{nom_activite}' existe déjà. Veuillez choisir un autre nom.")
            else:
                # Utilisation d'une image par défaut si aucune image n'est téléchargée
                if image is None:
                    image_path = "/Users/youssefboughanmi/projet_semaine_rafal/utils/images_activites/image_default.png"
                else:
                    # Enregistrer l'image téléchargée avec le même nom que l'activité
                    image_path = os.path.join(image_dir, f"{nom_activite}.png")
                    image_data = image.getbuffer()

                    # Convertir l'image en basse qualité
                    with Image.open(io.BytesIO(image_data)) as img:
                        img = img.convert("RGB")  # Assurer le bon mode d'image
                        img.save(image_path, format='PNG', quality=10)  # Ajuster la qualité si nécessaire

                # Ajouter les informations de l'activité au dictionnaire
                activite = {
                    "nom": nom_activite,
                    "description": description,
                    "date": date_activite.strftime('%Y-%m-%d'),
                    "duree": duree,
                    "image": image_path,
                    "initiateur": st.session_state["name"],
                    "inscrits": st.session_state["name"],
                    "nb_inscrits": 1
                }
                activites.append(activite)
                # Enregistrer les informations dans le fichier YAML
                with open(yaml_file, 'w') as file:
                    yaml.safe_dump(activites, file)

                st.success(f"L'activité '{nom_activite}' a été créée avec succès!")
        else:
            st.error("Veuillez remplir tous les champs du formulaire.")
