import requests

BASE_URL = "http://127.0.0.1:8000/api"

# Obtener lista de usuarios
def get_users():
    try:
        response = requests.get(f"{BASE_URL}/users/users/?format=json")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error getting users: {e}")
        return []

# Crear un nuevo usuario
def create_user(name, email, phone):
    try:
        user_data = {
            "name": name,
            "email": email,
            "telephone": phone
        }
        response = requests.post(f"{BASE_URL}/users/users/", json=user_data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error creating user: {e}")
        return None

# Obtener especialidades de chefs
def get_specialties():
    try:
        response = requests.get(f"{BASE_URL}/specialties/specialties/?format=json")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error getting specialties: {e}")
        return []

# Obtener chefs por especialidad
def get_chefs_by_specialty(specialty_id):
    try:
        response = requests.get(f"{BASE_URL}/chefs/chefs/")
        response.raise_for_status()
        chefs = response.json()
        return [c for c in chefs if c['specialty'] == specialty_id]
    except requests.RequestException as e:
        print(f"Error getting chefs: {e}")
        return []

# Crear una reserva
def create_reservation(reservation_data):
    try:
        response = requests.post(f"{BASE_URL}/reservations/reservations/", json=reservation_data)
        response.raise_for_status()
        return {"success": True}
    except requests.RequestException as e:
        print(f"Error creating reservation: {e}")
        return {"success": False}
def get_chefs():
    """Obtiene la lista de chefs desde la API"""
    url = f"{BASE_URL}/chefs/chefs/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching chefs: {e}")
        return []

def get_reservations():
    """Obtiene la lista de reservas registradas"""
    url = f"{BASE_URL}/reservations/reservations/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching reservations: {e}")
        return []