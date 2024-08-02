import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg
from authentification.auth import *
from navbar import *


st.set_page_config(initial_sidebar_state="collapsed")



import streamlit as st

# Fonction pour initialiser le nom dans l'état de session
def initialize_name():
    query_params = st.query_params
    if 'name' in query_params:
        st.session_state['name'] = query_params['name']
    else:
        st.session_state['name'] = ''

# Fonction pour mettre à jour le nom dans l'état de session et les paramètres de requête
def update_name():
    if(st.session_state['name'] == ''):
        name_input = st.text_input("Entrer votre nom:", st.session_state['name'])
        if name_input != st.session_state['name']:
            st.session_state['name'] = name_input
            st.query_params['name'] = name_input
        if st.button("Se connecter"):
            st.rerun()


        
def main():
    # Initialiser le nom dans l'état de session si nécessaire
    if 'name' not in st.session_state:
        initialize_name()

        # Appeler la fonction pour mettre à jour le nom
    update_name()

    # Vérifier si le nom est défini et afficher un message de bienvenue
    if st.session_state['name']:
         ft_navbar_user()

main()