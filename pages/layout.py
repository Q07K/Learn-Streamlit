import streamlit as st

# Title 작성
st.title("Layout 구성")

# 코드 표시
st.subheader("코드")
code = '''
import streamlit as st

# Sidebar
with st.sidebar:
    st.text_input("input")


# 분할
col1, col2, col3 = st.columns(3)
col1.text_input("1")
col2.text_input("2")
col3.text_input("3")


# container
cont = st.container(border=True, height=100)
cont.button("버튼", use_container_width=True)


# 모달 상자
@st.dialog("입력")
def box():
    item = st.selectbox(
        "선택하세요.",
        ["사과", "바나나", "딸기"],
    )
    col1, col2 = st.columns(2)
    if col1.button("결과 확인", use_container_width=True):
        st.session_state["box"] = {"item": item}
        st.write(st.session_state["box"])

    if col2.button("닫기", use_container_width=True):
        st.rerun()


if st.button("모달 상자"):
    box()


# 확장
with st.expander("해설"):
    st.write(
        """
        1 + 1 = 2는 자연수의 기본 성질과 덧셈의 정의에 의해 성립하는 수학적 명제입니다.\n
        이는 일종의 공리로 받아들여지며, 우리가 일상에서 경험하는 것과 일치합니다.\n
        수학에서는 이러한 기본 개념들이 정리되어 더 복잡한 수학적 구조를 구축하는 데 사용됩니다.\n
    """
    )


# Tab
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
'''
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과


# Sidebar
with st.sidebar:
    st.text_input("input")


# 분할
col1, col2, col3 = st.columns(3)
col1.text_input("1")
col2.text_input("2")
col3.text_input("3")


# container
cont = st.container(border=True, height=100)
cont.button("버튼", use_container_width=True)


# 모달 상자
@st.dialog("입력")
def box():
    item = st.selectbox(
        "선택하세요.",
        ["사과", "바나나", "딸기"],
    )
    col1, col2 = st.columns(2)
    if col1.button("결과 확인", use_container_width=True):
        st.session_state["box"] = {"item": item}
        st.write(st.session_state["box"])

    if col2.button("닫기", use_container_width=True):
        st.rerun()


if st.button("모달 상자"):
    box()


# 확장
with st.expander("해설"):
    st.write(
        """
        1 + 1 = 2는 자연수의 기본 성질과 덧셈의 정의에 의해 성립하는 수학적 명제입니다.\n
        이는 일종의 공리로 받아들여지며, 우리가 일상에서 경험하는 것과 일치합니다.\n
        수학에서는 이러한 기본 개념들이 정리되어 더 복잡한 수학적 구조를 구축하는 데 사용됩니다.\n
    """
    )


# Tab
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
