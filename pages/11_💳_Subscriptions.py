import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Subscriptions",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Subscribe Your Community")

st.markdown("""
Choose the best subscription plan for your apartment,
residential colony, hostel, or gated community.
""")

st.write("---")

# ==================================
# AVAILABLE PLANS
# ==================================

st.subheader("💰 Available Plans")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### 🏢 Small Community

₹5,000 / Year

✅ Up to 100 Members

✅ Private Community Group

✅ Community Feed

✅ Emergency Alerts
""")

with col2:
    st.info("""
### 🏘️ Medium Community

₹15,000 / Year

✅ Up to 500 Members

✅ Private Community Group

✅ Emergency Alerts

✅ Priority Support
""")

with col3:
    st.warning("""
### 🌆 Large Community

₹50,000 / Year

✅ Unlimited Members

✅ Premium Features

✅ Priority Support

✅ Community Analytics
""")

st.write("---")

# ==================================
# PLAN SELECTION
# ==================================

selected_plan = st.radio(
    "📋 Choose Subscription Plan",
    [
        "🏢 Small Community - ₹5,000",
        "🏘️ Medium Community - ₹15,000",
        "🌆 Large Community - ₹50,000"
    ],
    horizontal=True
)

st.write("---")

# ==================================
# COMMUNITY DETAILS
# ==================================

st.subheader("📝 Community Details")

community_name = st.text_input(
    "Community Name",
    placeholder="Example: Shakti Sai Nagar"
)

community_type = st.selectbox(
    "Community Type",
    [
        "Apartment",
        "Residential Colony",
        "Student Hostel",
        "Gated Community"
    ]
)

contact_person = st.text_input(
    "Contact Person",
    placeholder="Example: Varshini"
)

phone = st.text_input(
    "Phone Number",
    max_chars=10,
    placeholder="10 Digit Mobile Number"
)

email = st.text_input(
    "Email Address",
    placeholder="example@gmail.com"
)

# ==================================
# VALIDATION
# ==================================

contact_valid = (
    contact_person.replace(" ", "").isalpha()
    if contact_person
    else False
)

phone_valid = (
    phone.isdigit() and len(phone) == 10
    if phone
    else False
)

email_valid = (
    "@" in email and "." in email
    if email
    else False
)

if contact_person and not contact_valid:
    st.error("❌ Contact Person should contain only alphabets.")

if phone and not phone_valid:
    st.error("❌ Phone Number must contain exactly 10 digits.")

if email and not email_valid:
    st.error("❌ Please enter a valid email address.")

st.write("---")

# ==================================
# SAVE SUBSCRIPTION
# ==================================

if st.button("💳 Proceed to Payment"):

    if not community_name.strip():
        st.error("❌ Please enter Community Name.")
        st.stop()

    if not contact_valid:
        st.error("❌ Contact Person should contain only alphabets.")
        st.stop()

    if not phone_valid:
        st.error("❌ Phone Number must contain exactly 10 digits.")
        st.stop()

    if not email_valid:
        st.error("❌ Please enter a valid email address.")
        st.stop()

    conn = sqlite3.connect("neighborhelp.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO communities
    (
        community_name,
        community_type,
        contact_person,
        phone,
        email,
        plan
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        community_name,
        community_type,
        contact_person,
        phone,
        email,
        selected_plan
    ))

    conn.commit()
    conn.close()

    st.balloons()

    st.success("✅ Subscription Saved Successfully!")

    st.markdown("## 📋 Subscription Summary")

    st.write("🏢 Community Name:", community_name)
    st.write("🏘️ Community Type:", community_type)
    st.write("👤 Contact Person:", contact_person)
    st.write("📞 Phone Number:", phone)
    st.write("📧 Email:", email)
    st.write("💳 Selected Plan:", selected_plan)

st.write("---")

st.subheader("🌟 Subscription Benefits")

st.markdown("""
✅ Private Community Groups

✅ Resident Directory

✅ Emergency Alerts

✅ Community Notices

✅ Lost & Found

✅ Verified Members

✅ Hyperlocal Assistance

✅ Trust & Reputation System
""")