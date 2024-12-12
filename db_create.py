import sqlite3

# Step 1: Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("bus_routes.db")  # Creates a file named 'bus_routes.db'
cursor = conn.cursor()

# Step 2: Create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS BusDetails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    state TEXT,
    route_name TEXT,
    route_link TEXT,
    bus_name TEXT,
    bus_type TEXT,
    departing_time TEXT,
    duration TEXT,
    reaching_time TEXT,
    star_rating TEXT,
    price TEXT,
    seat_availability TEXT
);
"""

cursor.execute(create_table_query)  # Execute the SQL command

# Step 3: Commit the changes and close the connection
conn.commit()  # Save the changes
conn.close()   # Close the database connection

print("Table created successfully!")


