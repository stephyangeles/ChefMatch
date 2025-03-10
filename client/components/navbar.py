import streamlit as st

def navbar(page_name, show_reservations=True, show_staff=True, show_logout=False):
    
    st.markdown("""
    <style>
    .nav-buttons {
        text-align: center;
        margin-top: 10px;
    }
    
    .nav-buttons a {
        background-color: #fe0000;
        border: 2px solid white;
        border-radius: 20px;
        padding: 8px 16px;
        color: white;
        font-weight: bold;
        text-decoration: none;
        margin-left: 5%;  
        margin-right: 5%;
        display: inline-block;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    .nav-buttons a:hover {
        background-color: white;
        color: #fe0000;
        border: 2px solid #fe0000;
    }
    </style>
    """, unsafe_allow_html=True)

    
    col1, col2 = st.columns([1, 3])

   
    with col1:
        st.image("client/assets/logos/ChefMatch-horiz-blanco.png", use_container_width=True)

   
    with col2:
        nav_html = "<div class='nav-buttons'>"
        if show_reservations and page_name != "reservations":
            nav_html += "<a href='#reservations'>Reservations</a>"
        if show_staff and page_name != "staff":
            nav_html += "<a href='#staff'>Staff</a>"
        if show_logout:
            nav_html += "<a href='#logout'>Logout</a>"
        nav_html += "</div>"
        st.markdown(nav_html, unsafe_allow_html=True)
