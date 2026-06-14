import streamlit as st
import sqlite3
from locations import HYDERABAD_AREAS

st.set_page_config(page_title="Offer Help", page_icon="🤲")

st.markdown("""
<style>

.stButton button {
    background: linear-gradient(90deg,#16A34A,#22C55E);
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

st.title("🤲 Offer Help")

st.success("Share your skills and help your community.")

category = st.selectbox(
    "Choose Service Category",
    [
        "Tutor",
        "Pet Sitting",
        "Transportation",
        "Tool Lending",
        "Household Help",
        "Tech Support",
        "Skill Training",
        "Other"
    ]
)

custom_service = ""

if category == "Other":
    custom_service = st.text_input(
        "Enter Your Service"
    )

service_title = st.text_input(
    "Service Title",
    placeholder="Example: Mathematics Tutor"
)

description = st.text_area(
    "Describe Your Service"
)

st.subheader("📍 Service Location")

area = st.selectbox(
    "Select Hyderabad Area",
    HYDERABAD_AREAS
)

exact_location = st.text_input(
    "Apartment / Landmark / Street",
    placeholder="Example: Near DLF Building"
)

location = f"{area} - {exact_location}"

radius = st.slider(
    "Service Radius (KM)",
    1,
    5,
    3
)

if st.button("🚀 Publish Service"):

    final_category = (
        custom_service
        if category == "Other"
        else category
    )

    conn = sqlite3.connect("neighborhelp.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO offers
    (
        category,
        title,
        description,
        area,
        radius
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        final_category,
        service_title,
        description,
        location,
        radius
    ))

    conn.commit()
    conn.close()

    st.success("✅ Service Published Successfully!")

    st.markdown("### 📋 Service Summary")

    st.write("Category:", final_category)
    st.write("Title:", service_title)
    st.write("Description:", description)
    st.write("Location:", location)
    st.write("Radius:", radius, "KM")