## Tutorial - Beautiful Soup ##

# Toy example #
html_str = '<html> \
  <head> \
  <title>Data Viz</title> \
  </head> \
  <body> \
  <div class="course">Data Visualization</div> \
  <div class="program">MBA full-time</div> \
  <a class="professor" \
  href="https://www.iese.edu/faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a> \
  </body> \
  </html>'
html_str

# Parsing HTML code #
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')
type(soup)
soup

# The method find #
soup.find('head')
type(soup.find('head'))
soup.find('head').find('title')
soup.find('head').find('div')
soup.find('head').find('div') == None
soup.find('div')
soup.find('div', {'class': 'course'})
soup.find('div', 'program')

# The method find_all #
soup.find_all('div')
soup.find('head').find_all('div')
soup.find_all('div', 'course')
soup.find_all('div', 'course')[0]

# Extracting information from a tag element #
soup.find('a').text
soup.find_all('div').text
[t.text for t in soup.find_all('div')]
soup.find('a')['href']

