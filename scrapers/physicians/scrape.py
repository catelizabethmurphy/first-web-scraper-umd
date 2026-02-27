import csv
import sys
from datetime import datetime
import requests
from bs4 import BeautifulSoup

all_rows = []
current_year = datetime.now().year

# Check if specific years are provided as command-line arguments
if len(sys.argv) > 1:
    years_to_scrape = [int(year) for year in sys.argv[1:]]
else:
    years_to_scrape = [2017, 2018, 2019, 2021, 2022, 2023, 2024, 2025, 2026]

for year in years_to_scrape:
    print(f"Scraping {year}...")
    try:
        if int(year) == current_year:
            url = 'https://www.mbp.state.md.us/sanctions.aspx'
        else:
            url = f'https://www.mbp.state.md.us/sanctions_{year}.aspx'
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        
        html = response.content

        soup = BeautifulSoup(html, features="html.parser")
        table = soup.find('tbody')
        
        if table is None:
            print(f"Warning: No table found for {year}, skipping...")
            continue

        for row in table.find_all('tr'):
            list_of_cells = []
            list_of_cells.append(year)
            cells = row.find_all('td')
            
            # Check structure: 3 columns (old) or 4 columns (new)
            if len(cells) == 3:
                # Older years: link with name, type, date
                href = cells[0].find('a')['href']
                if href.startswith('http'):
                    list_of_cells.append(href)
                else:
                    list_of_cells.append("https://www.mbp.state.md.us" + href)
                # Name is in the link text
                name = ' '.join(cells[0].find('a').text.split())
                list_of_cells.append(name)
                # Type and date
                for cell in cells[1:3]:
                    text = ' '.join(cell.text.split())
                    list_of_cells.append(text)
            else:
                # Current year: link, name, type, date (4 columns)
                # First cell has the link
                href = cells[0].find('a')['href']
                if href.startswith('http'):
                    list_of_cells.append(href)
                else:
                    list_of_cells.append("https://www.mbp.state.md.us" + href)
                # Process remaining cells (name, type, date)
                for cell in cells[1:4]:
                    text = ' '.join(cell.text.split())
                    list_of_cells.append(text)
            
            all_rows.append(list_of_cells)
    except Exception as e:
        print(f"Error scraping {year}: {e}")
        continue

print(f"\nTotal rows scraped: {len(all_rows)}")

if len(all_rows) == 0:
    print("ERROR: No data was scraped. Exiting without creating empty file.")
    sys.exit(1)

outfile = open("alerts.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["year", "url","name","type","date"])
writer.writerows(all_rows)
outfile.close()

print("Successfully wrote data to alerts.csv")
