import streamlit as st

def get_page():
    query_params = st.experimental_get_query_params()
    if "page" in query_params:
        return query_params["page"][0]
    return "main"
