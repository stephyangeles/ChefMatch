import streamlit as st
from components.navbar import navbar
from components.footer import footer

def chef_agenda_page():
    navbar("chef_agenda", show_reservations=False, show_staff=False, show_logout=True)
    st.title("Your Agenda")
    # Implement calendar and reservation management here
    st.write("Calendar goes here...")
    footer()

if __name__ == "__main__":
    chef_agenda_page()