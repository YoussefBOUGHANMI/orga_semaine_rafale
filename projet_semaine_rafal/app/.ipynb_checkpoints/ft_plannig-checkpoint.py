import streamlit as st
from streamlit_calendar import calendar
import os 
import yaml



def get_end_date(date_act , duree):
    
    if(duree == 'Matin'):
        return(date_act + "T12:00:00")
    else :
        return(date_act + "T18:00:00")
    
    

def get_start_date(date_act , duree):
    
    if(duree == 'Matin' or duree == 'Toute la journee'):
        return(date_act + "T09:00:00")
    else :
        return(date_act + "T14:00:00")
    
def ft_plannig(user , type_pl = "user"):
    
    
    # Chemin du fichier YAML
    yaml_file = "/Users/youssefboughanmi/projet_semaine_rafal/utils/activites.yaml"

    # Charger les données existantes si le fichier existe
    if os.path.exists(yaml_file):
        with open(yaml_file, 'r') as file:
            activites = yaml.safe_load(file) or []
    else:
        activites = []
        
    if(type_pl == "user"):    
        activites = [act for act in activites if user in act["inscrits"].split(",")]
        
    # Étape 1: Organiser les activités par date
    activites_par_date = {}
    for activite in activites:
        date = activite['date']
        if date not in activites_par_date:
            activites_par_date[date] = activite
        else:
            # Comparer le nombre d'inscrits
            if activite['nb_inscrits'] > activites_par_date[date]['nb_inscrits']:
                activites_par_date[date] = activite

    # Étape 2: Convertir le dictionnaire en liste avec uniquement la date et le nom de l'activité
    resultat_final = [{'title': activite['nom'], 'start': get_start_date(activite['date'], activite['duree']) , 
                        'end': get_end_date(activite['date'], activite['duree'])} for activite in activites_par_date.values()]

    return(resultat_final)



def ft_print_calendar(type_pl = "user"):
    
    calendar_options = {
        "editable": True,
        "selectable": True,
        "initialView": "timeGridWeek",  # Définit la vue initiale comme la semaine
        "initialDate": "2024-08-11",  # Définit la date initiale à 10 août 2024
        "headerToolbar": {
            "left": "prev,next",  # Supprime le bouton "Today"
            "center": "title",
            "right": "timeGridWeek,timeGridDay",  # Options de vue disponibles
        },
        "locale": "fr",  # Définit la langue sur français
        "buttonText": {  # Traduction des boutons de vue
            "timeGridWeek": "Semaine",
            "timeGridDay": "Jour"
        }
    }

    custom_css="""
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
    """

    cal = calendar(events=ft_plannig(st.session_state["name"] , type_pl), options=calendar_options, custom_css=custom_css)

    
def ft_display_plannig():
    option = st.selectbox(
    "Choix du planning",
    ("Mon planning", "Planning de l'équipe"),
)

    if(option == "Mon planning"):
        ft_print_calendar("user")

    else :
        ft_print_calendar("global")
        
        
