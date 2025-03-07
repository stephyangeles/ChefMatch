import streamlit as st
from components.navbar import navbar
from components.footer import footer
import api # Import your api.py file.

def reservations_page():
    navbar("reservations", show_reservations=False)
    st.title("Book Your Chef")

    date = st.date_input("Date")
    specialties = api.get_specialties() #get the specialties from the api
    specialty_options = [s['description'] for s in specialties]
    specialty = st.selectbox("Specialty", specialty_options)

    # Find the specialty ID
    selected_specialty = next((s for s in specialties if s['description'] == specialty), None)

    if specialty:
        chefs = api.get_chefs_by_specialty(selected_specialty['id']) #get the chefs by specialty id
        chef_options = [c['name'] for c in chefs]
        chef = st.selectbox("Chef", chef_options)

        if st.button("Reserve"):
            st.write("Additional Info:")
            name = st.text_input("Name")
            address = st.text_input("Address")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            gdpr = st.checkbox("I agree to the GDPR terms")

            if st.button("Confirm Reservation"):
                # Implement reservation logic here
                st.success("Reservation confirmed!")
    footer()

if __name__ == "__main__":
    reservations_page()