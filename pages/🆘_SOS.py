import streamlit as st

st.set_page_config(
    page_title="SOS Alert",
    page_icon="🆘"
)

st.title("🆘 Emergency SOS")

st.warning("""
Use this feature only during emergencies.
This will notify nearby volunteers and emergency contacts.
""")

st.write("---")

emergency_type = st.selectbox(
    "Emergency Type",
    [
        "Medical Emergency",
        "Safety Threat",
        "Accident",
        "Senior Citizen Assistance",
        "Other"
    ]
)

location = st.text_input(
    "Current Location"
)

details = st.text_area(
    "Emergency Details"
)

if st.button("🆘 SEND SOS ALERT"):

    st.error("🚨 SOS Alert Sent!")

    st.success("""
Emergency contacts and nearby community members
have been notified.
""")