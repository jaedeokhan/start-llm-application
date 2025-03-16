import streamlit as st

from dotenv import load_dotenv
from llm import get_ai_message

st.set_page_config(page_title="소득세 챗봇", page_icon="🐻")

st.title("🐻 소득세 챗봇")
st.caption("소득세에 관련된 모든것을 답해드립니다!")

load_dotenv()

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

# session 저장 리스트 출력
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message['content'])    


# 메시지 입력 및 session 저장
if user_message := st.chat_input(placeholder="소득세에 관련한 내용들을 말씀해주세요!"):
    with st.chat_message("user"):
        st.write(user_message)
    st.session_state.message_list.append({"role":"user", "content": user_message})

    with st.spinner("답변을 생성중입니다."):
        ai_message = get_ai_message(user_message)
        with st.chat_message("ai"):
            st.write(ai_message)
        st.session_state.message_list.append({"role":"ai", "content": ai_message})

