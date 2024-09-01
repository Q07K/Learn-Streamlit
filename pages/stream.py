import streamlit as st
import time

# Title 작성
st.title("Color Picker 구현")

# 코드 표시
st.subheader("코드")
code = '''
import streamlit as st
import time

text = """
#### 1절

동해물과 백두산이 마르고 닳도록

하느님이 보우하사 우리나라 만세

무궁화 삼천리 화려 강산

대한 사람 대한으로 길이 보전하세


#### 2절

남산 위에 저 소나무 철갑을 두른 듯

바람 서리 불변함은 우리 기상일세

무궁화 삼천리 화려 강산

대한 사람 대한으로 길이 보전하세


#### 3절

가을 하늘 공활한데 높고 구름 없이

밝은 달은 우리 가슴 일편단심일세

무궁화 삼천리 화려 강산

대한 사람 대한으로 길이 보전하세


#### 4절

이 기상과 이 맘으로 충성을 다하여

괴로우나 즐거우나 나라 사랑하세

무궁화 삼천리 화려 강산

대한 사람 대한으로 길이 보전하세
"""


def stream_data():
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.1)


if st.button("실행"):
    st.header("애국가")
    st.write_stream(stream_data)
'''
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

text = """
#### 1절

동해물과 백두산이 마르고 닳도록

하느님이 보우하사 우리나라 만세

무궁화 삼천리 화려 강산

대한 사람 대한으로 길이 보전하세


#### 2절

남산 위에 저 소나무 철갑을 두른 듯

바람 서리 불변함은 우리 기상일세

무궁화 삼천리 화려 강산

대한 사람 대한으로 길이 보전하세


#### 3절

가을 하늘 공활한데 높고 구름 없이

밝은 달은 우리 가슴 일편단심일세

무궁화 삼천리 화려 강산

대한 사람 대한으로 길이 보전하세


#### 4절

이 기상과 이 맘으로 충성을 다하여

괴로우나 즐거우나 나라 사랑하세

무궁화 삼천리 화려 강산

대한 사람 대한으로 길이 보전하세
"""


def stream_data():
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.1)


if st.button("실행"):
    st.header("애국가")
    st.write_stream(stream_data)
