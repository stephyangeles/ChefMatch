import streamlit as st
from components.navbar import navbar
from components.footer import footer

def staff_page():
    navbar("staff", show_staff=False)
    st.title("Staff Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Implement login logic here
        if username == "chef":
            st.experimental_set_query_params(page="chef_agenda")
            st.experimental_rerun()
        elif username == "admin":
            st.experimental_set_query_params(page="admin_ledger")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")
    footer()

if __name__ == "__main__":
    staff_page()