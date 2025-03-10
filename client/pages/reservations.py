import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from components.navbar import navbar
from components.footer import footer
import api  # Importamos api para conectarnos con el backend

def reservations_page():
    navbar("reservations", show_reservations=False)
    st.title("📅 Book Your Chef")

    # Seleccionar fecha
    date = st.date_input("📆 Select a Date")

    # Obtener especialidades desde la API
    specialties = api.get_specialties()
    specialty_options = [s['description'] for s in specialties]
    specialty = st.selectbox("🍽 Select Specialty", specialty_options)

    selected_specialty = next((s for s in specialties if s['description'] == specialty), None)

    if selected_specialty:
        chefs = api.get_chefs_by_specialty(selected_specialty['id'])
        chef_options = [c['name'] for c in chefs]
        chef = st.selectbox("👨‍🍳 Select Chef", chef_options)

        # Sección de datos personales para la reserva
        with st.expander("🔽 Enter Your Details"):
            name = st.text_input("👤 Full Name")
            address = st.text_input("🏠 Address")
            phone = st.text_input("📞 Phone")
            email = st.text_input("📧 Email")
            gdpr = st.checkbox("✅ I agree to the GDPR terms")

        # Botón de confirmación
        if st.button("✅ Confirm Reservation"):
            if not all([name, address, phone, email, gdpr]):  # Verifica que todo esté completo
                st.warning("⚠ Please fill in all fields and accept the GDPR terms.")
            else:
                # Enviar la reserva al backend
                response = api.create_reservation({
                    "date": str(date), 
                    "specialty_id": selected_specialty['id'],
                    "chef_name": chef,
                    "customer_name": name,
                    "address": address,
                    "phone": phone,
                    "email": email
                })

                if response.get("success"):
                    st.success("🎉 Reservation confirmed!")
                else:
                    st.error("❌ Failed to make reservation. Try again later.")

    footer()

if __name__ == "__main__":
    reservations_page()
