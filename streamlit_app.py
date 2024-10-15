import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
import os

# Streamlit 앱 설정
st.title('텍스트 요약 앱')
st.sidebar.header('설정')

# OpenAI API 키 입력
oai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# 텍스트 입력란
text_input = st.text_area("요약할 텍스트를 입력하세요:")

# 요약 버튼
yes_summary = st.button("요약하기")

# 요약 기능 구현
if yes_summary:
    if not oai_api_key:
        st.error("먼저 OpenAI API 키를 입력해주세요.")
    elif not text_input:
        st.error("요약할 텍스트를 입력해주세요.")
    else:
        # 환경 변수에 OpenAI API 키 설정
        os.environ["OPENAI_API_KEY"] = oai_api_key
        
        # OpenAI 모델 설정
        llm = ChatOpenAI(model_name="gpt-4o-mini")
        prompt = PromptTemplate(input_variables=["text"], template="다음 텍스트를 요약하세요: {text}")
        
        # 입력 텍스트를 요약
        formatted_prompt = prompt.format(text=text_input)
        message = HumanMessage(content=formatted_prompt)
        summary = llm([message])
        
        # 요약 결과 출력
        st.subheader("요약 결과:")
        st.write(summary.content)