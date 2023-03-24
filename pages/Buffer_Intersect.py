import streamlit as st
import geopandas as gpd
import leafmap.foliumap as lf

uploaded_file = st.file_uploader("Choose First GeoJson a file",accept_multiple_files=False,type='geojson')
uploaded_file2 = st.file_uploader("Choose Second GeoJson a file",accept_multiple_files=False,type='geojson')
BufferValue=st.text_input("inter your Buffer value in meters")

if uploaded_file != None and uploaded_file2 != None and BufferValue:
    BufferValue=int(BufferValue)
    gjasonfile=gpd.read_file (uploaded_file).to_crs("EPSG:3857")
    gjasonfile2=gpd.read_file (uploaded_file2).to_crs("EPSG:3857")
    buffered = gjasonfile
    buffered2 = gjasonfile2
    buffered["geometry"] = gjasonfile["geometry"].buffer(BufferValue)
    buffered2["geometry"] = gjasonfile2["geometry"].buffer(BufferValue)
    intersection = gpd.overlay(buffered, buffered2, how='intersection')
    
    m=lf.Map()
    m.add_gdf(intersection)
    m.add_gdf(gjasonfile)
    m.add_gdf(gjasonfile2)
    m.add_gdf(buffered)
    m.add_gdf(buffered2)
    m.to_streamlit(height=500)

