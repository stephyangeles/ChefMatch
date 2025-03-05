import streamlit as st
import requests

# URL de tu backend en Django
API_URL = "http://127.0.0.1:8000"

# Configurar la interfaz
st.title("ChefMatch - Administración")

# Sidebar de navegación
menu = st.sidebar.selectbox("Selecciona una opción", ["Ver Especialidades", "Añadir Especialidad", "Ver Chefs", "Añadir Chef"])

# Función para obtener especialidades
def get_specialties():
    response = requests.get(f"{API_URL}/specialties/")
    if response.status_code == 200:
        return response.json()
    return []

# Función para añadir una especialidad
def add_specialty(description):
    response = requests.post(f"{API_URL}/specialties/", json={"description": description})
    return response.status_code == 201

# Función para obtener chefs
def get_chefs():
    response = requests.get(f"{API_URL}/chefs/")
    if response.status_code == 200:
        return response.json()
    return []

# Función para añadir un chef
def add_chef(name, expertise, rating):
    response = requests.post(f"{API_URL}/chefs/", json={"name": name, "expertise": expertise, "rating": rating})
    return response.status_code == 201

# Opción: Ver Especialidades
if menu == "Ver Especialidades":
    st.subheader("Lista de Especialidades")
    specialties = get_specialties()
    for specialty in specialties:
        st.write(f"🔹 {specialty['description']}")

# Opción: Añadir Especialidad
elif menu == "Añadir Especialidad":
    st.subheader("Añadir Nueva Especialidad")
    new_description = st.text_input("Descripción de la especialidad")
    if st.button("Guardar Especialidad"):
        if add_specialty(new_description):
            st.success("Especialidad añadida con éxito")
        else:
            st.error("Error al añadir la especialidad")

# Opción: Ver Chefs
elif menu == "Ver Chefs":
    st.subheader("Lista de Chefs")
    chefs = get_chefs()
    for chef in chefs:
        st.write(f"👨‍🍳 {chef['name']} - {chef['expertise']} ⭐ {chef['rating']}")

# Opción: Añadir Chef
elif menu == "Añadir Chef":
    st.subheader("Añadir Nuevo Chef")
    name = st.text_input("Nombre del chef")
    expertise = st.text_input("Especialidad del chef")
    rating = st.number_input("Calificación (1-5)", min_value=1.0, max_value=5.0, step=0.1)
    if st.button("Guardar Chef"):
        if add_chef(name, expertise, rating):
            st.success("Chef añadido con éxito")
        else:
            st.error("Error al añadir el chef")
