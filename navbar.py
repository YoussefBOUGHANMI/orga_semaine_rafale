import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import app.all_app as pg



def ft_navbar_user(authenticator):

    pages = ["Activités 🏖️", "Ajouter une activité 📝", "Planning 📅", "Mon compte 👤"]
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
    
    if (page == "Mon compte 👤"):
        pg.ft_compte(authenticator)
    if (page == "Home"):
        pg.ft_home()
    if (page == "Activités 🏖️"):
        pg.ft_activites()
    if (page == "Ajouter une activité 📝"):
        pg.ft_ajout_activite()
    if (page == "Planning 📅"):
        pg.ft_display_plannig()

    
    

    
    

def ft_navbar_admin(authenticator):

    pages = ["Activités 🏖️", "Ajouter une activité 📝", "Planning 📅", "Mon compte 👤", "Admin 🛠️"]
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
    
    if (page == "Mon compte 👤"):
        pg.ft_compte(authenticator)
    if (page == "Admin 🛠️"):
        pg.ft_admin()
    if (page == "Home"):
        pg.ft_home()
    if (page == "Activités 🏖️"):
        pg.ft_activites()
    if (page == "Ajouter une activité 📝"):
        pg.ft_ajout_activite()
    if (page == "Planning 📅"):
        pg.ft_display_plannig()