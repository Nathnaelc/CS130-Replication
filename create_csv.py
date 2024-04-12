import pandas as pd

# Path to the Excel file
excel_file_path = 'filtered_regions.xlsx'

# Output CSV file path
output_csv_path = 'merged_csv.csv'

# List of sheet names corresponding to regions for 'People' as identified before
sheet_names = ['neast_p', 'nwest_p', 'ykhu_p', 'emids_p',
               'wmids_p', 'east_p', 'lon_p', 'seast_p', 'swest_p', 'eng_p']

# Dictionary to map sheet names to more friendly region names
region_names = {
    'neast_p': 'North East',
    'nwest_p': 'North West',
    'ykhu_p': 'Yorkshire and The Humber',
    'emids_p': 'East Midlands',
    'wmids_p': 'West Midlands',
    'east_p': 'East of England',
    'lon_p': 'London',
    'seast_p': 'South East',
    'swest_p': 'South West',
    'eng_p': 'England'
}

# Initialize an empty DataFrame to hold all the data
all_data_combined = pd.DataFrame()

# Iterate through each sheet name, read the data, add a 'Region' column, and concatenate
for sheet_name in sheet_names:
    # Read the sheet data into a DataFrame
    sheet_data = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    # Rename the columns based on your provided format
    sheet_data.columns = [
        'Date',
        'All aged 16 & over',
        'Total economically active',
        'Total in employment',
        'Unemployed',
        'Economically inactive',
        'Economic activity rate (%)',
        'Employment rate (%)',
        'Unemployment rate (%)',
        'Economic inactivity rate (%)',
        'All aged 16 to 64',
        'Total economically active (16 to 64)',
        'Total in employment (16 to 64)',
        'Unemployed (16 to 64)',
        'Economically inactive (16 to 64)',
        'Economic activity rate (%) (16 to 64)',
        'Employment rate (%) (16 to 64)',
        'Unemployment rate (%) (16 to 64)',
        'Economic inactivity rate (%) (16 to 64)'
    ]

    # Insert the 'City' column with the mapped region name
    sheet_data.insert(0, 'City', region_names[sheet_name])

    # Insert the 'Treated' column with the appropriate flag (0 for control, 1 for treated - London is treated)
    sheet_data['Treated'] = 0 if sheet_name != 'lon_p' else 1

    # Append the DataFrame to the combined data DataFrame
    all_data_combined = pd.concat(
        [all_data_combined, sheet_data], ignore_index=True)

# Add a column name for the date column
all_data_combined.columns = ['Date'] + list(all_data_combined.columns[1:])

# Save the combined DataFrame to a CSV file
all_data_combined.to_csv(output_csv_path, index=False)

print(f"The combined data has been saved to {output_csv_path}")
