import streamlit as st
from app8_home import run_home_app
from app8_eda import run_ead_app
from app8_ml import run_ml_app
def main():
    st.title('파일 분리 앱')

    menu=['Home', 'EDA', 'ML']

    choice = st.sidebar.selectbox('메뉴 선택', options=menu)

    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        run_ead_app()
    elif choice == menu[2] :
        run_ml_app()
        

    

if __name__ == '__main__' :
    main()