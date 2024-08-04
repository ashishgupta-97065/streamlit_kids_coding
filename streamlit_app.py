import streamlit as st
import numpy as np

if st.button("Restart"):
    st.rerun()

st.title("TEST RUN")

X1 = np.random.randint(low=0, high=10)

st.write(X1)

# Initialize session state variables
if 'count_value' not in st.session_state:
    st.session_state.count_value = X1

X2 = st.number_input("YOUR ANSWER:", step=1)

if st.button("check answer"):
    st.write("Actual answer: ", st.session_state.count_value)
    st.write("Your answer: ", X2)
    
    if X2==st.session_state.count_value:
        st.write("your are correct")
    else:
        st.write("your are incorrect")
    
    st.session_state.count_value = X1
