# capstone1_redbus

# Redbus Data Scraping and Dynamic Filtering

This project scrapes bus route details from Redbus using Selenium and provides a dynamic filtering interface using Streamlit. The data includes bus information from 10 different states and is stored in an SQL database for querying and filtering.

## Project Overview

- **Data Scraping with Selenium**: Scrapes bus details such as state name, route name, route link, bus name, bus type, departure time, duration, arrival time, star rating, price, and seat availability from Redbus for 10 states.
- **Data Combination**: Combines individual state data into a single CSV file.
- **SQL Integration**: Loads the combined CSV into an SQL database.
- **Streamlit Dashboard**: Displays bus routes details in a table with filtering options for state name, route name, and rating.

## Technologies Used

- **Selenium**: For web scraping the bus details from Redbus.
- **Pandas**: For combining and handling CSV files.
- **MySQL**: For storing the bus data.
- **Streamlit**: For creating the web interface to display and filter bus data.

## File Structure

|-- Uttarpradesh.py
|-- SouthBengal.py
|-- Rajasthan.py
|-- Punjab.py
|-- Meghalaya.py
|-- Himachalpradesh.py
|-- Kadamba.py
|-- Kerala.py
|-- Chandigarh.py
|-- Andhra.py
|-- CombinedBusData.py
|-- SqlConnection.py
|-- Streamlit.py

