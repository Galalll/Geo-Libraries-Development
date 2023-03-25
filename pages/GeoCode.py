import time 
import base64

import streamlit as st
import pandas as pd 
import geopandas as gpd 

import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import leafmap.foliumap as leafmap
import json


def geocode_address(address):
    locator = Nominatim(user_agent="myGeocoder")
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
    location = geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


def display_map(lat, lon , address):
    m = leafmap.Map()
    if lat and lon:
        m.add_marker(location=[lat, lon], popup=f"{address}")
        # m.add_marker
        # m.center = (lat, lon)
    return m.to_streamlit(height=500)


def download_geojson(df):
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
    geojson_str = gdf.to_json()
    b64 = base64.b64encode(geojson_str.encode()).decode()
    href = f'<a href="data:application/json;base64,{b64}" download="geocoded_data.geojson">Download GeoJSON. File</a>'
    return href


def main():
    st.title("Geocoding App.")
    st.write("## This page will allow you to search for any contry and download GeoJson file includes its location ")
    st.markdown("Enter an address to search for")

    address = st.text_input("Enter an address")

    if address:
        with st.spinner('Geocoding address...'):
            lat, lon = geocode_address(address)
            time.sleep(3)

        if lat and lon:
            # st.success(f"Location found: {lat}, {lon}")
            st.markdown(download_geojson(pd.DataFrame({'latitude': [lat], 'longitude': [lon]})), unsafe_allow_html=True)
            st.write(display_map(lat, lon,address))
        else:
            st.error("Could not find location for entered address")

if __name__ == "__main__":
    main()