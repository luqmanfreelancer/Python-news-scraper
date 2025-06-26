import requests
from bs4 import BeautifulSoup

# Target URL
url = 'https://www.bbc.com/news'

# Send HTTP request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all headline tags
headlines = soup.find_all('h3')

print("📰 Top BBC News Headlines:\n")

# Print headlines
for i, headline in enumerate(headlines[:10], 1):
    print(f"{i}. {headline.text.strip()}")