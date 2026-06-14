import streamlit as st

st.title("👤 My Profile")

st.image(
    "https://cdn-icons-png.flaticon.com/512/149/149071.png",
    width=120
)

name = st.text_input("Name", "Raja")
age = st.number_input("Age", min_value=16, max_value=100, value=20)

phone = st.text_input("Phone Number")

st.subheader("⭐ Trust Score")

trust_score = 75

st.progress(trust_score/100)

st.success(f"Trust Score: {trust_score}/100")

st.subheader("🏆 Badges")

st.write("🥇 Helpful Neighbor")
st.write("⭐ Trusted Member")
st.write("🤝 Community Supporter")