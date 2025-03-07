import streamlit as st
from components.navbar import navbar
from components.footer import footer

def admin_ledger_page():
    navbar("admin_ledger", show_reservations=False, show_staff=False, show_logout=True)
    st.title("General Ledger")
    # Implement ledger list and editing here
    st.write("Ledger list goes here...")
    footer()

if __name__ == "__main__":
    admin_ledger_page()