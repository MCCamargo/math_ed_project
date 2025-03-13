import requests
import csv
import time

# Read input CSV (assumes columns: ID, Latitude, Longitude)
input_file = "./AR23/AR23_Lats_Longs.csv"  # Replace with your file
output_file = "./AR23/AR23_schools_with_tracts.csv"

def get_census_tract(lat, lon):
    url = f"https://geocoding.geo.census.gov/geocoder/geographies/coordinates?x={lon}&y={lat}&benchmark=Public_AR_Current&vintage=Current_Current&layers=10&format=json"
    
    response = requests.get(url)
    response_json = response.json()
    
    if response.status_code == 200:
        if 'Census Block Groups' in response_json['result']['geographies']:
            block_group_info = response_json['result']['geographies']['Census Block Groups'][0]
            tract_id = block_group_info.get('TRACT', 'Not found')  # Get the tract number
            return tract_id
        else:
            return 'No data'
    else:
        return 'Error'

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    header = next(reader) + ["Census Tract"]  # Add new column to header
    writer.writerow(header)

    for row in reader:
        lat, lon = row[1], row[2]  # Adjust column indices as needed
        tract = get_census_tract(lat, lon)
        writer.writerow(row + [tract])
        time.sleep(0.2)  # Prevent rate-limiting (5 requests/sec)

print("Done! Results saved to", output_file)
