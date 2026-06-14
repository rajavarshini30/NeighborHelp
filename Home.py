import streamlit as st
import sqlite3

st.set_page_config(
    page_title="NeighborHelp",
    page_icon="🤝",
    layout="wide"
)

# ---------------------------
# DATABASE
# ---------------------------

request_count = 0
offer_count = 0
recent_requests = []
recent_offers = []

try:

    conn = sqlite3.connect("neighborhelp.db")
    cursor = conn.cursor()

    # Request Count
    cursor.execute("SELECT COUNT(*) FROM requests")
    request_count = cursor.fetchone()[0]

    # Offer Count
    cursor.execute("SELECT COUNT(*) FROM offers")
    offer_count = cursor.fetchone()[0]

    # Recent Requests
    cursor.execute("""
    SELECT title, location
    FROM requests
    ORDER BY id DESC
    LIMIT 5
    """)

    recent_requests = cursor.fetchall()

    # Recent Offers
    cursor.execute("""
    SELECT title, area
    FROM offers
    ORDER BY id DESC
    LIMIT 5
    """)

    recent_offers = cursor.fetchall()

    conn.close()

except Exception as e:
    st.error(f"Database Error: {e}")

# ---------------------------
# HEADER
# ---------------------------

st.title("🤝 NeighborHelp")

st.markdown("""
### Helping Neighbors, Building Communities
""")

st.write("---")

# ---------------------------
# QUICK ACCESS
# ---------------------------

col1, col2 = st.columns(2)

with col1:
    st.info("📝 Request Help")

with col2:
    st.success("🤲 Offer Help")

col3, col4 = st.columns(2)

with col3:
    st.error("🚨 Emergency Assistance")

with col4:
    st.warning("🏘️ Community Groups")

st.write("---")

# ---------------------------
# LIVE STATS
# ---------------------------

st.subheader("📊 Live Statistics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "📝 Total Requests",
        request_count
    )

with c2:
    st.metric(
        "🤲 Total Offers",
        offer_count
    )

with c3:
    st.metric(
        "📈 Total Activity",
        request_count + offer_count
    )

st.write("---")

# ---------------------------
# RECENT REQUESTS
# ---------------------------

st.subheader("📝 Recent Requests")

if recent_requests:

    for title, location in recent_requests:

        st.success(
            f"📌 {title}\n\n📍 {location}"
        )

else:
    st.info("No requests available.")

st.write("---")

# ---------------------------
# RECENT OFFERS
# ---------------------------

st.subheader("🤲 Recent Offers")

if recent_offers:

    for title, location in recent_offers:

        st.info(
            f"📌 {title}\n\n📍 {location}"
        )

else:
    st.info("No offers available.")

st.write("---")

# ---------------------------
# ACTIVE COMMUNITIES
# ---------------------------

st.subheader("🏘️ Active Communities")

st.success("🏢 Shakti Sai Nagar")
st.info("🏢 Green Valley Residency")
st.warning("🏫 ABC Student Hostel")

st.write("---")

# ---------------------------
# COMMUNITY HEROES
# ---------------------------

st.subheader("🌟 Community Heroes")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🥇 Community Hero")

with col2:
    st.info("🤝 Trusted Neighbor")

with col3:
    st.warning("🚨 Emergency Responder")

st.write("---")

# ---------------------------
# FEATURES
# ---------------------------

st.subheader("📍 Platform Features")

st.markdown("""
✅ Request Help

✅ Offer Help

✅ Emergency Assistance

✅ Community Feed

✅ Community Groups

✅ Subscriptions

✅ Ratings & Trust Score

✅ Hyperlocal Support
""")
st.write("---")

st.caption(
    "NeighborHelp © 2026 | Community Support Platform"
)