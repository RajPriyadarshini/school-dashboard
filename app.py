import streamlit as st

# Page configuration
st.set_page_config(
    page_title="School Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Home Page Content
st.title("🎓 Welcome to School Dashboard")

st.markdown("""
This application helps manage:
- 📚 Student Information
- 📝 Subject Enrollment

Use the sidebar to navigate between pages.
""")

st.success("Select a page from the sidebar to get started!")