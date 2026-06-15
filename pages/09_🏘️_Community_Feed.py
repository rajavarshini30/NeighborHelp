import streamlit as st
import sqlite3
from locations import HYDERABAD_AREAS

st.set_page_config(
    page_title="Community Feed",
    page_icon="🏘️"
)

st.title("🏘️ Community Feed")

st.write(
    "View nearby help requests and community services."
)

st.write("---")

# =====================================
# FILTERS
# =====================================

search = st.text_input(
    "🔍 Search"
)

selected_area = st.selectbox(
    "📍 Filter by Area",
    ["All Areas"] + HYDERABAD_AREAS
)

st.write("---")

# =====================================
# HELP REQUESTS
# =====================================

st.header("📌 Help Requests")

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

request_count = 0

for request in requests:

    req_id, title, category, help_type, location, urgency = request

    if search:
        if search.lower() not in title.lower():
            continue

    if selected_area != "All Areas":
        if not location.startswith(selected_area):
            continue

    request_count += 1

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
                f"❤️ Volunteer #{req_id}"
            ):
                st.success(
                    "Volunteer request submitted!"
                )

        with col2:
            if st.button(
                f"✔ Resolve #{req_id}"
            ):
                st.success(
                    "Request marked resolved!"
                )

        st.write("---")

if request_count == 0:
    st.info("No help requests found.")

# =====================================
# COMMUNITY HELPERS
# =====================================

st.header("🤲 Community Helpers")

cursor.execute("""
SELECT
id,
category,
title,
description,
area,
radius
FROM offers
ORDER BY id DESC
""")

offers = cursor.fetchall()

helper_count = 0

for offer in offers:

    offer_id, category, title, description, area, radius = offer

    if search:
        if search.lower() not in title.lower():
            continue

    if selected_area != "All Areas":
        if not area.startswith(selected_area):
            continue

    helper_count += 1

    with st.container():

        st.markdown(f"""
### 🤲 {title}

🏷️ Category: {category}

📝 Description: {description}

📍 Location: {area}

📏 Service Radius: {radius} KM
""")

        if st.button(
            f"📞 Contact Helper #{offer_id}"
        ):
            st.success(
                "Helper contact request sent!"
            )

        st.write("---")

if helper_count == 0:
    st.info("No community helpers found.")

conn.close()

# =====================================
# FOOTER
# =====================================

st.write("---")

st.caption(
    "NeighborHelp © 2026 | Community Support Platform"
)