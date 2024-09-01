import streamlit as st

# Title 작성
st.title("Camera 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
