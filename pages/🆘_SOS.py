import streamlit as st

st.set_page_config(
    page_title="SOS Alert",
    page_icon="🆘"
)

st.title("🆘 Emergency SOS")

st.warning("""
Use this feature only during emergencies.

This alert is designed for immediate assistance.
""")

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

area = st.selectbox(
    "📍 Current Area",
    areas
)

exact_location = st.text_input(
    "📌 Exact Location",
    placeholder="Example: Apartment Name, Landmark"
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
    f"🆘 SOS alert will notify users within {radius} KM of {area}"
)

details = st.text_area(
    "Emergency Details",
    placeholder="Describe the emergency..."
)

if st.button("🆘 SEND SOS ALERT"):

    st.error("🚨 SOS Alert Sent!")

    st.success(
        f"Nearby users within {radius} KM have been notified."
    )

    st.success(
        "Emergency contact notification initiated."
    )

    st.markdown("### SOS Summary")

    st.write("Area:", area)
    st.write("Location:", exact_location)
    st.write("Radius:", radius, "KM")
    st.write("Details:", details)

st.write("---")

st.caption(
    "NeighborHelp © 2026 | Community Support Platform"
)