import streamlit as st
import json


def data():
    if (
        "API-KEY" in st.session_state
        and st.session_state["API-KEY"] is not None
    ):
        api_key = st.session_state["API-KEY"].read()
        result = json.loads(api_key.decode("utf-8"))
        return result
    else:
        st.error("Enter API KEY")


with st.sidebar:

    st.header("Google API Key")
    st.file_uploader(
        "Google API Key",
        label_visibility="hidden",
        type="json",
        key="API-KEY",
    )
if st.button("test"):
    print(st.session_state["API-KEY"])
    d = data()
    print(d)
