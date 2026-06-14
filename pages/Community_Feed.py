import streamlit as st

st.title("🏘️ Community Feed")

col1, col2 = st.columns(2)

with col1:
    st.info("""
🪜 Need Ladder

📍 Habsiguda

📏 1.2 KM Away

⚡ High Priority
""")

with col2:
    st.success("""
📚 Need Math Tutor

📍 Uppal

📏 2.3 KM Away

⚡ Medium Priority
""")

st.warning("""
🐶 Pet Sitting Needed

📍 Tarnaka

📏 3 KM Away

⚡ Low Priority
""")