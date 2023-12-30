import json
import requests
import sys
from urllib.parse import quote_plus

# Exit if the correct number of command-line arguments is not provided
if len(sys.argv) != 2:
    sys.exit()

# URL encode the search term to handle spaces and special characters
search_term = quote_plus(sys.argv[1])

# Construct and make the API request
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + search_term)

# Parse the JSON response
o = response.json()

# Iterate and print each track name
for result in o["results"]:
    print(result["trackName"])
