# Database Practice :)
import sqlite3
connection = sqlite3.connect("./database.db")
cursor = connection.cursor()
query = """
SELECT product_name, price FROM Products;
"""
result = cursor.execute(query).fetchall()
print(f"OUR SQL RESULT: {result}")
connection.commit() # this commits our changes
connection.close() # this disconnects our connection