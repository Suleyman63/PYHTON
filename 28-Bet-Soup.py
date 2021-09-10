from bs4 import BeautifulSoup

import requests

from csv import writer


base_url = 'http://quotes.toscrape.com/'
response = requests.get(base_url)

soup1 = BeautifulSoup(response.text, 'html.parser')


with open('quotes.csv', 'w') as f:
    csv_w =writer(f)
    header_l = ['AUTHOR', 'QUOTE', 'LINK']
    csv_w.writerow(header_l)


    for quote in soup1.select('.quote'):
        text = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        link = base_url + quote.find('a')['href']
        csv_w.writerow([author, text, link])