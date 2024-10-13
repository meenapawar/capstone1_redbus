import pandas as pd
import os

folder_path = (r"C:\Users\ramya\PycharmProjects\pythonProject1\RedBus")

dataframes = []

# Loop through all CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        # Read each CSV file and append it to the list
        df = pd.read_csv(file_path)
        #print(df)
        dataframes.append(df)

# Combine all dataframes into a single one
combined_Bus_data = pd.concat(dataframes, ignore_index=True)

# Save the combined data into a new CSV file
combined_Bus_data.to_csv("combined_data.csv", index=False)
