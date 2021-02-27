''' This is a test version for the future update of Algocli'''
import requests
from bs4 import BeautifulSoup


url = 'https://rosettacode.org/wiki/Insertion_sort#Python'
#url = 'https://rosettacode.org/mw/index.php?title=External_sort&action=edit&section=8'
#url = 'https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Insertion_sort#Python'
#url = 'https://en.wikibooks.org/w/index.php?title=Algorithm_Implementation/Sorting/Insertion_sort&action=edit&section=21'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='toc')

wanted_language = 'Scala'
for cat in results('li'):
    section_number = str(cat).split('"')[1].split('-')[-1]
    current_language = cat.find('a')['href'].lstrip('#')

    if wanted_language.lower() == current_language.lower():
        print(f'Language: {current_language}')
        print(f'Section: {section_number}')

