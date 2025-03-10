import requests
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000/api"  # Asegurar que coincida con el backend

def get_specialties():
    """Obtiene la lista de especialidades desde la API."""
    try:
        response = requests.get(f"{API_BASE_URL}/specialties/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching specialties: {e}")
        return []

def get_chefs_by_specialty(specialty_id):
    """Obtiene los chefs que pertenecen a una especialidad específica."""
    try:
        response = requests.get(f"{API_BASE_URL}/chefs/?specialty_id={specialty_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching chefs: {e}")
        return []

def create_reservation(reservation_data):
    """Envía una nueva reserva al backend."""
    try:
        response = requests.post(f"{API_BASE_URL}/reservations/", json=reservation_data)
        response.raise_for_status()
        
        if response.status_code == 201:
            return {"success": True, "message": "🎉 Reservation confirmed!"}
        else:
            return {"success": False, "message": "❌ Unexpected response from server."}
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error creating reservation: {e}")
        return {"success": False, "message": str(e)}
