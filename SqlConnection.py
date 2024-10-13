import pandas as pd
from sqlalchemy import create_engine

#Read the CSV file
csv_file = (r"C:\Users\ramya\PycharmProjects\pythonProject1\RedBus\combined_data.csv")
df = pd.read_csv(csv_file)

#Create a connection to the MySQL database
db_host = 'localhost'
db_user = 'meena'
db_password = 'Root'
db_name = 'Project'

# MySQL connection string format:
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}')

#Insert the data into the `bus_routes` table
df.to_sql('bus_routes', con=engine, if_exists='append', index=False)

print("Data loaded successfully!")
