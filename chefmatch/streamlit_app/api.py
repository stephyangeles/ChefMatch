import requests
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000"

def get_specialties():
    try:
        response = requests.get(f"{API_BASE_URL}/specialties/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching specialties: {e}")
        return []

def get_chefs_by_specialty(specialty_id):
    try:
        response = requests.get(f"{API_BASE_URL}/chefs/?specialty={specialty_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching chefs: {e}")
        return []