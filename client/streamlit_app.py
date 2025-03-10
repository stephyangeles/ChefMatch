import streamlit as st
import utils
from components.navbar import navbar
from components.footer import footer
from pages import reservations, staff, chef_agenda, admin_ledger

def main():
    page = utils.get_page()

    if page == "reservations":
        reservations.reservations_page()
    elif page == "staff":
        staff.staff_page()
    elif page == "chef_agenda":
        chef_agenda.chef_agenda_page()
    elif page == "admin_ledger":
        admin_ledger.admin_ledger_page()
    else:
        navbar("main")
        st.title("ChefMatch")
        st.write("About Us: Lorem ipsum dolor sit amet...")
        footer()

if __name__ == "__main__":
    main()