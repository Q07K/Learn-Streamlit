import streamlit as st

# Title 작성
st.title("Check Box 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
