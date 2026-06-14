import streamlit as st

st.set_page_config(
    page_title="NeighborHelp",
    page_icon="🤝",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

h1 {
    text-align:center;
}

.stMetric {
    background-color:white;
    padding:15px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

st.title("🤝 NeighborHelp")

st.subheader("Helping Neighbors, Building Communities")

st.write("")

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

st.subheader("📊 Community Statistics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("👥 Users", "250")

with c2:
    st.metric("📝 Requests", "120")

with c3:
    st.metric("🤲 Helpers", "85")

st.write("---")

st.subheader("🌟 Top Community Heroes")

st.write("🥇 Rahul - 120 Points")
st.write("🥈 Priya - 110 Points")
st.write("🥉 Arjun - 95 Points")

st.write("---")

st.success("Welcome to NeighborHelp! Use the sidebar to access all features.")