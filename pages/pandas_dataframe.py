import streamlit as st
import pandas as pd
import numpy as np

# Title 작성
st.title("Pandas DataFrame")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(50, 20), columns=(f"col {i}" for i in range(20))
)

st.dataframe(df)

"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

df = pd.DataFrame(
    np.random.randn(50, 20), columns=(f"col {i}" for i in range(20))
)

st.dataframe(df)
