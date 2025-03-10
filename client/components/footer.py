import streamlit as st

def footer():
    st.markdown("---") 

    col1, col2 = st.columns([1, 2])  

    with col1:
        st.image("client/assets/logos/ChefMatch-logoblanco.png", width=150)  

    with col2:
        icon_container = st.container()
        with icon_container:
            st.image(["client/assets/icons/icons-chef-1.png",
                      "client/assets/icons/icons-chef-2.png",
                      "client/assets/icons/icons-chef-3.png"], width=100)  

    st.markdown("© 2024 ChefMatch®. All rights reserved.") 
    st.markdown("""
    Disclaimer:  
    Al usar esta plataforma exclusiva, accedes a una herramienta diseñada para chefs privados,  
    optimizando la gestión de tus reservas con la máxima eficiencia y discreción.  
    Tu privacidad y la calidad de tu experiencia son nuestra prioridad.
    """, unsafe_allow_html=True)

