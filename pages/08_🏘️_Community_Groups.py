import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Community Groups",
    page_icon="🏘️"
)

st.title("🏘️ Community Groups")

st.markdown("""
Browse subscribed communities on NeighborHelp.

Communities that purchase a subscription
automatically appear here.
""")

st.write("---")

# ==========================
# FILTER
# ==========================

community_filter = st.selectbox(
    "Filter Community Type",
    [
        "All",
        "Apartment",
        "Residential Colony",
        "Student Hostel",
        "Gated Community"
    ]
)

st.write("---")

# ==========================
# LOAD COMMUNITIES
# ==========================

conn = sqlite3.connect("neighborhelp.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
community_name,
community_type,
plan
FROM communities
ORDER BY id DESC
""")

communities = cursor.fetchall()

conn.close()

# ==========================
# DISPLAY COMMUNITIES
# ==========================

st.subheader("🏘️ Subscribed Communities")

if not communities:

    st.info("No subscribed communities yet.")

else:

    for name, ctype, plan in communities:

        if community_filter != "All":
            if ctype != community_filter:
                continue

        st.success(f"""
🏢 {name}

🏘️ Type: {ctype}

💳 Plan: {plan}

✅ Subscription Active
""")

st.write("---")

# ==========================
# SEARCH
# ==========================

st.subheader("🔍 Search Community")

search = st.text_input(
    "Enter Community Name"
)

if search:

    found = False

    for name, ctype, plan in communities:

        if search.lower() in name.lower():

            found = True

            st.info(f"""
🏢 {name}

🏘️ Type: {ctype}

💳 Plan: {plan}
""")

    if not found:
        st.warning("No matching community found.")

st.write("---")

# ==========================
# PLANS
# ==========================

st.subheader("💰 Subscription Plans")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
🏢 Small Community

₹5,000/year

Up to 100 Members
""")

with col2:
    st.info("""
🏘️ Medium Community

₹15,000/year

Up to 500 Members
""")

with col3:
    st.warning("""
🌆 Large Community

₹50,000/year

Unlimited Members
""")

st.write("---")

# ==========================
# JOIN BUTTON
# ==========================

if st.button(
    "🚀 Join Community",
    key="join_community"
):
    st.success(
        "Join request submitted successfully!"
    )

st.write("---")

st.caption(
    "NeighborHelp © 2026 | Community Support Platform"
)