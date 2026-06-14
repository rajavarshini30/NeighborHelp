import streamlit as st

st.title("🤲 Offer Help")

skill = st.text_input(
    "What Help Can You Offer?"
)

description = st.text_area(
    "Describe Your Offer"
)

availability = st.selectbox(
    "Availability",
    [
        "Weekdays",
        "Weekends",
        "Anytime"
    ]
)

locality = st.text_input(
    "Your Locality"
)

if st.button("Post Offer"):
    st.success("✅ Offer Posted Successfully!")

    st.write("### Offer Details")
    st.write("Skill:", skill)
    st.write("Description:", description)
    st.write("Availability:", availability)
    st.write("Locality:", locality)