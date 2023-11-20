import streamlit as st
import pandas as pd

# 버튼을 만들어 누르면 데이터 프레임을 나타나게 하기

def main():
    df=pd.read_csv('data/iris.csv')
    if st.button('데이터프레임 보기') :
        st.dataframe(df)

    name = 'Mike'
    if st.button('대문자') :
        st.subheader(name.upper())

    if st.button('소문자') :
        st.subheader(name.lower())

    # 라디오 버튼을 만드는 방법
    selceted=st.radio('정렬을 선택하세요.', ['오름차순 정렬', '내림차순 정렬'])
    if selceted =='오름차순 정렬' :
       st.dataframe(df.sort_values('petal_length', ascending=1))
    elif selceted =='내림차순 정렬' :
        st.dataframe(df.sort_values('petal_length', ascending=0))

    # 체크박스를 나타내는 방법
    if st.checkbox('데이터프레임 보이기/ 숨기기') :
        st.dataframe(df)
    else :
        st.write('')

    # 셀렉트박스 : 여러개중에 한개를 선택할 때
    language=['Python', 'Java', 'C', 'PHP', 'GO']
    my_choice=st.selectbox('좋아하는 언어를 선택하세요', language)
    st.text('저는 {}언어를 좋아합니다.'.format(my_choice))
    if my_choice == language[0] or my_choice == language[3] or my_choice==language[-1]:
        st.text('배우기 쉽습니다.')
    elif my_choice == language[1] or my_choice == language[2] :
        st.text('배우기 어렵습니다.')
    
    # 멀티셀렉트 : 여러개를 동시에 선택 가능
    selceted_list=st.multiselect('여러개 선택 가능',df.columns)

    if len(selceted_list) != 0 :
        st.dataframe(df[selceted_list])

    # 슬라이더
    selected_slider=st.slider('나이', 0, 100)
    st.text("제 나이는 "+str(selected_slider)+"살 입니다.")
    st.slider('데이터', 50, 200, step=10)
    st.slider('나이', 0, 100, value=32) # 초기값을 32으로 준다.
    st.slider('데이터',-0.5,2.7, step=0.1, value=1.0)

    with st.expander('상세 내용 보기') :
        st.text('상세 내용 입니다~~')
if __name__ == '__main__' :
    main()