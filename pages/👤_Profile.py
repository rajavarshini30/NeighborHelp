import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Profile",
    page_icon="👤"
)

# =====================================
# CHECK LOGIN
# =====================================

if "user_email" not in st.session_state:
    st.error("Please login first.")
    st.stop()

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
""", (st.session_state["user_email"],))

user_data = cursor.fetchone()

conn.close()

if user_data:

    saved_name = user_data[0] or ""
    saved_age = user_data[1] or 18
    saved_gender = user_data[2] or "Prefer Not To Say"
    saved_area = user_data[3] or ""
    saved_phone = user_data[4] or ""

   