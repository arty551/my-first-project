import requests
from bs4 import BeautifulSoup

# 1. Download the page
url = "https://news.ycombinator.com/"
response = requests.get(url)
html = response.text

# 2. Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# 3. Find all story titles
# On HN, titles are in <span class="titleline"> tags
stories = soup.find_all("span", class_="titleline")

# 4. Print them
print(f"Top {len(stories)} stories on Hacker News:\n")
for i, story in enumerate(stories, 1):
    link = story.find("a")
    title = link.text
    url = link.get("href")
    print(f"{i}. {title}")
    print(f"   {url}\n")
