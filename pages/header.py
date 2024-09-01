import streamlit as st

# Title 작성
st.title("Header 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

st.header("Header 작성 예시입니다.")
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

st.header("Header 작성 예시입니다.")
