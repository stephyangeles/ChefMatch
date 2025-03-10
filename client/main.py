import streamlit as st
import time

from components.navbar import navbar
from components.footer import footer

def main():
    # Load custom CSS
    st.markdown("""
    <style>
    /* Navbar Styles */
    .navbar {
        background-color: #000;
        padding: 10px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .navbar img {
        height: 50px;
    }

    /* Title Styling */
    .title {
        font-family: 'Arial', sans-serif;
        color: #e63946;
        text-align: center;
        font-size: 32px;
        margin-top: 20px;
    }

    /* Footer Styles */
    .footer {
        background-color: #000;
        color: white;
        padding: 20px;
        text-align: center;
        position: relative;
        bottom: 0;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

  
    navbar("main")
   
    st.markdown('<h1 class="title">ChefMatch</h1>', unsafe_allow_html=True)

    st.write("Bienvenido a ChefMatch, la plataforma que transforma tu hogar en un exclusivo restaurante de alta cocina. Nuestro objetivo es brindarte experiencias gastronómicas inolvidables al conectar a chefs profesionales con clientes que buscan disfrutar de alta cocina, sin salir de casa.")

    st.write("### ¿Por qué elegirnos?")
    st.write("- **Profesionalismo**: Trabajamos solo con chefs altamente capacitados y apasionados por la gastronomía.")
    st.write("- **Experiencias únicas**: Cada plato es una obra de arte que cuenta una historia, creada especialmente para ti.")
    st.write("- **Comodidad y exclusividad**: Disfruta de la alta cocina sin moverte de tu hogar, en el ambiente más cómodo y seguro.")
    
    st.write("Descubre un mundo de sabores, aromas y momentos especiales con ChefMatch. La cocina gourmet ahora está al alcance de tu mano.")

   
    image_placeholder = st.empty()

    images = [
        "client/assets/images/banner-chef-2.png",
        "client/assets/images/banner-chef-3.png",
        "client/assets/images/banner-chef-4.png"
    ]

    for i in range(len(images) * 2):  
        image_placeholder.image(images[i % len(images)], use_container_width=True)
        time.sleep(2)  

    
    # Display the footer
    footer()

if __name__ == "__main__":
    main()
