# making import statements
import sqlite3

# creating a connection to the db i.e creating or accessing db """db means Database"
connection = sqlite3.connect("test.db")
"""
A cursor can be considered as the walking stick of a blind man i.e 
the user is the blind fellow and the cursor is the stick use to carry out operation
in the db
"""

# creating a cursor
cursor = connection.cursor()

# this is to create a table articles with field id, title content image and date
cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    content TEXT,
                    category TEXT,
                    image TEXT,
                    date_published DATE)''')

# to insert the data inside the table
cursor.execute("INSERT INTO articles (title, content, category, image, date_published) VALUES (?, ?, ?, ?, ?)",
                                   ("title_text", "content_text", 'business', "image", None))

# Tor fetc
cursor.execute("SELECT * FROM articles")
rows = cursor.fetchall()
for row in rows:
    print(row)

# closing the connection
connection.close()