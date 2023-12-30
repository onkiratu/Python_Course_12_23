import json
import requests
import sys
from urllib.parse import quote_plus

# Check if exactly one argument (search term) is provided
if len(sys.argv) != 2:
    print("Usage: script_name <search_term>")
    sys.exit(1)

# Encode the search term to handle spaces and special characters
search_term = quote_plus(sys.argv[1])

# Construct the URL for the iTunes API request
url = f"https://itunes.apple.com/search?entity=song&limit=50&term={search_term}"

try:
    # Make the API request
    response = requests.get(url)

    # Raise an exception if the request was unsuccessful
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Check if "results" key is in the JSON response
    if "results" in data:
        # Iterate and print each track name
        for result in data["results"]:
            if "trackName" in result:
                print(result["trackName"])
            else:
                print("No track name available")

except requests.RequestException as e:
    print(f"Error while making the request: {e}")
except json.JSONDecodeError:
    print("Error decoding the JSON response")
