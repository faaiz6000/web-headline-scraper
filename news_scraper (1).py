# news_scraper.py

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Print start message
print("Fetching top BBC news headlines...")

# Define the URL
url = "https://www.bbc.com/news"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find headline tags (class names can change, so check the page manually too)
    headlines = soup.find_all("h3")  # H3 tags usually contain headlines

    # Create a CSV file with current date
    filename = f"headlines_{datetime.now().strftime('%Y-%m-%d')}.csv"

    # Open the file in write mode
    with open(filename, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])  # Column title

        # Loop through and write each headline
        for h in headlines:
            text = h.get_text(strip=True)
            if text:
                writer.writerow([text])

    print(f"Done! Headlines saved in '{filename}'")
else:
    print("Failed to fetch the page. Status code:", response.status_code)
