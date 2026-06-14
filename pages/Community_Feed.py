import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Community Feed",
    page_icon="🏘️"
)

st.title("🏘️ Community Feed")

st.write("View nearby help requests from your community.")

# Connect to database
conn = sqlite3.connect("neighborhelp.db")
cursor = conn.cursor()

# Get all requests
cursor.execute("""
SELECT
title,
category,
help_type,
location,
urgency
FROM requests
ORDER BY id DESC
""")

requests = cursor.fetchall()

conn.close()

if not requests:
    st.info("No requests available yet.")
else:

    for request in requests:

        title, category, help_type, location, urgency = request

        if urgency == "High":
            st.error(
                f"""
📌 {title}

🏷️ Category: {category}

🤝 Help Needed: {help_type}

📍 Location: {location}

⚡ Urgency: {urgency}
"""
            )

        elif urgency == "Medium":
            st.warning(
                f"""
📌 {title}

🏷️ Category: {category}

🤝 Help Needed: {help_type}

📍 Location: {location}

⚡ Urgency: {urgency}
"""
            )

        else:
            st.success(
                f"""
📌 {title}

🏷️ Category: {category}

🤝 Help Needed: {help_type}

📍 Location: {location}

⚡ Urgency: {urgency}
"""
            )