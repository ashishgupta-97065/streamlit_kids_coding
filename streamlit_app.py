import streamlit as st
import numpy as np

if st.button("Restart"):
    st.rerun()

st.title("TEST RUN")

X1 = np.random.randint(low=0, high=10)

st.write(X1)

if st.button("PRINT"):
    st.write(X1)



# # import eval

# # a = st.number_input("a")
# # b = st.number_input("b")
# # operator = st.text_input("operator")
# # # expression = a + operator + b # simple string concatenation
# # # result = eval(expression)
# # # st.write(result)



# X1 = np.random.randint(low=0, high=10)

# st.title("🎈 My new app")
# st.write(X1)
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )
