import streamlit as st

# Title 작성
st.title("Select Slider 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

value = st.select_slider(
    "숫자 선택",
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    (1),
)
st.write("내 선택:", value)

value = st.select_slider(
    "숫자 범위 선택",
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    (1, 4),
)
st.write("내 선택:", value)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

value = st.select_slider(
    "숫자 선택",
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    (1),
)
st.write("내 선택:", value)

value = st.select_slider(
    "숫자 범위 선택",
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    (1, 4),
)
st.write("내 선택:", value)
