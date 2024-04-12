import pandas as pd

# Load the dataset directly from the provided URL
data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSN9Kubs9hmW0rcwICMv9id9UFnhRnIPPLy4VnfBsIImd5iKSAApMiILQEiOfrb43Lk76P4HhKTyUHU/pub?gid=1041933585&single=true&output=csv"
data = pd.read_csv(data_url)

# Make 'Year' is of integer type for accurate comparison
data['year'] = data['year'].astype(int)

# Keep data for years between 1993 and 2021 (inclusive)
data = data[(data['year'] >= 1993) & (data['year'] < 2022)]

# Aggregating monthly data into yearly by taking the mean for each year-region combination
yearly_data = data.groupby(['region', 'year']).mean().reset_index()

# Adding RegionID
# Make London is sorted first and assigned 1, followed by other regions
regions_sorted = sorted(
    yearly_data['region'].unique(), key=lambda x: (x != 'London'))
region_id_mapping = {region: idx + 1 for idx,
                     region in enumerate(regions_sorted)}
yearly_data['RegionID'] = yearly_data['region'].map(region_id_mapping)

# Reordering the dataframe so that London (RegionID == 1) comes first
yearly_data = yearly_data.sort_values(['RegionID', 'year'])

# Save the prepared data to a new CSV file locally
cleaned_csv_path = 'final_merged_yearly_csv.csv'
yearly_data.to_csv(cleaned_csv_path, index=False)

print(f"Yearly aggregated data saved to {cleaned_csv_path}")
