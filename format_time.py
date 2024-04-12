import csv

# Input and output file paths
input_file = 'merged_csv.csv'
output_file = 'updated_merged_csv.csv'

# Read the CSV file
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Update the header
data[0][1] = 'Year'

# Update the date format in the 'Year' column
for row in data[1:]:
    date_str = row[1]
    year = date_str.split()[-1]
    row[1] = year

# Write the updated data to a new CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Updated CSV file saved as '{output_file}'.")
