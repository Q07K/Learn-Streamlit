import streamlit as st

# Title 작성
st.title("Login 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

# 로그인 가능한 계정 및 비밀번호 목록
users = {
    "test1@test.com": "1234",
    "test2@test.com": "5678",
}

box = st.container(border=True)

email = box.text_input("Email")
password = box.text_input("Password", type="password")

_, col, _ = box.columns(3)

if col.button("submit", use_container_width=True):
    if not users.get(email, False):
        st.error("사용할 수 없는 계정입니다.")
    elif users[email] != password:
        st.error("비밀번호가 틀렸습니다.")
    else:
        st.session_state["flag"] = True


if "flag" in st.session_state and st.session_state["flag"]:
    st.success("로그인 성공")
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

# 로그인 가능한 계정 및 비밀번호 목록
users = {
    "test1@test.com": "1234",
    "test2@test.com": "5678",
}

box = st.container(border=True)

email = box.text_input("Email")
password = box.text_input("Password", type="password")

_, col, _ = box.columns(3)

if col.button("submit", use_container_width=True):
    if not users.get(email, False):
        st.error("사용할 수 없는 계정입니다.")
    elif users[email] != password:
        st.error("비밀번호가 틀렸습니다.")
    else:
        st.session_state["flag"] = True


if "flag" in st.session_state and st.session_state["flag"]:
    st.success("로그인 성공")
