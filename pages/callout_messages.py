import streamlit as st

# Title 작성
st.title("상태 메시지 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

st.success("This is a success message!", icon="✅")
st.info("This is a purely informational message", icon="ℹ️")
st.warning("This is a warning", icon="⚠️")
st.error("This is an error", icon="🚨")
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

st.success("This is a success message!", icon="✅")
st.info("This is a purely informational message", icon="ℹ️")
st.warning("This is a warning", icon="⚠️")
st.error("This is an error", icon="🚨")
