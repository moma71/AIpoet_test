
import streamlit as st
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI()

st.title('인공지능시인')

content = st.text_input("시의 주제를 제시해 주세요")



if st.button(content +"로 시를 작성해주세요"):
    with st.spinner('시 작성 중...'):
        result =chat_model.predict(content+"에 대한 시를 써줘")
        st.write(result)
    


# 

# print(result)