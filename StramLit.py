import streamlit as st
import geopandas as gpd
import leafmap.foliumap as lf

uploaded_file = st.file_uploader("Choose GeoJson a file",accept_multiple_files=False,type='geojson')
if uploaded_file != None :
    gjasonfile=gpd.read_file (uploaded_file).to_crs("EPSG:3857")
    buffered = gjasonfile.head(5)

    buffered["geometry"] = gjasonfile["geometry"].head(5).buffer(500)
    m=lf.Map()
    m.add_gdf(buffered)
    m.add_gdf(gjasonfile.head(5))
    m.to_streamlit(height=500)
    
