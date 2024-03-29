import requests
from bs4 import BeautifulSoup

# URL of the web page you want to scrape
url = 'http://10.10.173.212'

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links in the HTML content
links = soup.find_all('a')

# Write the extracted data to a file
with open('output.txt', 'w') as file:
    for link in links:
        href = link.get('href')
        # Check if the href attribute is not None and is not an empty string
        if not href.isspace():
            file.write(href + '\n')

print('Data extracted and saved to output.txt')
