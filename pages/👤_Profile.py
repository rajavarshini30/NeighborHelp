import streamlit as st

st.set_page_config(
    page_title="Profile",
    page_icon="👤"
)

# =====================================
# HEADER
# =====================================

st.title("👤 User Profile")

st.write("""
Manage your NeighborHelp profile and safety information.
""")

st.write("---")

# =====================================
# PROFILE PHOTO
# =====================================

profile_pic = st.file_uploader(
    "📷 Upload Profile Picture",
    type=["jpg", "jpeg", "png"]
)

if profile_pic:
    st.image(profile_pic, width=180)

st.write("---")

# =====================================
# PERSONAL DETAILS
# =====================================

st.subheader("👤 Personal Information")

name = st.text_input(
    "Full Name",
    placeholder="Enter your full name"
)

age = st.number_input(
    "Age",
    min_value=16,
    max_value=100,
    value=18
)

gender = st.selectbox(
    "Gender",
    [
        "Male",
        "Female",
        "Other",
        "Prefer Not To Say"
    ]
)

area = st.text_input(
    "Area",
    placeholder="Example: Mallapur"
)

phone = st.text_input(
    "Mobile Number",
    max_chars=10,
    placeholder="10 Digit Mobile Number"
)

phone_valid = (
    phone.isdigit() and len(phone) == 10
    if phone
    else False
)

if phone and not phone_valid:
    st.error("❌ Mobile Number must contain exactly 10 digits.")

st.write("---")

# =====================================
# EMERGENCY CONTACT
# =====================================

st.subheader("🛡️ Emergency Contact (Optional)")

emergency_name = st.text_input(
    "Emergency Contact Name",
    placeholder="Example: Parent / Spouse / Friend"
)

emergency_phone = st.text_input(
    "Emergency Contact Number",
    max_chars=10,
    placeholder="10 Digit Mobile Number"
)

emergency_email = st.text_input(
    "Emergency Contact Email",
    placeholder="example@gmail.com"
)

emergency_phone_valid = (
    emergency_phone.isdigit() and len(emergency_phone) == 10
    if emergency_phone
    else False
)

if emergency_phone and not emergency_phone_valid:
    st.error(
        "❌ Emergency Contact Number must contain exactly 10 digits."
    )

st.write("---")

# =====================================
# VERIFICATION STATUS
# =====================================

st.subheader("✅ Verification Status")

st.success("📱 Mobile Verification Enabled")

st.success("📧 Email Verification Enabled")

st.info("🪪 Government ID Verification (Future Feature)")

st.success("🔞 Age Requirement Passed")

st.write("---")

# =====================================
# TRUST SCORE
# =====================================

st.subheader("⭐ Trust Score")

st.metric(
    "Community Trust Score",
    "4.8 / 5"
)

st.write("---")

# =====================================
# BADGES
# =====================================

st.subheader("🏆 Community Badges")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
🥇 Community Hero

50+ Successful Helps
""")

with col2:
    st.info("""
🤝 Trusted Neighbor

High Community Rating
""")

with col3:
    st.warning("""
🚨 Emergency Responder

10+ Emergency Assists
""")

st.write("---")

# =====================================
# ACTIVITY STATS
# =====================================

st.subheader("📊 Activity Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📝 Requests", "3")

with c2:
    st.metric("🤲 Offers", "1")

with c3:
    st.metric("🚨 Emergencies", "2")

with c4:
    st.metric("🏘️ Communities", "1")

st.write("---")

# =====================================
# SAVE PROFILE
# =====================================

if st.button("💾 Save Profile"):

    if not name.strip():
        st.error("❌ Please enter your name.")
        st.stop()

    if not phone_valid:
        st.error("❌ Enter a valid 10-digit mobile number.")
        st.stop()

    if emergency_phone and not emergency_phone_valid:
        st.error("❌ Enter a valid emergency contact number.")
        st.stop()

    st.success("✅ Profile Saved Successfully!")

    st.markdown("### 📋 Profile Summary")

    st.write("👤 Name:", name)
    st.write("🎂 Age:", age)
    st.write("⚧ Gender:", gender)
    st.write("📍 Area:", area)
    st.write("📞 Mobile:", phone)

    st.write("---")

    st.write("🛡️ Emergency Contact:", emergency_name)
    st.write("📞 Emergency Contact Number:", emergency_phone)
    st.write("📧 Emergency Contact Email:", emergency_email)

st.write("---")

st.caption(
    "NeighborHelp © 2026 | Community Support Platform"
)