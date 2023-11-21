import streamlit as st
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt

import pandas as pd

def main():
    df=pd.read_csv('data/lang_data.csv')

    st.dataframe(df)

    # 멀티셀렉트를 만들어서,
    # 컬럼이름 중에서 프로그래밍 언어를 보여주고,
    # 유저가 선택한 언어만 차트로 표시하려 한다.

    column_menu=df.columns[1:]
    choice_list = st.multiselect('언어를 선택하세요', options=column_menu)

    if len(choice_list) != 0 :
        # 유저가 선택한 언어의 수치를, 차트로 그린다.
        df_selected = df[choice_list]

        # 스트림릿에서 제공하는, 라인차트

        st.line_chart(data=df_selected)
        

        # 스트림릿에서 제공하는, 영역차트
        st.area_chart(data=df_selected)

        # 스트림릿에서 제공하는, 바차트
        st.bar_chart(data=df_selected)


        ### 2017년 4월부터 2018년 3월까지의 데이터를 
        ### 바차트로 나타내시오
        my_filter = (df['Week'] >='2017-04') & (df['Week'] <='2018-03')
        df_filter = df.loc[my_filter,]
        st.dataframe(df_filter)
        st.bar_chart(data=df_filter, x='Week')

        df_iris = pd.read_csv('data/iris.csv')

        # 두 컬럼간의관계를 표시하되.
        # 종 정보까지 표시하는 방법

        chart=alt.Chart(data=df_iris).mark_circle().encode(x='petal_length', y='petal_width', color='species')
        st.altair_chart(chart)

        # 위치정보를 가지고, 지도에 표시하는 방법
        # 스트림릿의 map 차트.

        df_location=pd.read_csv('data/location.csv', index_col=0)
        st.dataframe(df_location)
        st.map(data=df_location)


        ## plotly 차트 그리는 방법

        df_prog=pd.read_csv('data/prog_languages_data.csv', index_col=0)
        st.dataframe(df_prog)

        # 1. pie 차트
        chart2=px.pie(data_frame= df_prog, names= 'lang', values='Sum', title='각 언어별 파이차트')
        st.plotly_chart(chart2)

        # 2. bar 차트
        chart3=px.bar(data_frame=df_prog,x='lang', y='Sum')
        st.plotly_chart(chart3)

        # 정렬해서 보여주기.
        df_prog_sorted=df_prog.sort_values('Sum', ascending=0)
        chart4 = px.bar(data_frame=df_prog_sorted, x='lang', y='Sum')
        st.plotly_chart(chart4)



if __name__ == '__main__' :
    main()