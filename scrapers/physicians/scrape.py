import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.mbp.state.md.us/disciplinary.aspx'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    for cell in row.find_all('td'):
        if cell.find('a'):
            list_of_cells.append("https://www.mbp.state.md.us" + cell.find('a')['href'])
        text = cell.text.strip()
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("alerts.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["url", "name", "type", "date"])
writer.writerows(list_of_rows)
