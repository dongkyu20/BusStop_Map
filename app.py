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

all_city = p_df['LOC'] == '전국'
all_tmp = p_df[all_city]
all_count = all_tmp['COUNT']


city_lst = list(set(df['CITY']))
city_lst.sort()

picked = st.selectbox('Pick City', city_lst)
picked_city = df['CITY'] == picked
df_map = df[picked_city]

picked_tmp = p_df['LOC'] == picked
picked_t = p_df[picked_tmp]
picked_count = picked_t['COUNT']



# chart_df = pd.DataFrame({'CITY':['전국',picked],
#                              'COUNT':[all_count, picked_count],
#                              'DENSITY':['H', 'W']})

st.map(df_map)
# st.bar_chart(chart_df)

st.text_area(all_count)

