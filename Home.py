import streamlit as st
import sqlite3

st.set_page_config(
    page_title="NeighborHelp",
    page_icon="🤝",
    layout="wide"
)

# ---------------------------
# DATABASE COUNTS
# ---------------------------

request_count = 0
offer_count = 0

try:
    conn = sqlite3.connect("neighborhelp.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM requests")
    request_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM offers")
    offer_count = cursor.fetchone()[0]

    conn.close()

except Exception as e:
    st.error(f"Database Error: {e}")

# ---------------------------
# HOME PAGE
# ---------------------------

st.title("🤝 NeighborHelp")

st.markdown("""
### Helping Neighbors, Building Communities
""")

st.write("---")

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

st.subheader("📊 Live Statistics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        label="📝 Total Requests",
        value=request_count
    )

with c2:
    st.metric(
        label="🤲 Total Offers",
        value=offer_count
    )

with c3:
    st.metric(
        label="📈 Total Activity",
        value=request_count + offer_count
    )

st.write("---")

st.subheader("🌟 Community Heroes")

st.success("🥇 Community Hero")
st.info("🥈 Trusted Neighbor")
st.warning("🥉 Active Helper")

st.write("---")

st.markdown("""
### 📍 Features

✅ Request Help

✅ Offer Help

✅ Emergency Assistance

✅ Community Feed

✅ Trust Building

✅ Hyperlocal Support
""")