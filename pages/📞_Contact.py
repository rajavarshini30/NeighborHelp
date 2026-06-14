import streamlit as st

st.set_page_config(
    page_title="Contact Us",
    page_icon="📞"
)

st.title("📞 Contact Us")

st.write("Send feedback, suggestions, or report issues.")

st.write("---")

name = st.text_input(
    "Your Name"
)

email = st.text_input(
    "Email Address"
)

message = st.text_area(
    "Your Message"
)

if st.button("📨 Send Message"):

    if not name.strip():
        st.error("Please enter your name.")
        st.stop()

    if not email.strip():
        st.error("Please enter your email.")
        st.stop()

    if not message.strip():
        st.error("Please enter a message.")
        st.stop()

    st.success("✅ Message Sent Successfully!")

st.write("---")

st.caption(
    "NeighborHelp © 2026 | Community Support Platform"
)