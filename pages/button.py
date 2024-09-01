import streamlit as st


import streamlit as st

# Title 작성
st.title("Button 구현")

# 코드 표시
st.subheader("코드")
code = """
if "num" not in st.session_state:
    st.session_state["num"] = 0


def count_up():
    st.session_state["num"] += 1


def count_down():
    st.session_state["num"] -= 1


box = st.container(border=True)
box.write(st.session_state["num"])

col1, col2 = st.columns(2)
col1.button("➕ 버튼", on_click=count_up, use_container_width=True)
col2.button("➖ 버튼", on_click=count_down, use_container_width=True)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

if "num" not in st.session_state:
    st.session_state["num"] = 0


def count_up():
    st.session_state["num"] += 1


def count_down():
    st.session_state["num"] -= 1


box = st.container(border=True)
box.write(st.session_state["num"])

col1, col2 = st.columns(2)
col1.button("➕ 버튼", on_click=count_up, use_container_width=True)
col2.button("➖ 버튼", on_click=count_down, use_container_width=True)
