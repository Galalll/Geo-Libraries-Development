import streamlit as st
import leafmap.foliumap as lf
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium


st.set_page_config(
    page_title="GeoTools",
    page_icon="👋",
    layout="wide",
)
st.write("# Welcome to My GeoTools Project 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    ## My Name is Abdelrahman Mohamed Galal.
    ### This is my Demo For GeoTools Project that I made as Finall Assessment for my course 
"""
)