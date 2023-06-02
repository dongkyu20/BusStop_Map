import streamlit as st
import pandas as pd

csv_file_path1 = 'Bus_stop_data.csv'
csv_file_path2 = 'people_re.csv'


data = pd.read_csv(csv_file_path1)
people = pd.read_csv(csv_file_path2, encoding='EUC-KR')


new_columns = ['NUM', 'NAME', 'LAT', 'LON', 'DATE', 'H_KEY', 'CODE', 'CITY', 'AT']
new_columns2 = ['LOC', 'COUNT']


df = data.rename(columns=dict(zip(data.columns, new_columns)))
p_df = people.rename(columns=dict(zip(people.columns, new_columns2)))





city_lst = list(set(df['CITY']))
city_lst.sort()

picked = st.selectbox('Pick City', city_lst)
picked_city = df['CITY'] == picked
df_map = df[picked_city]
st.map(df_map)

st.text_area('South Korea')

