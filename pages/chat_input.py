import streamlit as st

# Title 작성
st.title("Chat Input 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

def save_history(prompt: str):
    st.session_state["history"].extend(
        [
            {"rule": "human", "content": prompt},
            {"rule": "ai", "content": f"저도 `{prompt}` 이 말을 좋아해요."},
        ]
    )


if "history" not in st.session_state:
    st.session_state["history"] = []

box = st.container(border=True, height=400)
prompt = st.chat_input("대화를 입력해주세요.")

if prompt:
    save_history(prompt)

for hisotry in st.session_state["history"]:
    with box.chat_message(hisotry["rule"]):
        st.write(hisotry["content"])
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과


def save_history(prompt: str):
    st.session_state["history"].extend(
        [
            {"rule": "human", "content": prompt},
            {"rule": "ai", "content": f"저도 `{prompt}` 이 말을 좋아해요."},
        ]
    )


if "history" not in st.session_state:
    st.session_state["history"] = []

box = st.container(border=True, height=400)
prompt = st.chat_input("대화를 입력해주세요.")

if prompt:
    save_history(prompt)

for hisotry in st.session_state["history"]:
    with box.chat_message(hisotry["rule"]):
        st.write(hisotry["content"])
