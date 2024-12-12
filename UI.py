# Import necessary libraries
import streamlit as st
import sqlite3
import pandas as pd

# Function to fetch bus data from the database
def fetch_bus_data():
    # Connect to the SQLite database (replace "bus_routes.db" with your database file)
    conn = sqlite3.connect("bus_routes.db")
    cursor = conn.cursor()

    # SQL query to select all rows from the BusDetails table
    cursor.execute("SELECT * FROM BusDetails")
    rows = cursor.fetchall()

    # Get the column names of the table
    cursor.execute("PRAGMA table_info(BusDetails)")
    columns = [description[1] for description in cursor.fetchall()]

    # Convert the rows into a Pandas DataFrame for easier handling and display
    df = pd.DataFrame(rows, columns=columns)

    # Close the connection to the database
    conn.close()

    # Return the DataFrame
    return df

# Main function for the Streamlit app
def createUi():
    # Set the title of the app
    st.title("Bus Routes Data")

    # Fetch the data from the database using the fetch_bus_data function
    df = fetch_bus_data()

    # Check if we got any data from the database
    if df.empty:
        st.write("No data available in the database.")
    else:
        # Filter by State
        states = df['state'].unique()
        state_filter = st.selectbox("Select a State to Filter by", states)

        # Filter data based on the selected state
        df_state_filtered = df[df['state'] == state_filter]

        # Filter by Bus Type (dynamically based on selected state)
        bus_types = df_state_filtered['bus_type'].unique()
        bus_type_filter = st.selectbox("Select Bus Type", bus_types)

        # Filter data based on the selected bus type
        df_bus_type_filtered = df_state_filtered[df_state_filtered['bus_type'] == bus_type_filter]

        # Filter by Route Name (dynamically based on selected bus type)
        route_names = df_bus_type_filtered['route_name'].unique()
        route_name_filter = st.selectbox("Select Route Name", route_names)

        # Filter data based on the selected route name
        df_route_filtered = df_bus_type_filtered[df_bus_type_filtered['route_name'] == route_name_filter]

        # Filter by Star Rating (dynamically based on selected route name)
        star_ratings = df_route_filtered['star_rating'].unique()
        star_rating_filter = st.selectbox("Select Star Rating", star_ratings)

        # Filter data based on the selected star rating
        df_star_filtered = df_route_filtered[df_route_filtered['star_rating'] == star_rating_filter]

        # Display the filtered data
        if df_star_filtered.empty:
            st.write("No bus routes found for the selected filters.")
        else:
            st.write("Here is the data for your selected filters:")
            st.dataframe(df_star_filtered)


createUi()