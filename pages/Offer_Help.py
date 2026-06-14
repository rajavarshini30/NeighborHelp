import streamlit as st
import sqlite3

st.set_page_config(page_title="Offer Help", page_icon="🤲")

st.title("🤲 Offer Help")

help_category = st.selectbox(
    "Choose Service Category",
    [
        "Tutor",
        "Pet Sitting",
        "Transportation",
        "Tool Lending",
        "Household Help",
        "Tech Support",
        "Other"
    ]
)

custom_service = ""

if help_category == "Other":
    custom_service = st.text_input(
        "Enter Your Service"
    )

service_title = st.text_input(
    "Service Title"
)

description = st.text_area(
    "Describe Your Service"
)

area = st.text_input(
    "Area"
)

radius = st.slider(
    "Service Radius (KM)",
    1,
    5,
    3
)

if st.button("🚀 Publish Service"):

    final_category = (
        custom_service
        if help_category == "Other"
        else help_category
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
        area,
        radius
    ))

    conn.commit()
    conn.close()

    st.success("✅ Service Published Successfully!")