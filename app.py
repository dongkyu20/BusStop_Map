import streamlit as st
import pandas as pd

csv_file_path1 = 'Bus_stop_data.csv'
csv_file_path2 = 'people.csv'

data = pd.read_csv(csv_file_path1)
people = pd.read_csv(csv_file_path2)

new_columns = ['NUM', 'NAME', 'LAT', 'LON', 'DATE', 'H_KEY', 'CODE', 'CITY', 'AT']
new_columns2 = ['loc', 
df = data.rename(columns=dict(zip(data.columns, new_columns)))



city_lst = list(set(df['city']))
city_lst.sort()

picked = st.selectbox('Pick City', city_lst)
picked_city = df['city'] == picked
df_map = df[picked_city]
st.map(df_map)

st.text_area('South Korea')

