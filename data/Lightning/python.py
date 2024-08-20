import os
import pandas as pd

# Replace this with your actual directory path
directory = '/'

# Walk through all files in the directory and subdirectories
for root, _, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".csv"):
            file_path = os.path.join(root, filename)
            
            try:
                # Read the CSV file, skipping the first row if it's empty
                df = pd.read_csv(file_path, header=None, skip_blank_lines=True)
                
                # Add the header to the DataFrame
                df.columns = ["time", "intensity", "x"]
                
                # Write the DataFrame back to the CSV file, including the header
                df.to_csv(file_path, index=False)
                
                print(f"Processed file: {file_path}")
            except Exception as e:
                print(f"Failed to process file: {file_path}. Error: {e}")

print("Headers added to all CSV files successfully.")
