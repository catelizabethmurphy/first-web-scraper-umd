import csv
import sys
from datetime import datetime
import requests
from bs4 import BeautifulSoup

all_rows = []
current_year = datetime.now().year
for year in range(2021, 2027):
    print(f"Scraping {year}...")
    if int(year) == current_year:
        url = 'https://www.mbp.state.md.us/sanctions.aspx'
    else:
        url = f'https://www.mbp.state.md.us/sanctions_{year}.aspx'
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    html = response.content

    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find('tbody')

    for row in table.find_all('tr'):
        list_of_cells = []
        list_of_cells.append(year)
        for cell in row.find_all('td'):
            if cell.find('a'):
                href = cell.find('a')['href']
                if href.startswith('http'):
                    list_of_cells.append(href)
                else:
                    list_of_cells.append("https://www.mbp.state.md.us" + href)
            else:
                text = ' '.join(cell.text.split())
                list_of_cells.append(text)
        all_rows.append(list_of_cells)
    
outfile = open("alerts.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["year", "url","name","type","date"])
writer.writerows(all_rows)
