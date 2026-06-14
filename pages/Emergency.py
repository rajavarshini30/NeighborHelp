import streamlit as st
from locations import HYDERABAD_AREAS

st.set_page_config(
    page_title="Emergency Assistance",
    page_icon="🚨"
)

# ---------------------------
# STYLING
# ---------------------------

st.markdown("""
<style>

.stButton button {
    background: linear-gradient(90deg,#DC2626,#EF4444);
    color: white;
    border-radius: 12px;
    border: none;
    height: 50px;
    font-size: 16px;
    font-weight: bold;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# PAGE TITLE
# ---------------------------

st.title("🚨 Emergency Assistance")

st.warning(
    "Use this section only for urgent situations requiring immediate community support."
)

# ---------------------------
# EMERGENCY TYPE
# ---------------------------

emergency_type = st.selectbox(
    "🚨 Emergency Type",
    [
        "Medical Emergency",
        "Blood Donation",
        "Vehicle Breakdown",
        "Safety Concern",
        "Pet Emergency",
        "Hospital Assistance",
        "Other"
    ]
)

# ---------------------------
# PRIORITY
# ---------------------------

priority = st.radio(
    "⚡ Priority Level",
    ["Low", "Medium", "High"],
    horizontal=True
)

# ---------------------------
# LOCATION
# ---------------------------

st.subheader("📍 Location Details")

area = st.selectbox(
    "Select Hyderabad Area",
    HYDERABAD_AREAS
)

exact_location = st.text_input(
    "Apartment / Landmark / Hotel / Street",
    placeholder="Example: Shakti Sai Nagar, Plot 91"
)

# ---------------------------
# CONTACT NUMBER
# ---------------------------

phone = st.text_input(
    "📞 Contact Number",
    max_chars=10,
    placeholder="10 Digit Mobile Number"
)

phone_valid = (
    phone.isdigit() and len(phone) == 10
    if phone
    else False
)

if phone and not phone_valid:
    st.error("❌ Phone Number must contain exactly 10 digits.")

# ---------------------------
# DESCRIPTION
# ---------------------------

description = st.text_area(
    "📝 Describe the Emergency",
    placeholder="Provide complete details of the emergency..."
)

# ---------------------------
# RADIUS
# ---------------------------

radius = st.slider(
    "📏 Alert Radius (KM)",
    min_value=1,
    max_value=5,
    value=3
)

# ---------------------------
# SUBMIT BUTTON
# ---------------------------

if st.button("🚨 SEND EMERGENCY ALERT"):

    if not phone_valid:
        st.error("❌ Enter a valid 10-digit phone number.")
        st.stop()

    location = f"{area} - {exact_location}"

    st.error("🚨 Emergency Alert Sent Successfully!")

    st.markdown("## 📋 Emergency Summary")

    st.write("🚨 Emergency Type:", emergency_type)
    st.write("⚡ Priority Level:", priority)
    st.write("📍 Location:", location)
    st.write("📞 Contact Number:", phone)
    st.write("📏 Alert Radius:", radius, "KM")
    st.write("📝 Description:", description)

    st.success(
        "Nearby community members within the selected radius have been notified."
    )