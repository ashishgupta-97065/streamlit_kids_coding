if st.button("Clear All"):
    # Clears all singleton caches:
    st.experimental_singleton.clear()


import streamlit as st
# import pyautogui
 
# if st.button("Reset"):
#     pyautogui.hotkey("ctrl","F5")

import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
