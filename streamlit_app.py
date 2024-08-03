import streamlit as st
from streamlit import caching

if st.button("Clear All"):
    st.title("🎈 My new app")
    caching.clear_cache()




st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
