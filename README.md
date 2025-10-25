# Automated Google Interaction Bot

Selenium + BeautifulSoup system that performs structured Google searches in a VM and exports cleaned SERP data to CSV.

## Features
- Headless Chrome automation
- Explicit waits and error logging
- CSV output with title, url, snippet, rank

## Usage
1. python -m venv venv
2. source venv/bin/activate or venv\Scripts\activate
3. pip install -r requirements.txt
4. python main.py --queries queries.txt
