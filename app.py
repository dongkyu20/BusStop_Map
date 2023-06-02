import streamlit as st
import pandas as pd

csv_file_path = 'Bus_stop_data.csv'

data = pd.read_csv(csv_file_path)
new_columns = ['NUM', 'NAME', 'LAT', 'LON', 'date', 'h_key', 'code', 'city', 'at']
df = data.rename(columns=dict(zip(data.columns, new_columns)))



st.text_area('South Korea')
dd = st.selectbox('pick city', ['아산시', '파주시'])
is_x = df['city'] == dd
df_map = df[is_x]
st.map(df_map)
