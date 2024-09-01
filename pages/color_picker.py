import streamlit as st

# Title 작성
st.title("Color Picker 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

color = st.color_picker("색상을 선택해주세요.", "#00f900")
st.write(color)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

color = st.color_picker("색상을 선택해주세요.", "#00f900")
st.write(color)
