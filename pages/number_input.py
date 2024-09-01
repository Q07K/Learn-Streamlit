import streamlit as st

# Title 작성
st.title("Number Input 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

number = st.number_input(
    "숫자를 입력해주세요.",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.5,
    format="%0.1f",
)
st.write("선택된 숫자는 ", number)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

number = st.number_input(
    "숫자를 입력해주세요.",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.5,
    format="%0.1f",
)
st.write("선택된 숫자는 ", number)
