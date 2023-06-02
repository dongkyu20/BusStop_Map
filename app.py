import streamlit as st
import pandas as pd

csv_file_path = 'Bus_stop_data.csv'

data = pd.read_csv(csv_file_path)
new_columns = ['NUM', 'NAME', 'LAT', 'LON', 'date', 'h_key', 'code', 'city', 'at']
df = data.rename(columns=dict(zip(data.columns, new_columns)))

df_set = list(set(df['NAME']))

city_lst = list(set(df_set['city']))
city_lst.sort()

picked = st.selectbox('Pick City', city_lst)
picked_city = df['city'] == picked
df_map = df[picked_city]
st.map(df_map)

st.text_area('South Korea')

