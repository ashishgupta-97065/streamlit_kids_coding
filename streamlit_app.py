import streamlit as st

if st.button("Clear All"):
    # Clears all singleton caches:
    st.experimental_singleton.clear()




st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
