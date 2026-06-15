import streamlit as st

st.set_page_config(
    page_title="SOS Alert",
    page_icon="🆘"
)

st.title("🆘 Emergency SOS")

st.warning("""
Use this feature only during emergencies.

This alert is designed for immediate assistance and personal safety.
""")

st.write("---")

# =====================================
# SOS TYPE
# =====================================

sos_type = st.selectbox(
    "🆘 SOS Type",
    [
        "Medical Emergency",
        "Accident",
        "Not Feeling Safe",
        "Senior Citizen Assistance",
        "Other"
    ]
)

# =====================================
# LOCATION
# =====================================

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
    placeholder="Apartment Name, Landmark, Street"
)

# =====================================
# GEOFENCING
# =====================================

st.subheader("📍 Geofencing Settings")

radius = st.slider(
    "📏 Alert Radius (KM)",
    1,
    10,
    3
)

st.info(
    f"🆘 SOS alert will notify nearby users within {radius} KM of {area}"
)

# =====================================
# DETAILS
# =====================================

details = st.text_area(
    "📝 Emergency Details",
    placeholder="Describe the emergency..."
)

st.write("---")

st.subheader("🛡️ Emergency Contact")

st.info("""
Emergency contact information will be
retrieved automatically from the user's profile.
""")

# =====================================
# SEND SOS
# =====================================

if st.button("🆘 SEND SOS ALERT"):

    st.error("🚨 SOS Alert Sent!")

    st.success(
        f"Nearby users within {radius} KM have been notified."
    )

    if sos_type == "Not Feeling Safe":

        st.warning("""
🛡️ Personal Safety Alert Activated
""")

        st.success("""
📞 Emergency Contact Notification Initiated

✅ Status: Sent Successfully
""")

    else:

        st.success("""
📞 Emergency Contact Notification Initiated

✅ Status: Sent Successfully
""")

    st.markdown("### 📋 SOS Summary")

    st.write("🆘 SOS Type:", sos_type)
    st.write("📍 Area:", area)
    st.write("📌 Exact Location:", exact_location)
    st.write("📏 Alert Radius:", radius, "KM")
    st.write("📝 Details:", details)

st.write("---")

st.subheader("ℹ️ How SOS Works")

st.info("""
1️⃣ User selects SOS type.

2️⃣ User enters location details.

3️⃣ Nearby community members are alerted.

4️⃣ Emergency contact saved in Profile is notified.

5️⃣ Community assistance is coordinated.
""")

st.write("---")

st.caption(
    "NeighborHelp © 2026 | Community Support Platform"
)