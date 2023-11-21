import streamlit as st
import pandas as pd

def run_ead_app() :
    st.subheader('EDA 화면')
    df=pd.read_csv('data/iris.csv')
    st.dataframe(df)
    st.subheader('상관계수')
    st.dataframe(df.corr(numeric_only=True))