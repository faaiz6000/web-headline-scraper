# 📰 Web Scraper – BBC News Headlines

This is a beginner-friendly Python project that scrapes the latest news headlines from [BBC News](https://www.bbc.com/news) and saves them into a CSV file. Built as part of my internship at CodeClause.

🎯 Project Aim
To extract current top news headlines from a live website and save them using Python.

🚀 Features
- Automatically connects to the BBC News website
- Finds all major headlines (from `<h3>` tags)
- Saves them into a CSV file named with today's date
- Lightweight and easy to run

 🧰 Technologies Used
- Python 3
- `requests` – to fetch web pages
- `beautifulsoup4` – to parse and extract HTML content
- `csv` and `datetime` – for saving structured data

🛠️ Setup Instructions
1. Clone this repo or download the files
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the script:
   ```
   python news_scraper.py
   ```
4. Check the folder for a CSV file like:
   ```
   headlines_2025-06-03.csv
   ```

📁 Files
- `news_scraper.py` – Main script
- `news_scraper_with_explanation.py` – Fully commented version
- `requirements.txt` – Python dependencies
- `Project_Report_Web_Scraper_Faaiz.pdf` – Project documentation
- `README.md` – 

 👨‍💻 Author
**Faaiz Ahmed Ansari**  
Python Developer Intern @ CodeClause (June 2025)
