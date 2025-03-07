import streamlit as st
from components.navbar import navbar
from components.footer import footer

def main():
    navbar("main")
    st.title("ChefMatch")
    st.write("About Us: Lorem ipsum dolor sit amet...")
    footer()

if __name__ == "__main__":
    main()