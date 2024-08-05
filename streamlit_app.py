import streamlit as st
import numpy as np


if st.button("Restart"):
    st.caching.clear_cache()
    st.rerun()
    

st.title("TEST RUN")

X1 = np.random.randint(low=0, high=10)

st.write(X1)

# Initialize session state variables
if 'answer' not in st.session_state:
    st.session_state.answer = X1

X2 = st.number_input("YOUR ANSWER:", step=1)

if st.button("check answer"):
    a = st.session_state.answer
    st.write("Actual answer: ", a)
    st.write("Your answer: ", X2)
    
    if X2==a:
        st.write("your are correct")
    else:
        st.write("your are incorrect")
    
    st.session_state.answer = X1
