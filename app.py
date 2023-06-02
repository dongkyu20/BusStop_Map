import streamlit as st
import pandas as pd

csv_file_path = 'Bus_stop_data.csv'

data = pd.read_csv(csv_file_path)
new_columns = ['NUM', 'NAME', 'LAT', 'LON', 'date', 'h_key', 'code', 'city', 'at']
df = data.rename(columns=dict(zip(data.columns, new_columns)))


city_lst = list(set(df['city']))
city_lst.sort()

st.text_area('South Korea')
picked = st.selectbox('Pick City', city_lst)
picked_city = df['city'] == picked
df_map = df[picked_city]
st.map(df_map)
