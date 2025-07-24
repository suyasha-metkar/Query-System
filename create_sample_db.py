import os
import sqlite3

os.makedirs("data", exist_ok=True) #Checking if data directory exists, if not create it


conn = sqlite3.connect("./data/sample.db") # Connect to the SQLite database and 
cursor = conn.cursor()
        
# Create a sample table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sample (
        id INTEGER PRIMARY KEY,
        product TEXT NOT NULL,
        category TEXT NOT NULL,
        value INTEGER NOT NULL
            )
        ''')
        
# Insert sample data
cursor.executemany('INSERT INTO sample (id, product, category, value) VALUES (?, ?, ?, ?)', [
    (101, 'Chair', 'Furniture', 100),
    (102, 'Table', 'Furniture', 200),
    (103, 'Hammer', 'Tools', 15),
    (104, 'Screwdriver', 'Tools', 10),
    (105, 'Notebook', 'Stationery', 5),
    (106, 'Pen', 'Stationery', 2),
    (107, 'Laptop', 'Electronics', 800),
    (108, 'Smartphone', 'Electronics', 600),
    (109, 'Headphones', 'Electronics', 150),
    (110, 'Monitor', 'Electronics', 300),
    (111, 'Pant', 'Kitchenware', 25),
    (112, 'Plate', 'Kitchenware', 10),
    (113, 'Cup', 'Kitchenware', 5),
    (114, 'Blender', 'Kitchenware', 50),
    (115, 'Book', 'Books', 20),
    (116, 'Magazine', 'Books', 5),
    (117, 'Novel', 'Books', 15),
    (118, 'Textbook', 'Books', 30),
    (119, 'T-shirt', 'Clothing', 15),
    (120, 'Jeans', 'Clothing', 40)
])

conn.commit()
conn.close()

print(f"Database created at ./data/sample.db")

