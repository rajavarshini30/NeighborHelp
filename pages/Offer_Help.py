import streamlit as st

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
        "🏠 Household Help",
        "💻 Tech Support",
        "🎨 Skill Training",
        "Other"
    ]
)

custom_service = ""

if help_category == "Other":
    custom_service = st.text_input(
        "Enter Your Service"
    )

service_title = st.text_input(
    "Service Title",
    placeholder="Example: Mathematics Tutor"
)

description = st.text_area(
    "Describe Your Service"
)

availability = st.multiselect(
    "Available Days",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
)

area = st.text_input(
    "Area",
    placeholder="Example: Habsiguda"
)

radius = st.slider(
    "Service Radius (KM)",
    1,
    5,
    3
)

if st.button("🚀 Publish Service"):

    st.success("Service Published Successfully!")

    st.markdown("### Service Summary")

    if help_category == "Other":
        st.write("Category:", custom_service)
    else:
        st.write("Category:", help_category)

    st.write("Title:", service_title)
    st.write("Description:", description)
    st.write("Available Days:", availability)
    st.write("Area:", area)
    st.write("Radius:", radius, "KM")