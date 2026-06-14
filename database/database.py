import sqlite3

# =====================================
# CONNECT DATABASE
# =====================================

conn = sqlite3.connect("neighborhelp.db")

cursor = conn.cursor()

# =====================================
# REQUESTS TABLE
# =====================================

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

# =====================================
# OFFERS TABLE
# =====================================

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

# =====================================
# COMMUNITIES TABLE
# =====================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS communities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    community_name TEXT,
    community_type TEXT,
    contact_person TEXT,
    phone TEXT,
    email TEXT,
    plan TEXT
)
""")

# =====================================
# RATINGS TABLE
# =====================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    helper_name TEXT,
    rating INTEGER,
    feedback TEXT
)
""")

# =====================================
# DIRECT CHAT TABLE
# =====================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requester TEXT,
    helper TEXT,
    sender TEXT,
    message TEXT
)
""")

# =====================================
# SAVE CHANGES
# =====================================

conn.commit()

# =====================================
# CLOSE DATABASE
# =====================================

conn.close()

print("✅ NeighborHelp Database Updated Successfully!")