import streamlit as st
import sqlite3
from locations import HYDERABAD_AREAS

st.set_page_config(page_title="Request Help", page_icon="📝")

# Styling
st.markdown("""
<style>

.stButton button {
    background: linear-gradient(90deg,#4F46E5,#7C3AED);
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

st.title("📝 Request Help")

# Request Title
title = st.text_input(
    "📌 Request Title",
    placeholder="Example: Need a Ladder for Painting"
)

# Category
category = st.selectbox(
    "🏷️ Select Category",
    [
        "Borrow Item",
        "Tutor Needed",
        "Pet Care",
        "Ride Needed",
        "Household Help",
        "Emergency",
        "Other"
    ]
)

custom_category = ""

if category == "Other":
    custom_category = st.text_input(
        "✏️ Enter Custom Category"
    )

# Help Type
help_type = st.text_input(
    "🤝 Type of Help Needed",
    placeholder="Example: Ladder, Math Tutor, Dog Walker"
)

# Description
description = st.text_area(
    "📝 Describe Your Request"
)

# Location
st.subheader("📍 Location Details")

area = st.selectbox(
    "Select Hyderabad Area",
    HYDERABAD_AREAS
)

exact_location = st.text_input(
    "Apartment / Landmark / Hotel / Street",
    placeholder="Example: Shakti Sai Nagar, Plot 91"
)

location = f"{area} - {exact_location}"

# Radius
radius = st.slider(
    "📏 Help Radius (KM)",
    min_value=1,
    max_value=5,
    value=3
)

# Urgency
urgency = st.radio(
    "⚡ Urgency Level",
    ["Low", "Medium", "High"],
    horizontal=True
)

# Submit
if st.button("🚀 Submit Request"):

    final_category = (
        custom_category
        if category == "Other"
        else category
    )

    conn = sqlite3.connect("neighborhelp.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO requests
    (
        title,
        category,
        help_type,
        description,
        location,
        radius,
        urgency
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        title,
        final_category,
        help_type,
        description,
        location,
        radius,
        urgency
    ))

    conn.commit()
    conn.close()

    st.success("✅ Request Saved Successfully!")

    st.markdown("### 📋 Request Summary")

    st.write("📌 Title:", title)
    st.write("🏷️ Category:", final_category)
    st.write("🤝 Help Type:", help_type)
    st.write("📝 Description:", description)
    st.write("📍 Location:", location)
    st.write("📏 Radius:", radius, "KM")
    st.write("⚡ Urgency:", urgency)