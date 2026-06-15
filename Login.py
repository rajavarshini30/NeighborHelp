import streamlit as st
import sqlite3

st.set_page_config(
    page_title="NeighborHelp Login",
    page_icon="🔐"
)

st.title("🔐 NeighborHelp Login")

st.info("""
Demo Accounts

👤 Raja Varshini
📧 varshini@gmail.com
🔑 1234

👤 Ravi Kumar
📧 ravi@gmail.com
🔑 1234
""")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    conn = sqlite3.connect("neighborhelp.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE email = ?
        AND password = ?
        """,
        (email, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        st.success(
            f"✅ Welcome {user[1]}!"
        )

        st.switch_page("pages/👤_Profile.py")

    else:

        st.error(
            "❌ Invalid Email or Password"
        )