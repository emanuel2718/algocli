''' This is a test version for the future update of Algocli'''
import requests
from bs4 import BeautifulSoup

sec_number = ''
#TODO: check Bubble sort exception
sort_method = 'Shell_sort'

url = f'https://rosettacode.org/wiki/{sort_method}#Python'
#url = 'https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Insertion_sort#Python'
#url = 'https://en.wikibooks.org/w/index.php?title=Algorithm_Implementation/Sorting/Insertion_sort&action=edit&section=21'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='toc')

wanted_language = 'Python'
for cat in results('li'):
    section_number = str(cat).split('"')[1].split('-')[-1]
    current_language = cat.find('a')['href'].lstrip('#')

    if wanted_language.lower() == current_language.lower():
        sec_number = section_number
        #print(f'Language: {current_language}')
        #print(f'Section: {section_number}')



code_url = f'https://rosettacode.org/mw/index.php?title=Sorting_algorithms/{sort_method}&action=edit&section={sec_number}'
code_page = requests.get(code_url)
sp = BeautifulSoup(code_page.content, 'html.parser')

#print(sp.prettify())
res = str(sp.find('textarea'))
# TODO: Clean this mess
string = res.split('==')[2]
string = string.replace('&gt;', '>')
string = string.replace('&gt;=', '>=')
string = string.replace('&lt;/lang&gt;', ' ')
string = string.replace(f'&lt;lang {wanted_language.lower()}>', '')
print(string)
