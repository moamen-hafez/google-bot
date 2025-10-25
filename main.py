# google-bot/main.py
import time, csv, argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def run_query(driver, query):
    driver.get("https://www.google.com/search?q=" + query)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    results = []
    for g in soup.select("div.g")[:10]:
        title = g.select_one("h3")
        link = g.select_one("a")
        snippet = g.select_one(".VwiC3b")
        if title and link:
            results.append({
                "title": title.get_text(strip=True),
                "url": link.get('href'),
                "snippet": snippet.get_text(strip=True) if snippet else ""
            })
    return results

def main(queries):
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    try:
        with open("results.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["title","url","snippet"])
            writer.writeheader()
            for q in queries:
                for r in run_query(driver, q):
                    writer.writerow(r)
    finally:
        driver.quit()

if __name__ == "__main__":
    main(["example query"])
