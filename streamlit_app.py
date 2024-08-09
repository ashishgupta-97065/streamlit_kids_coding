import streamlit as st
import numpy as np

if st.button("Refresh"):
  st.cache_resource.clear()
  st.session_state.answer = 0
  st.rerun()

with st.form("my_form"):
  st.write("Inside the form")
  st.title("This is a maths Sats test")
  st.write("Add these two numbers:")
  n1=np.random.randint(low=20,high=30)
  n2=np.random.randint(low=50,high=100)
  
  st.write("First number is " , n1)
  st.write("Second number is " , n2)

  
  s=n1+n2
  a=st.number_input(" Enter your answer",step=1)
  if st.form_submit_button("Submit"):
    if a==s:
      st.write( " YAY YOU ARE CORRRRRRRREEEEEECCCCCCTTTTTTTTTTTTTTTTTT")
    else:
      st.write(" YOU GET A RED CAAAAAAAAARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRD")
st.write("Outside the form")



st.title("This is a maths Sats test")
st.write("please enter you answer here")
n1=np.random.randint(low=20,high=30)
n2=np.random.randint(low=50,high=100)
s=n1+n2

# st.write("session answer: ", st.session_state.answer)

if 'answer' not in st.session_state or st.session_state.answer == 0:
  # st.write("inside session creation:")
  st.session_state.n1 = n1
  st.session_state.n2 = n2
  st.session_state.answer = s
  # st.write("session answer:",s)


st.write("First number is " , n1)
st.write("Second number is " , n2)
# st.write("The first sum is" , s)      
a=st.number_input(" Enter your answer",step=1)


if st.button("check your answer"):
  ans = st.session_state.answer
  st.write("Question: ", st.session_state.n1, " + ", st.session_state.n2)
  st.write("Actual Answer: ", ans)
  st.write("Your Answer: ", a)
  if a==ans:
    st.write( " YAY YOU ARE CORRRRRRRREEEEEECCCCCCTTTTTTTTTTTTTTTTTT")
  else:
    st.write(" YOU GET A RED CAAAAAAAAARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRD")
  st.session_state.answer = s
  st.session_state.n1 = n1
  st.session_state.n2 = n2
