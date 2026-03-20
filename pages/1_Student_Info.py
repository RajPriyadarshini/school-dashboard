import streamlit as st

st.set_page_config(page_title="Student Info", page_icon="👩‍🎓", layout="wide")

st.title("👩‍🎓 Student Information")

# Sample student data
students = [
    {"Name": "Priya", "Class": "10", "Age": 15},
    {"Name": "Rahul", "Class": "9", "Age": 14},
    {"Name": "Anjali", "Class": "10", "Age": 15}
]

st.subheader("Student List")
st.table(students)