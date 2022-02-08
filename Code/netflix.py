## Example - Netflix job postings ##

# Capturing the source code #
import requests
html_str = requests.get('https://jobs.lever.co/netflix').text

# Parsing the source code #
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str)

# Job titles #
job = soup.find_all('h5', {'data-qa': 'posting-name'})
len(job)
job[:5]
job[-5:]
job = [j.text for j in job]
job[:5]

# Job location #
location = soup.find_all('span', 'sort-by-location posting-category small-category-label')
location = [l.text for l in location]

# Team #
team = soup.find_all('span', 'sort-by-team posting-category small-category-label')
team = [t.text for t in team]
team = [t.split(' – ') for t in team]
division = [t[0] for t in team]
dept = [t[1] for t in team]

# Links #
id = soup.find_all('div', 'posting')
id = [i['data-qa-posting-id'] for i in id]
link = soup.find_all('a', 'posting-title')
link = [l['href'] for l in link]

# Packing #
import pandas as pd
df = pd.DataFrame({'job': job, 'location': location, 'division': division, 'dept': dept, 'link': link})

# Exporting to CSV file #
df.to_csv('data/netflix/netflix.csv', index=False)
