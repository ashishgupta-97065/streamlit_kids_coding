import streamlit as st
import numpy as np
import eval

a = st.number_input("a")
b = st.number_input("b")
operator = st.text_input("operator")
# expression = a + operator + b # simple string concatenation
# result = eval(expression)
# st.write(result)

if st.button("Restart"):
    st.rerun()

X1 = np.random.randint(low=0, high=10)

st.title("🎈 My new app")
st.write(X1)
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
