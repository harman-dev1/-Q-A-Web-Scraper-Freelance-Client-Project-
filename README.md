Web Scraping & Data Processing Pipeline

Overview

This project is a complete data pipeline that:

Scrapes question–answer data from a website
Stores the data in Excel format
Merges multiple Excel files into a single dataset
Converts the dataset into JSON format
Applies basic LaTeX formatting to mathematical expressions

The goal is to transform raw web data into a clean, structured, and usable format.

Tech Stack

Python
BeautifulSoup (HTML parsing)
Requests (HTTP requests)
Pandas (data processing)
JSON (data storage)

Project Workflow

1. Web Scraping
Scrapes Q&A data from multiple pages
Extracts:
Questions
Answers
Handles missing data gracefully
2. Data Storage
Stores scraped data into Excel files:
Science2.xlsx
Geography.xlsx
3. Data Merging
Reads multiple Excel files using glob
Combines them into a single dataset
4. JSON Conversion
Converts merged dataset into structured JSON:
combined_data.json
5. LaTeX Formatting
Applies formatting to mathematical expressions:
Multiplication → ×
Division → \frac{}{}
Outputs:
formatted_data_corrected.json

Output Files

Excel files (raw scraped data)
combined_data.json
formatted_data_corrected.json

How to Run

1. Install Dependencies
pip install requests beautifulsoup4 pandas openpyxl
2. Run Scraper
python scraper.py
3. Merge and Convert Data
python merge_to_json.py
4. Apply LaTeX Formatting
python format_latex.py

Notes
Website structure may change, which can break scraping logic
Large number of pages may take time to process
Ensure correct file paths (especially on Windows)
