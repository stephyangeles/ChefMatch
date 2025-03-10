import streamlit as st

def footer():
    col1, col2 = st.columns([1, 3])
    st.markdown("---")
    st.markdown("© 2024 ChefMatch®. All rights reserved.")
    st.markdown("Disclaimer: Al usar esta plataforma exclusiva, accedes a una herramienta diseñada para chefs privados, optimizando la gestión de tus reservas con la máxima eficiencia y discreción. Tu privacidad y la calidad de tu experiencia son nuestra prioridad.")
    with col1:
        st.image("client/assets/logos/ChefMatch-logoblanco.png", use_container_width=True)
