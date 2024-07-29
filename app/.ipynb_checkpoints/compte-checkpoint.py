import streamlit as st


def ft_compte(authenticator):

    
    # ----- Update data ----- #
    
    if st.session_state["authentication_status"]:
        try:
            if authenticator.update_user_details(st.session_state["username"] , fields = {'Form name':"Mettre à jour des données", 'Field':'Champ', 'Name':'Nom', 
                                                                                                       'Email':'Email', 'New value':'Nouvelle valeur', 'Update':'Mise à jour'}):
                with open('authentification/config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                st.success('Entries updated successfully')
        except Exception as e:
            st.error(e)
            
            
    # ----- Update password ----- #
    
    if st.session_state["authentication_status"]:
        try:
            if authenticator.reset_password(st.session_state["username"] , fields =  {'Form name':'Réinitialiser le mot de passe', 'Current password':'Mot de passe actuel', 'New password':'Nouveau mot de passe', 
                                                                                           'Repeat password': 'Répéter le mot de passe', 'Reset':'Réinitialiser'}):
                with open('authentification/config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                st.success('Password modified successfully')
        except Exception as e:
            st.error(e)
            
    st.write("\n\n\n\n\n\n\n\n")
    st.write("\n\n\n\n\n\n\n\n")
    col1 , col2 = st.columns([2,3]) 
    with col2:
        authenticator.logout(button_name = "Se déconnecter")
            
    