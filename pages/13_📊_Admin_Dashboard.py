import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="📊"
)

st.title("📊 Admin Dashboard")

conn = sqlite3.connect("neighborhelp.db")
cursor = conn.cursor()

# Requests
cursor.execute("SELECT COUNT(*) FROM requests")
request_count = cursor.fetchone()[0]

# Offers
cursor.execute("SELECT COUNT(*) FROM offers")
offer_count = cursor.fetchone()[0]

# Communities
cursor.execute("SELECT COUNT(*) FROM communities")
community_count = cursor.fetchone()[0]

# Ratings
cursor.execute("SELECT COUNT(*) FROM ratings")
rating_count = cursor.fetchone()[0]

# Chats
cursor.execute("SELECT COUNT(*) FROM chat_messages")
chat_count = cursor.fetchone()[0]

conn.close()

st.subheader("📈 Platform Statistics")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("📝 Requests", request_count)

with c2:
    st.metric("🤲 Offers", offer_count)

with c3:
    st.metric("🏘️ Communities", community_count)

with c4:
    st.metric("⭐ Ratings", rating_count)

with c5:
    st.metric("💬 Chats", chat_count)

st.write("---")

st.success("✅ Platform Monitoring Active")

st.caption(
    "NeighborHelp © 2026 | Admin Dashboard"
)