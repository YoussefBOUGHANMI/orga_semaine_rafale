import streamlit as st



def ft_home():


    st.markdown("""
        Les amis,

        Ça y est, on y est enfin ! Bienvenue à notre fameuse "Semaine Rafale". Cette semaine, c'est notre terrain de jeu, notre moment à nous, où on va pouvoir se lâcher et profiter à fond.

        Plutôt que de suivre un programme pré-établi, on vous propose quelque chose de plus fun : chacun de nous va apporter ses idées pour rendre cette semaine encore plus géniale. Vous avez une idée d'activité ajouter là au programme.
    """)
    for i in range(4):
        st.write("\n")
    
    col1, col2 = st.columns([1,9])
    col2.image("/Users/youssefboughanmi/projet_semaine_rafal/utils/images_site/Hv62.gif", caption="Quand tu sais que cette semaine sera légendaire 😎")
