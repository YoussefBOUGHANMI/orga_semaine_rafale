import streamlit as st
import yaml
import os



def ft_inscription(activity_info):
    
    activity_info["inscrits"] = activity_info["inscrits"] + "," + st.session_state["name"]
    activity_info["nb_inscrits"] = activity_info["nb_inscrits"] + 1
    
    yaml_file = "/Users/youssefboughanmi/projet_semaine_rafal/utils/activites.yaml"
    if os.path.exists(yaml_file):
        with open(yaml_file, 'r') as file:
            activites = yaml.safe_load(file) or []
    else:
        activites = []
        
    activites = [acti for acti in activites if acti["nom"] != activity_info["nom"]]
        
    #save the new infos 
    activites.append(activity_info)

    with open(yaml_file, 'w') as file:
        yaml.safe_dump(activites, file)
    st.rerun()
    
    
def ft_desinscription(activity_info):
    
    liste_inscrits = [x for x in activity_info["inscrits"].split(",") if x != st.session_state["name"]]
    
    activity_info["inscrits"] = ",".join(liste_inscrits)
    activity_info["nb_inscrits"] = activity_info["nb_inscrits"] - 1
    
    yaml_file = "/Users/youssefboughanmi/projet_semaine_rafal/utils/activites.yaml"
    if os.path.exists(yaml_file):
        with open(yaml_file, 'r') as file:
            activites = yaml.safe_load(file) or []
    else:
        activites = []
        
    activites = [acti for acti in activites if acti["nom"] != activity_info["nom"]]
        
    #save the new infos 
    activites.append(activity_info)

    with open(yaml_file, 'w') as file:
        yaml.safe_dump(activites, file)
    st.rerun()
    