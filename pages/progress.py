import streamlit as st
import time

# Title 작성
st.title("Color Picker 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st
import time

with st.spinner("로딩중..."):
    time.sleep(3)

progress_text = "잠시 기다려주세요."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()
st.success("Done!")
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

with st.spinner("로딩중..."):
    time.sleep(3)

progress_text = "잠시 기다려주세요."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()
st.success("Done!")
