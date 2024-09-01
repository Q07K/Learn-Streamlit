import streamlit as st
from streamlit_object import page_button

st.set_page_config(page_title="asdasd App", layout="wide")
st.header("Streamlit 실습", divider=True)
st.subheader("기본 구현")

basic = st.container(border=True)

# Text
basic.write("**Text**")
basic_row1 = basic.columns(4)
page_button(
    field=basic_row1,
    idx=0,
    path="pages/title.py",
    label="Title",
    icon=None,
)
page_button(
    field=basic_row1,
    idx=1,
    path="pages/header.py",
    label="Header",
    icon=None,
)
page_button(
    field=basic_row1,
    idx=2,
    path="pages/subheader.py",
    label="Sub Header",
    icon=None,
)
page_button(
    field=basic_row1,
    idx=3,
    path="pages/markdown.py",
    label="Markdown",
    icon=None,
)

# Input
basic.write("**Input**")
basic_row2 = basic.columns(4)
page_button(
    field=basic_row2,
    idx=0,
    path="pages/button.py",
    label="Button",
    icon="🕹️",
)
page_button(
    field=basic_row2,
    idx=1,
    path="pages/feedback.py",
    label="Feedback",
    icon="⭐",
)
page_button(
    field=basic_row2,
    idx=2,
    path="pages/download_button.py",
    label="Download",
    icon="💾",
)
page_button(
    field=basic_row2,
    idx=3,
    path="pages/from_button.py",
    label="From",
    icon="📨",
)
page_button(
    field=basic_row2,
    idx=0,
    path="pages/check_box.py",
    label="Check Box",
    icon="✔️",
)
page_button(
    field=basic_row2,
    idx=1,
    path="pages/toggle.py",
    label="Toggle",
    icon="🎚️",
)
page_button(
    field=basic_row2,
    idx=2,
    path="pages/radio_button.py",
    label="Radio",
    icon="🔘",
)
page_button(
    field=basic_row2,
    idx=3,
    path="pages/select_button.py",
    label="Select",
    icon="👉",
)

basic_row2 = basic.columns(3)
page_button(
    field=basic_row2,
    idx=0,
    path="pages/multi_select.py",
    label="Multi Select",
    icon="🔠",
)
page_button(
    field=basic_row2,
    idx=1,
    path="pages/select_slider.py",
    label="Select Slider",
    icon="🎚",
)
page_button(
    field=basic_row2,
    idx=2,
    path="pages/color_picker.py",
    label="Color Picker",
    icon="🎨",
)

basic_row2 = basic.columns(2)
page_button(
    field=basic_row2,
    idx=0,
    path="pages/number_input.py",
    label="Number",
    icon="🔢",
)
page_button(
    field=basic_row2,
    idx=1,
    path="pages/number_slider.py",
    label="Slider",
    icon="🎚",
)

basic_row2 = basic.columns(2)
page_button(
    field=basic_row2,
    idx=0,
    path="pages/date_input.py",
    label="Date",
    icon="📆",
)
page_button(
    field=basic_row2,
    idx=1,
    path="pages/time_input.py",
    label="Time",
    icon="🕒",
)

basic_row2 = basic.columns(3)
page_button(
    field=basic_row2,
    idx=0,
    path="pages/text_input.py",
    label="Text Input",
    icon="✏️",
)
page_button(
    field=basic_row2,
    idx=1,
    path="pages/text_area.py",
    label="Text Area",
    icon="📝",
)
page_button(
    field=basic_row2,
    idx=2,
    path="pages/chat_input.py",
    label="Chat Input",
    icon="🗣️",
)

basic_row2 = basic.columns(2)
page_button(
    field=basic_row2,
    idx=0,
    path="pages/upload.py",
    label="File Upload",
    icon="📤",
)
page_button(
    field=basic_row2,
    idx=1,
    path="pages/camera.py",
    label="Camera",
    icon="📸",
)

# Data
basic.write("**Data**")
basic_row3 = basic.columns(2)
page_button(
    field=basic_row3,
    idx=0,
    path="pages/pandas_dataframe.py",
    label="Pandas",
    icon="📅",
)
page_button(
    field=basic_row3,
    idx=1,
    path="pages/matplotlib_figure.py",
    label="Matplotlib",
    icon="📊",
)

# 기타
basic.write("**ETC**")
basic_row4 = basic.columns(4)
page_button(
    field=basic_row4,
    idx=0,
    path="pages/callout_messages.py",
    label="상태 메시지",
    icon="💻",
)
page_button(
    field=basic_row4,
    idx=1,
    path="pages/progress.py",
    label="Progress",
    icon="⌛",
)
page_button(
    field=basic_row4,
    idx=2,
    path="pages/stream.py",
    label="Stream",
    icon="🤖",
)
page_button(
    field=basic_row4,
    idx=3,
    path="pages/layout.py",
    label="Layout",
    icon="🪟",
)

#
st.subheader("다양한 기능 구현")
hard = st.container(border=True)
hard_row = hard.columns(3)
page_button(
    field=hard_row,
    idx=0,
    path="pages/login.py",
    label="Login",
    icon="🗝️",
)
page_button(
    field=hard_row,
    idx=1,
    path="pages/chat.py",
    label="Chat Bot",
    icon="🤖",
)
page_button(
    field=hard_row,
    idx=2,
    path="pages/student_management.py",
    label="교육 관리",
    icon="🎓",
)
