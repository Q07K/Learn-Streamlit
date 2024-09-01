import streamlit as st

# Title 작성
st.title("Feedback 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

value = st.selectbox("선택", ["faces", "stars", "thumbs"])

selected = st.feedback(value)
if selected is not None:
    st.write(selected)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

value = st.selectbox("선택", ["faces", "stars", "thumbs"])

selected = st.feedback(value)
if selected is not None:
    st.write(selected)
