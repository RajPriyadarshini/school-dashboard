import streamlit as st

st.set_page_config(page_title="Subject Enrollment", page_icon="📚", layout="wide")

st.title("📚 Subject Enrollment")

st.subheader("Select Subjects")

subjects = ["Maths", "Science", "English", "Computer", "History"]

selected_subjects = st.multiselect("Choose your subjects:", subjects)

if st.button("Submit"):
    if selected_subjects:
        st.success(f"You have enrolled in: {', '.join(selected_subjects)}")
    else:
        st.warning("Please select at least one subject.")