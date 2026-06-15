import streamlit as st

st.set_page_config(
    page_title="Emergency Assistance",
    page_icon="🚨"
)

st.title("🚨 Emergency Assistance")

st.warning(
    "Use this section only for urgent situations requiring immediate community support."
)

emergency_type = st.selectbox(
    "🚨 Emergency Type",
    [
        "Medical Emergency",
        "Blood Donation",
        "Vehicle Breakdown",
        "Safety Concern",
        "Pet Emergency",
        "Other"
    ]
)

areas = [
    "Habsiguda",
    "Uppal",
    "Tarnaka",
    "Mallapur",
    "Nacharam",
    "Boduppal",
    "LB Nagar",
    "Dilsukhnagar",
    "Ameerpet",
    "Kukatpally",
    "Madhapur",
    "Hitech City",
    "Gachibowli",
    "Banjara Hills",
    "Himayat Nagar",
    "Kompally",
    "Gandimaisamma"
]

st.subheader("📍 Location Details")

area = st.selectbox(
    "Select Area",
    areas
)

exact_location = st.text_input(
    "Exact Location",
    placeholder="Example: Shakti Sai Nagar, Plot 91"
)

# ==========================
# GEOFENCING
# ==========================

st.subheader("📍 Geofencing Settings")

radius = st.slider(
    "📏 Alert Radius (KM)",
    1,
    10,
    3
)

st.info(
    f"🚨 Emergency alert will be shared within {radius} KM of {area}"
)

description = st.text_area(
    "📝 Describe the Emergency",
    placeholder="Provide details..."
)

if st.button("🚨 SEND EMERGENCY ALERT"):

    st.error("🚨 Emergency Alert Sent!")

    st.success(
        f"Nearby users within {radius} KM have been notified."
    )

    st.markdown("### Alert Summary")

    st.write("Emergency Type:", emergency_type)
    st.write("Area:", area)
    st.write("Location:", exact_location)
    st.write("Radius:", radius, "KM")
    st.write("Description:", description)

st.write("---")

st.caption(
    "NeighborHelp © 2026 | Community Support Platform"
)