import streamlit as st
import sqlite3
from locations import HYDERABAD_AREAS

st.set_page_config(
    page_title="Community Feed",
    page_icon="🏘️"
)

st.title("🏘️ Community Feed")

st.write("View nearby help requests from your community.")

st.write("---")

# =========================
# FILTERS
# =========================

search = st.text_input(
    "🔍 Search Requests"
)

selected_area = st.selectbox(
    "📍 Filter by Area",
    ["All Areas"] + HYDERABAD_AREAS
)

selected_urgency = st.selectbox(
    "⚡ Filter by Urgency",
    ["All", "Low", "Medium", "High"]
)

st.write("---")

# =========================
# DATABASE
# =========================

conn = sqlite3.connect("neighborhelp.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
id,
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

filtered_requests = []

for request in requests:

    req_id, title, category, help_type, location, urgency = request

    if search:
        if search.lower() not in title.lower():
            continue

    if selected_area != "All Areas":
        if not location.startswith(selected_area):
            continue

    if selected_urgency != "All":
        if urgency != selected_urgency:
            continue

    filtered_requests.append(request)

# =========================
# DISPLAY
# =========================

if not filtered_requests:

    st.info("No matching requests found.")

else:

    st.success(
        f"Found {len(filtered_requests)} request(s)"
    )

    for request in filtered_requests:

        req_id, title, category, help_type, location, urgency = request

        with st.container():

            st.markdown(f"""
### 📌 {title}

🏷️ Category: {category}

🤝 Help Needed: {help_type}

📍 Location: {location}

⚡ Urgency: {urgency}
""")

            col1, col2 = st.columns(2)

            with col1:
                if st.button(
                    f"❤️ Volunteer to Help #{req_id}"
                ):
                    st.success(
                        "Volunteer request submitted!"
                    )

            with col2:
                if st.button(
                    f"✔ Mark Resolved #{req_id}"
                ):
                    st.success(
                        "Request marked as resolved!"
                    )

            st.write("---")