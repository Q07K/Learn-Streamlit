import streamlit as st

# Title 작성
st.title("Toggle 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

on = st.toggle("스위치")

if on:
    st.write("On")
else:
    st.write("Off")
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

on = st.toggle("스위치")

if on:
    st.write("On")
else:
    st.write("Off")
