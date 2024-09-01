import datetime
import streamlit as st

# Title 작성
st.title("Date Input 구현")

# 코드 표시
st.subheader("코드")
code = """
import datetime
import streamlit as st

d = st.date_input("생일을 입력해주세요.", datetime.date(2019, 7, 6))
st.write("생일:", d)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

d = st.date_input("생일을 입력해주세요.", datetime.date(2019, 7, 6))
st.write("생일:", d)
