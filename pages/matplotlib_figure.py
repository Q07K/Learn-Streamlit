import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title 작성
st.title("Matplotlib")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
