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



"""TO ADD MULTIPLE DATA IN THE db"""
# make your import
import sqlite3

# create a connection e.g test.db
connection = sqlite3.connect("test.db")

# create a cursor, this allows us work with daatabase
cursor = connection.cursor()

# create a table Table - 1
cursor.execute("create table gta (release_year integer, relase_name text, city text)")

# create a table Table - 2
cursor.execute("create table city (gta_city text, real_city text)")


# The raw data
release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto II", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]


# adding multiple data to the data base
cursor.executemany("insert into gta values (?,?,?)", release_list)

cursor.execute("insert into gta values (?,?)", ("Liberty City", ))


# To select from 
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})

gta_search = cursor.fetchall()
print(gta_search)

print("\n")
# print database 
for row in cursor.execute("select * from gta"):
    print(row)

# close your connection
connection.close