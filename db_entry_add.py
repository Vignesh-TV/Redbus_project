import sqlite3

def add_bus_entry(entry):
    """
    Inserts a new bus entry into the BusDetails table in the SQLite database.
    """
    #state,route_name, route_link, bus_name, bus_type, departing_time, duration, reaching_time, star_rating, price, seat_availability
    # Connect to the SQLite database (create if it doesn't exist)
    conn = sqlite3.connect("bus_routes.db")
    cursor = conn.cursor()
    try:
    # SQL query to insert the new entry
        insert_query = """
            INSERT INTO BusDetails (state, route_name, route_link, bus_name, bus_type, departing_time, duration, reaching_time, star_rating, price, seat_availability)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        
        # Execute the insert query with the provided data
        cursor.execute(insert_query, (
            entry['state'],
            entry['route_name'],
            entry['route_link'],
            entry['bus_name'],
            entry['bus_type'],
            entry['departing_time'],
            entry['duration'],
            entry['reaching_time'],
            entry['star_rating'],
            entry['price'],
            entry['seat_availability']
        ))    
    except Exception as e:
            print(f"Error occurred in db{str(e)}")
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    print("Entry added successfully!")
