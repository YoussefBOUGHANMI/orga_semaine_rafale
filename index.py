import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg
from authentification.auth import *
from navbar import *


st.set_page_config(initial_sidebar_state="collapsed")


def main():

    authenticator = ft_login()

    if st.session_state["authentication_status"]:
        if(st.session_state["name"] == "admin" ):
            ft_navbar_admin(authenticator)
        else: 
            ft_navbar_user(authenticator)
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password or register ')
    
    
main()