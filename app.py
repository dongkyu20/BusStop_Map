import streamlit as st
import pandas as pd

csv_file_path = 'Bus_stop_data.csv'

data = pd.read_csv(csv_file_path)
pd.DataFrame(data, columns = ['NUM', 'NAM', 'lat', 'lon', 'date', 'h_key', 'code', 'city', 'at'])

st.map(data)
