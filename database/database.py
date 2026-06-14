import sqlite3

# Connect to database
conn = sqlite3.connect("neighborhelp.db")

# Create cursor
cursor = conn.cursor()

# -----------------------------
# REQUESTS TABLE
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    category TEXT,
    help_type TEXT,
    description TEXT,
    location TEXT,
    radius INTEGER,
    urgency TEXT
)
""")

# -----------------------------
# OFFERS TABLE
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS offers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    title TEXT,
    description TEXT,
    area TEXT,
    radius INTEGER
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("✅ Database Created Successfully!")