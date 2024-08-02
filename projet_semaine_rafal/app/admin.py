import streamlit as st
import yaml



import yaml
import streamlit as st

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)


def get_usernames(config):
    return set(config['credentials']['usernames'].keys())






def ft_admin():
    
    # Remplacer par le chemin réel de vos fichiers YAML
    config_path = '/Users/youssefboughanmi/projet_semaine_rafal/authentification/config.yaml'
    new_config_path = '/Users/youssefboughanmi/projet_semaine_rafal/authentification/new_config.yaml'

    config = read_yaml(config_path)
    new_config = read_yaml(new_config_path)

    config_usernames = get_usernames(config)
    new_config_usernames = get_usernames(new_config)

    new_users = new_config_usernames - config_usernames
    
    st.title('Nouveaux utilisateurs')
    
    for user in new_users:
        col1 , col2, col3 = st.columns([3 , 1, 1])
        col1.write(user + "   :   [" + new_config['credentials']['usernames'][user]["email"] + "]")
        if col2.button('Accepter', key=f'accept_{user}'):
            # Add user to config
            config['credentials']['usernames'][user] = new_config['credentials']['usernames'][user]
            write_yaml(config, config_path)

            # Remove user from new_config
            del new_config['credentials']['usernames'][user]
            write_yaml(new_config, new_config_path)

            st.experimental_rerun()
        if col3.button('Refuser', key=f'reject_{user}'):
            # Remove user from new_config
            del new_config['credentials']['usernames'][user]
            write_yaml(new_config, new_config_path)

            st.experimental_rerun()
     