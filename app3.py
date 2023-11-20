import streamlit as st
import pandas as pd

# 판다스의 데이터프레임을, 웹화면으로 보여주는 방법

def main():
    st.title('아이리스 꽃 데이터')
    df=pd.read_csv('data/iris.csv')
    st.dataframe(df)
    count=df['species'].nunique()
    st.write("아이리스 꽃의 종류는 총",count,"가지 입니다.")

if __name__ == '__main__' :
    main()