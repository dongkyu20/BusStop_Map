import plotly.express as px
import streamlit as st
import pandas as pd

csv_file_path1 = 'Bus_stop_data.csv'
csv_file_path2 = 'people_re.csv'

data = pd.read_csv(csv_file_path1)
people = pd.read_csv(csv_file_path2, encoding='EUC-KR')

new_columns = ['NUM', 'NAME', 'LAT', 'LON', 'DATE', 'H_KEY', 'CODE', 'CITY', 'AT']
new_columns2 = ['지역', '인구수']

df = data.rename(columns=dict(zip(data.columns, new_columns)))
p_df = people.rename(columns=dict(zip(people.columns, new_columns2)))

bus_all_count = len(df) ## 전국 버스 정류장 수

people_all_city = p_df['지역'] == '전국'
people_all_count = p_df[people_all_city]  ## 전국의 인구 수

people_seoul_city = p_df['지역'] == '서울특별시'
people_seoul_count = p_df[people_seoul_city]  ## 서울의 인구 수

city_lst = list(set(df['CITY']))
city_lst.sort()  ## 셀렉트박스의 도시이름을 가나다 순으로 정렬

picked = st.selectbox('Pick City', city_lst)
picked_city = df['CITY'] == picked
df_map = df[picked_city]  ## 선택 도시의 버스 정류장 정보 추출

bus_picked_count = len(df_map)  ## 선택 도시의 버스 정류장 수

people_picked_tmp = p_df['지역'] == picked
people_picked_count = p_df[people_picked_tmp]  ## 선택 도시의 인구 수

bus_seoul = df['CITY'] == '서울특별시'
bus_seoul_city = df[bus_seoul]
bus_seoul_count = len(bus_seoul_city)  ## 서울의 버스 정류장 수

st.map(df_map)

fig1_df = pd.concat([people_all_count, people_seoul_count])
fig2_df = pd.concat([fig1_df, people_picked_count])

people_fig = px.bar(fig2_df, x='지역', y='인구수')

people = fig2_df['인구수']

people_all = people.iloc[0]
people_seoul = people.iloc[1]
people_picked = people.iloc[2]

density_all = int(bus_all_count) / int(people_all)
density_seoul = int(bus_seoul_count) / int(people_seoul)
density_picked = int(bus_picked_count) / int(people_picked)

density_df = pd.DataFrame([['전국', density_all],
                           ['서울특별시', density_seoul],
                           [picked, density_picked]], columns=['지역', '정류장 수 / 인구수'])

density_fig = px.bar(density_df, x='지역', y='정류장 수 / 인구수')

agree = st.checkbox('인구대비 정류장 수 그래프 (정류장 수 / 인구수)')

if agree:
    st.plotly_chart(density_fig)
else:
    st.plotly_chart(people_fig)
