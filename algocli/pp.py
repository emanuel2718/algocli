''' This is a test version for the future update of Algocli'''
import re
import markdown_strings
import json
import requests
from bs4 import BeautifulSoup
import html2text
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options


sec_number = ''
#TODO: check Bubble sort exception
sort_method = 'Shell_sort'

url = f'https://rosettacode.org/wiki/Sorting_algorithms/{sort_method}'
#url = f'https://rosettacode.org/wiki/{sort_method}#Python'
#url = f'https://rosettacode.org/wiki/{sort_method}#Python'
#url = 'https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Insertion_sort#Python'
#url = 'https://en.wikibooks.org/w/index.php?title=Algorithm_Implementation/Sorting/Insertion_sort&action=edit&section=21'

#path = 'c:/bin/chromedriver.exe'
#options = Options()
#browser = webdriver.Chrome(path, options=options)
#browser.get(url)
#
#html = browser.page_source
#print(html)


page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
#result = soup.find(title='Edit section: Python')
#result = soup.findAll('div', {'class': 'examplemeta translation'})

spans = soup.findAll('span', {'class': 'mw-headline'})
# TODO: make a try/except when returned list is empty: example 'java' & 'java5'
code = soup.findAll('pre', {'class': 'python highlighted_source'})

special_char = ' {0xSpace} '

def format_line(line):
    result = []
    s = line.split()
    for i, word in enumerate(s):
        if word == special_char.strip(' '):
            if i != 0:
                if s[i-1] == special_char.strip(' '):
                    result.append('  ')
                else:
                    result.append('\n')
        else:
            result.append(word)

    #print(result)
    #for i in result:
    #    print(i, end=' ')

    return result

def display_output(code):
    print('\n------------------------------------------------')
    for line in code:
        print(line, end=' ')
    print('\n')
    print('------------------------------------------------')

for i, line in enumerate(code):
    text = str(line.text.replace('  ', special_char))
    f_line = format_line(str(text))
    display_output(f_line)
    #text = str(line.text.replace('    ', '\n'))
    #print(markdown_strings.code_block(text, 'python'))
    #line = line.text.split()
    #for word in line:
    #    if word.endswith(':'):
    #        print(word, end=' ')
    #        print('\n')
    #        print('    ', end='')

    #    else:
    #        print(word, end=' ')
    #print(line.text.split())

#h = html2text.HTML2Text()
#
#for line in code:
#    print(h.handle(line))



#result = []
#for i, lst in enumerate(code):
#    lst = str(lst).split('<')
#    for line in lst:
#        print(line)
#        if line.startswith('span') or line.startswith('/span'):
#            l = line.split('>')[1]
#            result.append(l)
#        if line.startswith('br/>'):
#            result.append('\n')
#for word in result:
    #print(word, end='')




# ----------------------------------------------------------------------------------
# TODO: This semi works
#code = soup.findAll('pre', {'class': 'text highlighted_source'}) # TODO: This works
#count = 1
#for i, lst in enumerate(code):
#    for line in lst:
#        if not '<br/>' in str(line).split():
#            print(line)
#    print('\n')
#    count += 1
#
#print(f'Counter: {count}')
# ----------------------------------------------------------------------------------









        #print(str(word).split())
        #if '<br>' in word or '</br>' in word:
            #print('BR FOUND')


#count = 1
#for sec in code:
#    for word in sec:
#        if word is not None:
#            word = str(word).replace('<br>', '')
#            word = str(word).replace('</br>', '')
#            print(word)
#            #print(type(word))
#            #print(str(word))
#
#print(f'Count: {count}')

#count = 1
#for i in range(len(spans)):
#    print(result[i])
#    print('\n')
#    count += 1
#
#print(f'Counter: {count}')

#print(result.find(title='Edit section'))
#result = soup.findAll('pre', {'class': 'text highlighted_source'})
#result = soup.findAll('div')
#result = soup.findAll(id='Python')
#print(result)

#count = 1
#for line in result:
#    print(line.contents)
#    #print(line.contents)
#    print(f'Counter: {count}')
#    print('\n')
#    count += 1


#for line in result:
#    print(line)
#    print('\n')


#print(soup)

#print(soup.prettify())
#result = soup.findAll('span', {'class': 'mw-editsection-bracket'})
#result = soup.find(id='Python')
#print(result)
#results = soup.find(id='toc')
#result = soup.findAll('pre', {'class': 'text highlighted_source'})
#result = soup.find('div')


#print(result)
#for i in result:
    #print(i.find('div'))
    #print('\n')
#result = soup.find('div')
#
#print(result)

#for ele in result:
    #print(ele)
    #print('\n')


#print(result.findAll('pre', {'class': 'text highlighted_source'}))

#wanted_language = 'Python'
#for cat in results('li'):
#    section_number = str(cat).split('"')[1].split('-')[-1]
#    current_language = cat.find('a')['href'].lstrip('#')
#
#    if wanted_language.lower() == current_language.lower():
#        sec_number = section_number
#        #print(f'Language: {current_language}')
#        #print(f'Section: {section_number}')
#
#
#
#code_url = f'https://rosettacode.org/mw/index.php?title=Sorting_algorithms/{sort_method}&action=edit&section={sec_number}'
#code_page = requests.get(code_url)
#sp = BeautifulSoup(code_page.content, 'html.parser')
#
##print(sp.prettify())
#res = str(sp.find('textarea'))
## TODO: Clean this mess
#string = res.split('==')[2]
#string = string.replace('&gt;', '>')
#string = string.replace('&gt;=', '>=')
#string = string.replace('&lt;/lang&gt;', ' ')
#string = string.replace(f'&lt;lang {wanted_language.lower()}>', '')
#print(string)
