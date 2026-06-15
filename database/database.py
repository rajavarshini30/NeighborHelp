import sqlite3

conn = sqlite3.connect("neighborhelp.db")
cursor = conn.cursor()

# =====================================
# USERS
# =====================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")

# Demo Users
cursor.execute("""
INSERT OR IGNORE INTO users
(full_name, email, password)
VALUES
('Raja Varshini', 'varshini@gmail.com', '1234')
""")

cursor.execute("""
INSERT OR IGNORE INTO users
(full_name, email, password)
VALUES
('Ravi Kumar', 'ravi@gmail.com', '1234')
""")

# =====================================
# REQUESTS
# =====================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS requests(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    location TEXT
)
""")

# =====================================
# OFFERS
# =====================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS offers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    area TEXT
)
""")

# =====================================
# COMMUNITIES
# =====================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS communities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    community_name TEXT,
    community_type TEXT,
    plan TEXT
)
""")

# =====================================
# RATINGS
# =====================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    helper_name TEXT,
    rating INTEGER,
    feedback TEXT
)
""")

# =====================================
# CHAT MESSAGES
# =====================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_messages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requester TEXT,
    helper TEXT,
    sender TEXT,
    message TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully.")