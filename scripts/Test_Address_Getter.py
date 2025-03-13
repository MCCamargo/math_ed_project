import requests
import csv
import time

def get_location_details_nominatim(query):
    """Fetch latitude, longitude, street, and zip code from Nominatim, with debugging."""
    url = "https://nominatim.openstreetmap.org/search"
    headers = {"User-Agent": "YourAppName/1.0 (your_email@example.com)"}  # Replace with real info
    params = {"q": query, "format": "json", "addressdetails": 1}
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP issues
        data = response.json()
        
        print(f"Query: {query}\nResponse JSON: {data}\n")  # Debugging: Print full response

        if data:
            lat = data[0].get("lat", "N/A")
            lon = data[0].get("lon", "N/A")
            address = data[0].get("address", {})
            street = address.get("road", "N/A")  # Extract street
            zip_code = address.get("postcode", "N/A")  # Extract zip code
            
            return lat, lon, street, zip_code
    except requests.RequestException as e:
        print(f"Request error: {e}")
    
    return "N/A", "N/A", "N/A", "N/A"

def process_csv(input_csv, output_csv):
    """Reads a CSV, gets location details, and writes an updated CSV."""
    with open(input_csv, mode="r", newline="", encoding="utf-8") as infile, \
         open(output_csv, mode="w", newline="", encoding="utf-8") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read header and add new columns
        header = next(reader)
        header.extend(["Latitude", "Longitude", "Street", "ZIP Code"])
        writer.writerow(header)

        # Process each row
        for row in reader:
            if len(row) < 2:  # Skip invalid rows
                continue
            
            school = row[0].strip()
            district = row[1].strip()
            query = f"{school}, {district}"
            
            print(f"Fetching: {query}")  # Log progress
            lat, lon, street, zip_code = get_location_details_nominatim(query)
            
            row.extend([lat, lon, street, zip_code])
            writer.writerow(row)

            time.sleep(1)  # Respect Nominatim's rate limits (1 request/sec)

    print(f"Processing complete! Results saved to {output_csv}")



# Example usage
input_csv = "Arkansas_2023_ACT_Test.csv"  # Input file with School (A) & District (B)
output_csv = "Arkansas_2023_ACT_Test_with_address.csv"  # Output file with lat/lon/street/zip

process_csv(input_csv, output_csv)
