import streamlit as st
import pandas as pd
import api  # Importa el módulo API
from components.navbar import navbar
from components.footer import footer

def chef_agenda_page():
    navbar("chef_agenda", show_reservations=False, show_staff=False, show_logout=True)
    st.title("📅 Chef's Agenda")

    # Obtener datos de la API
    chefs = api.get_chefs()
    reservations = api.get_reservations()

    if not chefs:
        st.warning("⚠ No chefs found.")
        return

    if not reservations:
        st.warning("⚠ No reservations found.")
        return

    # Crear diccionarios para mapear IDs con nombres
    chef_dict = {chef["id"]: chef["name"] for chef in chefs}
    users = [{"id": 1, "name": "Tef"}, {"id": 2, "name": "Andrés"}]  # Simulación de usuarios
    user_dict = {user["id"]: user["name"] for user in users}

    # Convertir datos en DataFrame
    df = pd.DataFrame(reservations)
    df["chef"] = df["chef"].map(chef_dict)
    df["user"] = df["user"].map(user_dict)
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%d-%m-%Y")

    # Estilo de la tabla más grande con márgenes
    st.markdown("""
        <style>
            .big-table-container {
                margin: 30px 0px;
                padding: 10px;
            }
            .stDataFrame {
                font-size: 16px !important;
                color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Mostrar la tabla con botones de editar/eliminar
    st.write("### 📌 Reservations Overview")
    for index, row in df.iterrows():
        with st.container():
            col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 1, 1])
            col1.write(row["date"])
            col2.write(row["user"])
            col3.write(row["chef"])
            col4.write(row["location"])
            edit_btn = col5.button("✏️", key=f"edit_{index}")
            delete_btn = col6.button("❌", key=f"delete_{index}")

            if delete_btn:
                api.delete_reservation(row["id"])
                st.experimental_rerun()

            if edit_btn:
                open_edit_modal(row)

    footer()

def open_edit_modal(reservation):
    """Abre un modal para editar una reserva."""
    with st.expander("✏️ Edit Reservation", expanded=True):
        new_date = st.text_input("Date", reservation["date"])
        new_user = st.selectbox("User", ["Tef", "Andrés"], index=0)
        new_chef = st.selectbox("Chef", ["Chef A", "Chef B"], index=0)
        new_location = st.text_input("Location", reservation["location"])

        save_btn = st.button("💾 Save Changes")
        if save_btn:
            api.update_reservation(reservation["id"], new_date, new_user, new_chef, new_location)
            st.success("Reservation updated successfully!")
            st.experimental_rerun()

if __name__ == "__main__":
    chef_agenda_page()
