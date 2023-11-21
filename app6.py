import streamlit as st
import pandas as pd

def main():
    # 텍스트를 입력받는 방법
    user_name=st.text_input("이름을 입력하세요!")
    if user_name : 
        st.subheader('제 이름은 '+user_name+' 입니다.')
    st.text_input('이름을 입력하세요!', value='홍길동')
    st.text_input('이름을 입력하세요!', max_chars=5)
    st.text_input('이름을 입력하세요!', placeholder='홍길동')
    text=st.text_area('메세지를 입력하세요')
    st.text(text)

    # 숫자 입력 받는 방법
    st.number_input('출생년도를 입력하세요',)
    birth_year=st.number_input('출생년도를 입력하세요', 1900, 2023) # 최소, 최대값을 정해줘서 실수형형태로 나오지 않음
    st.text('제 출생년도는 ' + str(birth_year) + '입니다.')
    
    st.number_input('실수를 입력하세요.', -2.000, 100.000, step=0.005)

    # 날짜 입력받는 방법
    my_date=st.date_input('약속 날짜 입력')

    print(my_date)
    print(type(my_date))
    
    # 0000년00월00일 0요일 입니다. 라고 웹화면에 표시!

    st.text(my_date.strftime('%Y년 %m월 %d일 %A입니다.'))

    # 시간 입력 받는 방법
    my_time=st.time_input('약속 시간 선택')

    print(type(my_time))
    st.text(my_time.strftime('%H:%M 에 약속시간을 잡았습니다.'))

    # 비밀번호 입력받는 방법

    password=st.text_input('비밀번호 입력', type='password')

    print(password)

    # 색깔 입력
    color=st.color_picker('색을 선택하세요')
    st.text(color)
if __name__ == '__main__' :
    main()