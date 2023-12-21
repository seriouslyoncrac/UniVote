import sqlite3
import hashlib  # Used for hashing the admin password

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('user_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table for users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT,
        is_admin INTEGER DEFAULT 0
    )
''')

# Insert normal users (numbers 1-50)
for user_id in range(1, 51):
    cursor.execute('''
        INSERT INTO users (username) VALUES (?)
    ''', (f'user{user_id}',))

# Insert admin user (username 'admin' with a hashed password)
admin_password = 'admin_password'  # Change this to a secure password
hashed_password = hashlib.sha256(admin_password.encode()).hexdigest()
cursor.execute('''
    INSERT INTO users (username, password_hash, is_admin) VALUES (?, ?, 1)
''', ('admin', hashed_password))

# Commit the changes and close the connection
conn.commit()
conn.close()
