import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Profile",
    page_icon="👤"
)

# =====================================
# LOGIN CHECK
# =====================================

if "user_email" not in st.session_state:
    st.error("🔐 Please login first.")
    st.stop()

user_email = st.session_state["user_email"]

# =====================================
# LOAD USER DATA
# =====================================

conn = sqlite3.connect("neighborhelp.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
full_name,
age,
gender,
area,
phone,
emergency_name,
emergency_phone,
emergency_email
FROM users
WHERE email = ?
""", (user_email,))

user = cursor.fetchone()

conn.close()

if user:

    saved_name = user[0] if user[0] else ""
    saved_age = user[1] if user[1] else 18
    saved_gender = user[2] if user[2] else "Prefer Not To Say"
    saved_area = user[3] if user[3] else ""
    saved_phone = user[4] if user[4] else ""

    saved_emergency_name = user[5] if user[5] else ""
    saved_emergency_phone = user[6] if user[6] else ""
    saved_emergency_email = user[7] if user[7] else ""

else:

    saved_name = ""
    saved_age = 18
    saved_gender = "Prefer Not To Say"
    saved_area = ""
    saved_phone = ""

    saved_emergency_name = ""
    saved_emergency_phone = ""
    saved_emergency_email = ""

# =====================================
# HEADER
# =====================================

st.title("👤 User Profile")

st.write(
    "Manage your NeighborHelp profile and emergency contact information."
)

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
# PERSONAL INFORMATION
# =====================================

st.subheader("👤 Personal Information")

name = st.text_input(
    "Full Name",
    value=saved_name
)

age = st.number_input(
    "Age",
    min_value=16,
    max_value=100,
    value=int(saved_age)
)

gender_options = [
    "Male",
    "Female",
    "Other",
    "Prefer Not To Say"
]

gender_index = (
    gender_options.index(saved_gender)
    if saved_gender in gender_options
    else 3
)

gender = st.selectbox(
    "Gender",
    gender_options,
    index=gender_index
)

area = st.text_input(
    "Area",
    value=saved_area
)

phone = st.text_input(
    "Mobile Number",
    value=saved_phone,
    max_chars=10
)

st.write("---")

# =====================================
# EMERGENCY CONTACT
# =====================================

st.subheader("🛡️ Emergency Contact")

emergency_name = st.text_input(
    "Emergency Contact Name",
    value=saved_emergency_name
)

emergency_phone = st.text_input(
    "Emergency Contact Number",
    value=saved_emergency_phone,
    max_chars=10
)

emergency_email = st.text_input(
    "Emergency Contact Email",
    value=saved_emergency_email
)

st.write("---")

# =====================================
# SAVE PROFILE
# =====================================

if st.button("💾 Save Profile"):

    conn = sqlite3.connect("neighborhelp.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users
    SET
        full_name = ?,
        age = ?,
        gender = ?,
        area = ?,
        phone = ?,
        emergency_name = ?,
        emergency_phone = ?,
        emergency_email = ?
    WHERE email = ?
    """,
    (
        name,
        age,
        gender,
        area,
        phone,
        emergency_name,
        emergency_phone,
        emergency_email,
        user_email
    ))

    conn.commit()
    conn.close()

    st.success("✅ Profile Saved Successfully!")

# =====================================
# VERIFICATION STATUS
# =====================================

st.write("---")

st.subheader("✅ Verification Status")

st.success("📱 Mobile Verification Enabled")
st.success("📧 Email Verification Enabled")
st.info("🪪 Government ID Verification (Future Feature)")
st.success("🔞 Minimum Age Requirement: 16+")

st.write("---")

# =====================================
# CONTINUE TO HOME
# =====================================

if st.button("🏠 Continue to Home"):
    st.switch_page("pages/🏠_Home.py")

st.write("---")

st.caption(
    "NeighborHelp © 2026 | Community Support Platform"
)