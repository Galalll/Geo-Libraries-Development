import streamlit as st
import leafmap.foliumap as lf
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium
st.title("Drawing App. ")
st.write("## This page will allow you to Draw any feature and download it as GeoJson file. ")
m = folium.Map(location=[39.949610, -75.150282], zoom_start=5)
drawing = Draw(export=True,filename="drawn_shape.geojson")
drawing.add_to(m)
c1, c2 = st.columns(2)
with c1:
    output = st_folium(m, width=900, height=500)

with c2:
    st.write(output)