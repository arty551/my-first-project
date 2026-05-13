import requests
from bs4 import BeautifulSoup

ticker = "AAPL"
url = f"https://finance.yahoo.com/quote/{ticker}/"

# Yahoo blocks plain requests, so pretend to be a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")
print(f"Page length: {len(response.text)} characters")

soup = BeautifulSoup(response.text, "html.parser")

# Find the page title
title = soup.find("title")
print(f"\nPage title: {title.text if title else 'Not found'}")

# Find all <h3> tags (often used for section headers and news titles)
print("\n--- All H3 tags on page ---")
for h3 in soup.find_all("h3")[:10]:
    print(f"- {h3.text.strip()}")
