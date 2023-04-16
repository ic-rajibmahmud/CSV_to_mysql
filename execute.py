import os
import mysql.connector

# Define the database connection parameters
db_config = {
    'user': 'username',
    'password': 'password',
    'host': 'hostname',
    'database': 'dbname',
}

# Define the folder path where the CSV files are located
folder_path = "N:/hsales/"

# Create a MySQL connection
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Get the full path to the CSV file
        file_path = os.path.join(folder_path, filename)
        # Define the MySQL LOAD DATA INFILE statement
        load_data_stmt = f"LOAD DATA INFILE '{file_path}' INTO TABLE table_name FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' "
        # Execute the LOAD DATA INFILE statement
        cursor.execute(load_data_stmt)
        cnx.commit()

# Close the MySQL connection
cursor.close()
cnx.close()
