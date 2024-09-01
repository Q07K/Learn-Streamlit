import streamlit as st

# Title 작성
st.title("Number Slider 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

age = st.slider("당신의 나이는?", 0, 130, 25)
st.write("저는", age, "살 입니다.")
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

age = st.slider("당신의 나이는?", 0, 130, 25)
st.write("저는", age, "살 입니다.")
