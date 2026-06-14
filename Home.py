import streamlit as st
import sqlite3

st.set_page_config(
    page_title="NeighborHelp",
    page_icon="🤝",
    layout="wide"
)

# Database Connection
conn = sqlite3.connect("neighborhelp.db")
cursor = conn.cursor()

# Count Requests
cursor.execute("SELECT COUNT(*) FROM requests")
request_count = cursor.fetchone()[0]

# Count Offers
cursor.execute("SELECT COUNT(*) FROM offers")
offer_count = cursor.fetchone()[0]

conn.close()

# -------------------
# UI
# -------------------

st.title("🤝 NeighborHelp")

st.subheader("Helping Neighbors, Building Communities")

st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.info("📝 Request Help")

with col2:
    st.success("🤲 Offer Help")

col3, col4 = st.columns(2)

with col3:
    st.error("🚨 Emergency")

with col4:
    st.warning("🏘️ Community Groups")

st.write("---")

st.subheader("📊 Live Community Statistics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "📝 Total Requests",
        request_count
    )

with c2:
    st.metric(
        "🤲 Total Helpers",
        offer_count
    )

with c3:
    st.metric(
        "👥 Community Members",
        request_count + offer_count
    )

st.write("---")

st.subheader("🌟 Top Community Heroes")

st.write("🥇 Community Hero")
st.write("🥈 Trusted Neighbor")
st.write("🥉 Active Helper")

st.success(
    "Welcome to NeighborHelp! Use the sidebar to navigate."
)