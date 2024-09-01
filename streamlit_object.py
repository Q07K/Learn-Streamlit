import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def page_button(
    field: list[DeltaGenerator],
    idx: int,
    path: str,
    label: str,
    icon: str,
) -> None:
    with field[idx].container(border=True):
        st.page_link(
            path,
            label=f"**{label}**",
            icon=icon,
            use_container_width=True,
        )
