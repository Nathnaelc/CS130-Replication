import pandas as pd

# Path to the Excel file
excel_file_path = 'regionaltable1s.xlsx'

# Initialize pandas ExcelFile object
xls = pd.ExcelFile(excel_file_path)

# List all sheet names
all_sheet_names = xls.sheet_names
print("All Sheet Names:")
print(all_sheet_names)

# Filter out sheets based on your criteria
# Keeping only those that end with '_p' (indicating "People")
# and exclude regions not part of England
regions_to_exclude = ['neast_p', 'nwest_p', 'ykhu_p', 'emids_p', 'wmids_p', 'east_p',
                      'lon_p', 'seast_p', 'swest_p', 'eng_p']

sheets_to_keep = [sheet for sheet in regions_to_exclude]

sheets_to_drop = [
    sheet for sheet in all_sheet_names if sheet not in sheets_to_keep]

for sheet in sheets_to_drop:
    all_sheet_names.remove(sheet)

# Create a list to store the filtered sheets
filtered_sheets = []

# Load each sheet that you want to keep into a pandas DataFrame and append it to the list
for sheet in sheets_to_keep:
    df = xls.parse(sheet)
    filtered_sheets.append(df)

# Create a new Excel file using the ExcelWriter object
with pd.ExcelWriter('filtered_regions.xlsx') as writer:
    # Write each DataFrame in the filtered_sheets list to a separate sheet in the new Excel file
    for i, df in enumerate(filtered_sheets):
        df.to_excel(writer, index=False, sheet_name=f'Sheet_{i}')

print("\nFiltered Sheet Names to Keep:")
print(sheets_to_keep)
