import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python itunes.py <artist>")

artist = sys.argv[1]

response = requests.get(f"https://itunes.apple.com/search?term={artist}&limit=5")

data = response.json()

for result in data["results"]:
    print(result["trackName"])