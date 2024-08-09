import streamlit as st
import numpy as np

if st.button("Refresh"):
  st.cache_resource.clear()
  st.rerun()

st.title("This is a maths Sats test")
st.write("please enter you answer here")
n1=np.random.randint(low=20,high=30)
n2=np.random.randint(low=50,high=100)
s=n1+n2

if 'answer' not in st.session_state:
  # st.write("inside session creation:")
  st.session_state.answer = s
  # st.write("session answer:",s)


st.write("First number is " , n1)
st.write("Second number is " , n2)
# st.write("The first sum is" , s)      
a=st.number_input(" Enter your answer",step=1)


if st.button("check your answer"):
  ans = st.session_state.answer
  st.write("Actual Answer: ", ans)
  st.write("Your Answer: ", a)
  if a==ans:
    st.write( " YAY YOU ARE CORRRRRRRREEEEEECCCCCCTTTTTTTTTTTTTTTTTT")
  else:
    st.write(" YOU GET A RED CAAAAAAAAARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRD")
  st.session_state.answer = s
