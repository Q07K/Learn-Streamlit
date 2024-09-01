import streamlit as st

# Title 작성
st.title("Text Input 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

title = st.text_input("노래 제목", "진격의 방탄")
st.write("노래 제목: ", title)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

title = st.text_input("노래 제목", "진격의 방탄")
st.write("노래 제목: ", title)
