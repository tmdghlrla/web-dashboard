import streamlit as st
import pandas as pd

# 이미지 / 동영상을 화면에 보여주기

from PIL import Image

def main():
    img = Image.open('data/image_03.jpg')
    
    st.image(img)

    st.image(img, use_column_width=True)
    img_url='https://newsimg.sedaily.com/2023/10/12/29VXIATO1W_16.jpeg'
    st.image(img_url)

    # 동영상

    video_file=open('data/video1.mp4', 'rb') # mode='rb' 바이트 타입으로 읽어 온다.
    st.video(video_file)

if __name__ == '__main__' :
    main()