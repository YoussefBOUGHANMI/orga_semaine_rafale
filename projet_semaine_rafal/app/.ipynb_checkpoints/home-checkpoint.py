import streamlit as st



def ft_home():

    st.markdown("""
    Aloura,

    on y est enfin ! Bienvenue à notre légendaire "Semaine Rafale". Cette semaine, on va tout déchirer et profiter à fond !

    Pas de programme tout fait ici, on fait ça à notre sauce : chacun de nous va ramener ses idées pour rendre cette semaine encore plus dingue. Vous avez une idée d'activité ? Balancez-la au programme !
    """)


    
    for i in range(4):
        st.write("\n")
    
    col1, col2 = st.columns([1,9])
    col2.image("/Users/youssefboughanmi/projet_semaine_rafal/utils/images_site/Hv62.gif", caption="\"We gon' live this life like it's golden.\" - J. Cole 😎")
