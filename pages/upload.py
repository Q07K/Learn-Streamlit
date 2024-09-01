import streamlit as st

# Title 작성
st.title("File Upload 구현")

# 코드 표시
st.subheader("코드")
code = """
data = st.file_uploader("txt 파일을 선택해주세요.", type="txt")
if data:
    st.write(f"**파일 이름:** `{data.name}`")
    st.write("**내용:**")

    byte_data = data.read()
    st.write(f"{byte_data.decode('utf-8')}")
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

data = st.file_uploader("txt 파일을 선택해주세요.", type="txt")
if data:
    st.write(f"**파일 이름:** `{data.name}`")
    st.write("**내용:**")

    byte_data = data.read()
    st.write(f"{byte_data.decode('utf-8')}")
