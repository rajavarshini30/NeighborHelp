import streamlit as st

st.title("🚨 Emergency Assistance")

emergency_type = st.selectbox(
    "Emergency Type",
    [
        "Medical Emergency",
        "Blood Donation",
        "Vehicle Breakdown",
        "Safety Concern",
        "Other"
    ]
)

description = st.text_area(
    "Describe the Emergency"
)

location = st.text_input(
    "Location"
)

if st.button("Send Emergency Alert"):
    st.error("🚨 Emergency Alert Sent!")

    st.write("Emergency Type:", emergency_type)
    st.write("Description:", description)
    st.write("Location:", location)