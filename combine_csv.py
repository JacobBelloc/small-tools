import os
import glob
import csv

# Define the path to the directory containing the CSV files
dir_path = 'data/'

# Create a list of all CSV files in the directory
csv_files = glob.glob(os.path.join(dir_path, '*.csv'))

# Open the output CSV file for writing
with open('combined_data.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Loop over each CSV file and write its contents to the output file
    for file in csv_files:
        with open(file, 'r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                writer.writerow(row)
