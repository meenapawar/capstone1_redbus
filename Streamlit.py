import streamlit as st
import mysql.connector
import pandas as pd

#Connect to the MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="meena",
        password="Root",
        database="Project"
    )

#Query for the state names
def get_state_names(connection):
    query = "SELECT DISTINCT state_name FROM bus_routes;"  # SQL query for unique state names
    df = pd.read_sql_query(query, connection)
    return df

#Query for route names
def get_routes_by_state(connection, state_name):
    query = f"SELECT DISTINCT route_name, route_link FROM bus_routes WHERE state_name = '{state_name}';"
    df = pd.read_sql_query(query, connection)
    return df

#fetching bus details using state name and route name
def get_the_route_details(connection, state_name, route_name, star_rating):
    query = f"SELECT busname, bustype, departing_time, duration, reaching_time, star_rating, price, seats_available from bus_routes WHERE state_name = '{state_name}' and route_name = '{route_name}' and star_rating >= '{star_rating}%';"
    df = pd.read_sql_query(query, connection)

    if not df.empty:
        df['departing_time'] = df['departing_time'].apply(lambda x: str(x).split()[2] if pd.notnull(x) else None)
        df['reaching_time'] = df['reaching_time'].apply(lambda x: str(x).split()[2] if pd.notnull(x) else None)

        # Convert time strings to the desired format (12-hour format)
        df['departing_time'] = pd.to_datetime(df['departing_time'], format='%H:%M:%S').dt.strftime('%I:%M %p')
        df['reaching_time'] = pd.to_datetime(df['reaching_time'], format='%H:%M:%S').dt.strftime('%I:%M %p')

    return df

# Main function
def main():
    st.header("Bus Details")
    conn = create_connection()

    #Fetch and display state names in the sidebar
    state_data = get_state_names(conn)
    state_names = state_data['state_name'].unique().tolist()
    selected_state = st.sidebar.selectbox("Select a state:", state_names)

    #Fetch and display route names based on the selected state
    if selected_state:
        route_data = get_routes_by_state(conn, selected_state)
        route_names = route_data['route_name'].tolist()
        route_links = route_data['route_link'].tolist()

        # Display the route names in the sidebar
        st.sidebar.write("Routes under selected state:")
        selected_route = st.sidebar.selectbox("Select a route:", route_names)
        # Add a rating filter
        selected_rating = st.sidebar.slider("Minimum Star Rating", min_value=1, max_value=5, value=3)

        # Get the index of the selected route to fetch the corresponding route link
        if selected_route:
            route_index = route_names.index(selected_route)
            selected_link = route_links[route_index]

            # Display the route name and link on the sidebar
            st.sidebar.write(f"Selected Route:{selected_route}")
            st.sidebar.write(f"Route Link:[{selected_route}]({selected_link})")


            bus_details = get_the_route_details(conn, selected_state, selected_route, selected_rating)

            if not bus_details.empty:
                st.write(f"Bus details for {selected_state} - {selected_route}:")
                st.dataframe(bus_details)  # Show the bus details as a table
            else:
                st.write(f"No bus details available for {selected_state} - {selected_route}")

    conn.close()

if __name__ == "__main__":
    main()
