import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import app.all_app as pg

# Fonction pour supprimer le nom de l'état de session
def delete_name():
    if 'name' in st.session_state:
        del st.session_state['name']
        st.query_params['name'] = ''

def ft_navbar_user():

    pages = ["Activités 🏖️", "Ajouter une activité 📝", "Planning 📅"]
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(parent_dir, "utils/images_site/logo.svg")
    styles = {
        "nav": {
            "background-color": "royalblue",
            "justify-content": "left",
        },
        "img": {
            "padding-right": "14px",
        },
        "span": {
            "color": "white",
            "padding": "14px",
        },
        "active": {
            "background-color": "white",
            "color": "var(--text-color)",
            "font-weight": "normal",
            "padding": "14px",
        }
    }
    options = {
        "show_menu": False,
        "show_sidebar": False,
    }

    page = st_navbar(
        pages,
        logo_path=logo_path,
        styles=styles,
        options=options,
    )
    
        
    if (page == "Home"):
        pg.ft_home()
        
        for i in range(5) :
            st.write("\n")
            
        col1, col2 = st.columns([2,3])
        if col2.button("Se déconnecter"):
            delete_name()
            st.rerun()
            
    if (page == "Activités 🏖️"):
        pg.ft_activites()
    if (page == "Ajouter une activité 📝"):
        pg.ft_ajout_activite()
    if (page == "Planning 📅"):
        pg.ft_display_plannig()

    
    

    