import streamlit as st
import sqlite3

st.set_page_config(
    page_title="NeighborHelp Login",
    page_icon="🔐",
    initial_sidebar_state="expanded"
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

    try:

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

            st.session_state["user_email"] = user[2]
            st.session_state["user_name"] = user[1]

            st.success(
                f"✅ Welcome {user[1]}!"
            )

            st.switch_page("pages/02_👤_Profile.py")

        else:

            st.error(
                "❌ Invalid Email or Password"
            )

    except Exception as e:

        st.error(
            f"Database Error: {e}"
        )