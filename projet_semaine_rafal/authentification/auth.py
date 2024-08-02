import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader



def ft_login():

    #left , center , right = st.columns([8 , 1 , 8])

    with open('/Users/youssefboughanmi/projet_semaine_rafal/authentification/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized']
    )
    
    # ---------- Login ------------#
    #with left :
    authenticator.login(fields = {'Form name':'Se connecter', 'Username':"Nom d'utilisateur", 'Password': "Mot de passe", 'Login': "se connecter"})
        
        
    
    # --------- Sign in -----------#
    
    #with right :
    if st.session_state["authentication_status"] in [False , None]:
        try:
            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False , 
                                                                                                         fields =  {'Form name':'Nouvel utilisateur','Name' : 'Nom' ,'Email':'Email', 
                                                                                                                    'Username': "Nom d'utilisateur", 'Password': "Mot de passe", 'Repeat password': "Répéter le mot de passe", 
                                                                                                                    'Register':"s'inscrire"})
            if email_of_registered_user:
                st.success('User registered successfully')
                with open('/Users/youssefboughanmi/projet_semaine_rafal/authentification/new_config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
        except Exception as e:
            st.error(e)
        
    
    return(authenticator)

   