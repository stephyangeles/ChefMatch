import streamlit as st
import sys
import os
import api  # Importamos api para conectarnos con el backend

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from components.navbar import navbar
from components.footer import footer

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
            if not all([name, address, phone, email, gdpr]):
                st.warning("⚠ Please fill in all fields and accept the GDPR terms.")
            else:
                # Verificar si el usuario ya existe en la API
                users = api.get_users()
                existing_user = next((u for u in users if u["email"] == email), None)

                if not existing_user:
                    # Si el usuario no existe, crearlo
                    new_user = api.create_user(name, email, phone)
                    if not new_user:
                        st.error("❌ Failed to create user. Please try again.")
                        st.stop()

                    user_id = new_user["id"]  # Obtener ID del nuevo usuario
                else:
                    user_id = existing_user["id"]  # Obtener ID del usuario existente

                # Enviar la reserva al backend con el ID del usuario
                response = api.create_reservation({
                    "date": str(date),
                    "location": "Madrid",  # Puedes hacer esto dinámico si es necesario
                    "user": user_id,
                    "chef": next((c['id'] for c in chefs if c['name'] == chef), None)
                })

                if response.get("success"):
                    st.success("🎉 Reservation confirmed!")
                else:
                    st.error("❌ Failed to make reservation. Try again later.")

    footer()

if __name__ == "__main__":
    reservations_page()
