import streamlit as st
import sqlite3

st.set_page_config(page_title="Offer Help", page_icon="🤲")

st.markdown("""
<style>

.stButton button {
    background: linear-gradient(90deg,#16A34A,#22C55E);
    color: white;
    border-radius: 12px;
    border: none;
    height: 50px;
    font-size: 16px;
    font-weight: bold;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)

st.title("🤲 Offer Help")

st.success("Share your skills and help your community.")

help_category = st.selectbox(
    "Choose Service Category",
    [
        "📚 Tutor",
        "🐶 Pet Sitting",
        "🚗 Transportation",
        "🔧 Tool Lending",