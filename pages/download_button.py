import streamlit as st

# Title 작성
st.title("Download Button 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

value = st.text_input("Input")
st.download_button("Download Text", value)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

value = st.text_input("Input")
st.download_button("Download Text", value)
