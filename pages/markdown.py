import streamlit as st

# Title 작성
st.title("Markdown 구현")

# 코드 표시
st.subheader("코드")
code = '''
import streamlit as st

st.markdown(
    """
## Header
# H1
## H2
### H3
#### H4
##### H5
###### H6

## List
- <내용>
    - <내용>
        - <내용>
- <내용>
- <내용>


1. <내용>
1. <내용>
1. <내용>

## 인용구
> ### <내용>
> 1. <내용>
> 1. <내용>
"""
)
'''
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과
st.markdown(
    """
## Header
# H1
## H2
### H3
#### H4
##### H5
###### H6

## List
- <내용>
    - <내용>
        - <내용>
- <내용>
- <내용>


1. <내용>
1. <내용>
1. <내용>

## 인용구
> ### <내용>
> 1. <내용>
> 1. <내용>
"""
)
