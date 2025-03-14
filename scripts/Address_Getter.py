import csv
import time
import googlemaps


input_csv = "./AR23/Arkansas_2023_ACT_Test.csv"  # Input file with School (A) & District (B)
output_csv = "./AR23/Arkansas_2023_ACT_Test_with_address.csv"  # Output file with lat/lon/street/zip
state = "Arkansas"  #State 

# Set up Google Maps API client
API_KEY = "API KEY GOES HERE" #Don't run this too many times, I get charged after 3000 queries.
gmaps = googlemaps.Client(key=API_KEY)

def get_location_details_google(query):
    """Fetch latitude, longitude, full street address, ZIP code, and county from Google Maps API."""
    try:
        geocode_result = gmaps.geocode(query)
        if geocode_result:
            location = geocode_result[0]["geometry"]["location"]
            lat, lon = location["lat"], location["lng"]
            
            # Extract address components
            address_components = geocode_result[0].get("address_components", [])
            street_number = ""
            street_name = ""
            zip_code = "N/A"
            county = "N/A"
            
            for component in address_components:
                types = component["types"]
                if "street_number" in types:
                    street_number = component["long_name"]
                if "route" in types:  # Street name
                    street_name = component["long_name"]
                if "postal_code" in types:
                    zip_code = component["long_name"]
                if "administrative_area_level_2" in types:
                    county = component["long_name"]
                    
            full_street_address = f"{street_number} {street_name}".strip()
            return lat, lon, full_street_address, zip_code, county
    except Exception as e:
        print(f"Error fetching details for {query}: {e}")
    return "N/A", "N/A", "N/A", "N/A", "N/A"

def process_csv(input_csv, output_csv,state):
    """Reads a CSV, gets location details, and writes an updated CSV."""
    with open(input_csv, mode="r", newline="", encoding="utf-8") as infile, \
         open(output_csv, mode="w", newline="", encoding="utf-8") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read header and add new columns
        header = next(reader)
        header.extend(["Latitude", "Longitude", "Address", "ZIP Code", "County"])
        writer.writerow(header)

        # Process each row
        for row in reader:
            if len(row) < 2:  # Skip invalid rows
                continue
            
            school = row[0].strip()
            district = row[1].strip()
            query = f"{school}, {district}, {state}"

            print(f"Fetching: {query}")  # Log progress
            lat, lon, street, zip_code, county = get_location_details_google(query)

            row.extend([lat, lon, street, zip_code, county])
            writer.writerow(row)

            time.sleep(0.2)  # Avoid rate limits (Google allows higher throughput)

    print(f"Processing complete! Results saved to {output_csv}")



process_csv(input_csv, output_csv,state)
