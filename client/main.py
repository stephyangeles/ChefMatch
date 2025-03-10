import streamlit as st
from components.navbar import navbar
from components.footer import footer

def main():
    # Load custom CSS
    st.markdown("""
    <style>
    /* Custom Navbar Styles */
    .css-1v3fvcr {
        background-color: #1d3557;  /* Dark Blue */
        color: white;
        padding: 10px 20px;
    }
    
    /* Change the font style for title */
    .css-18e3th9 {
        font-family: 'Arial', sans-serif;
        color: #e63946; /* Red */
    }

    /* Button styles */
    .css-1d391kg {
        background-color: #f1faee;  /* Light background */
        color: #1d3557;  /* Dark Blue */
        font-size: 16px;
    }
    
    /* Footer Styles */
    .css-1vh5g7g {
        background-color: #1d3557;
        color: white;
        padding: 20px;
        text-align: center;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
    }

    ::-webkit-scrollbar-thumb {
        background-color: darkgrey;
        border-radius: 6px;
    }

    ::-webkit-scrollbar-track {
        background: #f1faee;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display the navbar
    navbar("main")

    # Main content
    st.title("ChefMatch")
    st.write("Bienvenido a ChefMatch, la plataforma que transforma tu hogar en un exclusivo restaurante de alta cocina. Nuestro objetivo es brindarte experiencias gastronómicas inolvidables al conectar a chefs profesionales con clientes que buscan disfrutar de alta cocina, sin salir de casa.")

    st.write("¿Por qué elegirnos?")
    st.write("- **Profesionalismo**: Trabajamos solo con chefs altamente capacitados y apasionados por la gastronomía.")
    st.write("- **Experiencias únicas**: Cada plato es una obra de arte que cuenta una historia, creada especialmente para ti.")
    st.write("- **Comodidad y exclusividad**: Disfruta de la alta cocina sin moverte de tu hogar, en el ambiente más cómodo y seguro.")
    
    st.write("Descubre un mundo de sabores, aromas y momentos especiales con ChefMatch. La cocina gourmet ahora está al alcance de tu mano.")

    # Display the footer
    footer()

if __name__ == "__main__":
    main()
