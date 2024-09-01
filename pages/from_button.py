import streamlit as st

# Title 작성
st.title("From Button 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

form = st.form(key="my_from")
text_input = form.text_input("input")
submit_button = form.form_submit_button()

if submit_button:
    st.write(f"{text_input = }")
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

form = st.form(key="my_from")
text_input = form.text_input("input")
submit_button = form.form_submit_button()

if submit_button:
    st.write(f"{text_input = }")
