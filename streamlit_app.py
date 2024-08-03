import streamlit as st
import numpy as np

a = input('enter a value')
b = input('enter a value') 
op = input('enter an operand')
expression = a + op + b # simple string concatenation
result = eval(expression)


if st.button("Restart"):
    st.rerun()

X1 = np.random.randint(low=0, high=10)

st.title("🎈 My new app")
st.write(X1)
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
