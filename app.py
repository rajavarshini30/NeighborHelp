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

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
    text-align: center;
    margin-bottom: 20px;
}

h1 {
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

st.title("🤝 NeighborHelp")

st.markdown(
"""
### Helping Neighbors, Building Communities
"""
)

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
    st.metric("Users", "250")

with c2:
    st.metric("Requests", "120")

with c3:
    st.metric("Helpers", "85")

st.write("---")

st.subheader("🌟 Top Community Heroes")

st.write("🥇 Rahul - 120 Points")
st.write("🥈 Priya - 110 Points")
st.write("🥉 Arjun - 95 Points")