import streamlit as st

def main() :
    st.title('웹 대시보드')

    st.header('이 영역은 헤더 영역') # 타이틀 보다 작음

    st.subheader('이 영역은 서브 헤더 영역')

    st.write('write 영역') # 텍스트보다 조금 큼

    st.text('text 영역')


    st.success('성공했을때의 메세지를 보여줄때')

    st.warning('경고 메세지를 보여줄때')

    st.info('정보성 메세지를 보여줄때')

    st.error('문제가 발생했음을 보여주고 싶을 때')

if __name__ == '__main__' :
    main()