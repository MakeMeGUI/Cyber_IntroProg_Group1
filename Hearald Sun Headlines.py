import requests
url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(r_html, features="html.parser")

for title in soup.find_all('h2'):
	print(title.string)

input()