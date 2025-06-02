# ---------------------------------------------------------------
# Project: Web Scraper - BBC News Headlines
# Author: Faaiz Ahmed Ansari
# Internship: CodeClause (June 2025 - Python Development)
# ---------------------------------------------------------------

# 📌 About:
# This Python script connects to the BBC News website, scrapes the latest headlines,
# and saves them into a CSV file named with the current date.

# Import required libraries
import requests                    # For sending HTTP requests
from bs4 import BeautifulSoup      # For parsing HTML and extracting data
import csv                         # For writing output to CSV file
from datetime import datetime      # For timestamped filenames

# Print a starting message
print("Fetching top BBC news headlines...")

# Define the URL of the target site
url = "https://www.bbc.com/news"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the HTML content into BeautifulSoup for parsing
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <h3> tags, where BBC stores its headlines
    headlines = soup.find_all("h3")

    # Create a CSV filename with today's date
    filename = f"headlines_{datetime.now().strftime('%Y-%m-%d')}.csv"

    # Open the CSV file in write mode
    with open(filename, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])  # Add column name

        # Loop through all found headlines
        for h in headlines:
            text = h.get_text(strip=True)  # Clean the headline text
            if text:
                print(text)                # Print headline to terminal
                writer.writerow([text])   # Write it into CSV

    print(f"✅ Done! Headlines saved in '{filename}'")

else:
    print("❌ Failed to fetch the page. Status code:", response.status_code)

# ---------------------------------------------------------------
# How It Works - Step by Step
# ---------------------------------------------------------------
# 1. requests.get() fetches the HTML page from BBC
# 2. BeautifulSoup parses the HTML to find all <h3> tags
# 3. It gets the text content from each <h3> (which are news titles)
# 4. Each headline is saved into a CSV file using the csv module
# 5. The filename includes today's date for uniqueness

# ---------------------------------------------------------------
# Technologies Used:
# - Python 3
# - requests
# - beautifulsoup4
# - csv, datetime (built-in)

# To Run:
# 1. pip install requests beautifulsoup4
# 2. python news_scraper.py
# ---------------------------------------------------------------
