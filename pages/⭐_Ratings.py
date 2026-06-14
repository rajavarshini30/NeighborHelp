import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Ratings & Trust Score",
    page_icon="⭐"
)

st.title("⭐ Ratings & Trust Score")

st.markdown("""
Rate community helpers and build trust within NeighborHelp.
""")

st.write("---")

# =====================================
# RATING FORM
# =====================================

helper_name = st.text_input(
    "👤 Helper Name",
    placeholder="Example: Ravi Kumar"
)

rating = st.slider(
    "⭐ Rating",
    min_value=1,
    max_value=5,
    value=5
)

feedback = st.text_area(
    "💬 Feedback",
    placeholder="Describe your experience..."
)

if st.button("⭐ Submit Rating"):

    if not helper_name.strip():
        st.error("❌ Please enter Helper Name.")
        st.stop()

    conn = sqlite3.connect("neighborhelp.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO ratings
    (
        helper_name,
        rating,
        feedback
    )
    VALUES (?, ?, ?)
    """,
    (
        helper_name,
        rating,
        feedback
    ))

    conn.commit()
    conn.close()

    st.success("✅ Rating Submitted Successfully!")

st.write("---")

# =====================================
# TRUST SCORE
# =====================================

conn = sqlite3.connect("neighborhelp.db")
cursor = conn.cursor()

cursor.execute("""
SELECT AVG(rating)
FROM ratings
""")

avg_rating = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM ratings
""")

total_reviews = cursor.fetchone()[0]

conn.close()

if avg_rating is None:
    avg_rating = 0

st.subheader("📊 Community Trust Score")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "⭐ Average Rating",
        f"{avg_rating:.1f}/5"
    )

with col2:
    st.metric(
        "📝 Total Reviews",
        total_reviews
    )

st.write("---")

# =====================================
# BADGES
# =====================================

st.subheader("🏆 Trust Badges")

if avg_rating >= 4.5:
    st.success("🥇 Community Hero")

if avg_rating >= 4.0:
    st.info("🤝 Trusted Neighbor")

if total_reviews >= 10:
    st.warning("🚨 Emergency Responder")

if avg_rating < 4:
    st.error("🌱 New Community Member")

st.write("---")

# =====================================
# RECENT REVIEWS
# =====================================

st.subheader("📋 Recent Reviews")

conn = sqlite3.connect("neighborhelp.db")
cursor = conn.cursor()

cursor.execute("""
SELECT helper_name, rating, feedback
FROM ratings
ORDER BY id DESC
LIMIT 5
""")

reviews = cursor.fetchall()

conn.close()

if not reviews:
    st.info("No reviews available yet.")

else:

    for name, rating_value, feedback_text in reviews:

        st.success(f"""
👤 {name}

⭐ Rating: {rating_value}/5

💬 {feedback_text}
""")