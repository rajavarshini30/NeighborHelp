import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Direct Help Chat",
    page_icon="💬"
)

st.title("💬 Direct Help Chat")

st.write("Connect requesters and helpers.")

st.write("---")

# ==========================
# CHAT PARTICIPANTS
# ==========================

requester = st.text_input(
    "Requester Name",
    placeholder="Example: Varshini"
)

helper = st.text_input(
    "Helper Name",
    placeholder="Example: Ravi"
)

sender = st.selectbox(
    "Sending As",
    [
        "Requester",
        "Helper"
    ]
)

message = st.text_area(
    "Type your message",
    height=100,
    placeholder="Enter your message..."
)

# ==========================
# SEND MESSAGE
# ==========================

if st.button("📨 Send Message"):

    if not requester.strip():
        st.error("❌ Enter requester name.")
        st.stop()

    if not helper.strip():
        st.error("❌ Enter helper name.")
        st.stop()

    if not message.strip():
        st.error("❌ Message cannot be empty.")
        st.stop()

    actual_sender = requester if sender == "Requester" else helper

    conn = sqlite3.connect("neighborhelp.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chat_messages
    (
        requester,
        helper,
        sender,
        message
    )
    VALUES (?, ?, ?, ?)
    """,
    (
        requester,
        helper,
        actual_sender,
        message
    ))

    conn.commit()
    conn.close()

    st.toast("📨 Message Sent!")

st.write("---")

# ==========================
# CHAT HISTORY
# ==========================

if requester and helper:

    st.subheader("💬 Conversation")

    conn = sqlite3.connect("neighborhelp.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT sender, message
    FROM chat_messages
    WHERE requester = ?
    AND helper = ?
    ORDER BY id ASC
    """,
    (
        requester,
        helper
    ))

    chats = cursor.fetchall()

    conn.close()

    if not chats:
        st.info("No messages yet.")

    else:

        for sender_name, msg in chats:

            with st.chat_message("user"):
                st.write(f"**{sender_name}:**")
                st.write(msg)

st.write("---")

st.info(
    "💡 Enter the same Requester and Helper names to continue an existing conversation."
)