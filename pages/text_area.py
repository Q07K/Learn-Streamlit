import streamlit as st

# Title 작성
st.title("Text Area 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

txt = st.text_area("Text Input")
st.write(f"{len(txt)} 자")
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

txt = st.text_area("Text Input")
st.write(f"{len(txt)} 자")
