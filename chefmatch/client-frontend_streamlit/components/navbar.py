import streamlit as st

def navbar(page_name, show_reservations=True, show_staff=True, show_logout=False):
    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown("[![Logo](https://via.placeholder.com/100)](/)") # Replace with your logo URL

    with col2:
        if show_reservations and page_name != "reservations":
            st.markdown("[Reservations](/reservations)", unsafe_allow_html=True)
        if show_staff and page_name != "staff":
            st.markdown("[Staff](/staff)", unsafe_allow_html=True)
        if show_logout:
            if st.button("Logout"):
                # Implement logout logic here
                st.write("Logged out")