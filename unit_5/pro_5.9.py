'''#Write a program to create a list with 3 columns for name, data type and size. Create table as per the information entered. Consider following example
name varchar 20
qualification varchar 20
post varchar 20
salary int 6
Once above information is stored in list, program shall create a table from above information.'''

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

columns = [
    ("name", "VARCHAR", 20),
    ("qualification", "VARCHAR", 20),
    ("post", "VARCHAR", 20),
    ("salary", "INT", 6)
]

table_name = "employee"


query = f"CREATE TABLE {table_name} ("

for col in columns:
    col_name, dtype, size = col
    query += f"{col_name} {dtype}({size}), "

query = query.rstrip(", ") + ")"

cursor.execute(query)

print("Table created successfully!")


conn.close()
