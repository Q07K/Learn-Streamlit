import streamlit as st

# Title 작성
st.title("Time Input 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

t = st.time_input("알람 설정", value=None)
st.write("알람이 울릴 시간:", t)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

t = st.time_input("알람 설정", value=None)
st.write("알람이 울릴 시간:", t)
