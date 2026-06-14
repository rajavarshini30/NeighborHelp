import streamlit as st

st.set_page_config(page_title="Request Help", page_icon="📝")

# Custom Styling
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

.stButton button {
    background: linear-gradient(90deg, #4F46E5, #7C3AED);
    color: white;
    border-radius: 12px;
    border: none;
    height: 50px;
    font-size: 16px;
    font-weight: bold;
    width: 100%;
}

.request-card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.title("📝 Request Help")

st.markdown("""
<div class="request-card">
<h4>Create a Help Request</h4>
</div>
""", unsafe_allow_html=True)

title = st.text_input(
    "📌 Request Title",
    placeholder="Example: Need a Ladder for Painting"
)

category = st.selectbox(
    "🏷️ Select Category",
    [
        "Borrow Item",
        "Tutor Needed",
        "Pet Care",
        "Ride Needed",
        "Household Help",
        "Emergency",
        "Other"
    ]
)

custom_category = ""

if category == "Other":
    custom_category = st.text_input(
        "✏️ Enter Custom Category",
        placeholder="Example: Need a Badminton Partner"
    )

help_type = st.text_input(
    "🤝 Type of Help Needed",
    placeholder="Example: Ladder, Math Tutor, Dog Walker"
)

description = st.text_area(
    "📝 Describe Your Request",
    placeholder="Provide more details..."
)

st.subheader("📍 Location & Radius")

location = st.text_input(
    "Current Location",
    placeholder="Example: Mallapur, Hyderabad"
)

radius = st.slider(
    "Select Help Radius (KM)",
    min_value=1,
    max_value=5,
    value=3
)

urgency = st.radio(
    "⚡ Urgency Level",
    ["Low", "Medium", "High"],
    horizontal=True
)

if st.button("🚀 Submit Request"):

    st.success("Request Submitted Successfully!")

    st.markdown("### 📋 Request Summary")

    st.write("📌 Title:", title)

    if category == "Other":
        st.write("🏷️ Category:", custom_category)
    else:
        st.write("🏷️ Category:", category)

    st.write("🤝 Help Type:", help_type)
    st.write("📝 Description:", description)
    st.write("📍 Location:", location)
    st.write("📏 Radius:", radius, "KM")
    st.write("⚡ Urgency:", urgency)