''' This is a test version for the future update of Algocli'''
import requests
from bs4 import BeautifulSoup

sec_number = ''
#TODO: check Bubble sort exception
wanted_language = 'Lua'
#wanted_language = 'Rust'
sort_method = 'Insertion_sort'
current_language = ''
formatted_language = ''

url = f'https://rosettacode.org/wiki/{sort_method}'
#url = 'https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Insertion_sort#Python'
#url = 'https://en.wikibooks.org/w/index.php?title=Algorithm_Implementation/Sorting/Insertion_sort&action=edit&section=21'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='toc')

dividers = '---------------------------'

#print(results)
#exit(0)

for cat in results('li'):
    #print(cat)
    section_number = str(cat).split('"')[1].split('-')[-1]
    current_language = cat.find('a')['href'].lstrip('#')
    if current_language == wanted_language:
        formatted_language = cat.find('span', {'class': 'toctext'}).text

    if wanted_language.lower() == current_language.lower():
        sec_number = section_number
        #print(f'Language: {current_language}')
        #print(f'Section: {section_number}')



#print(f'Section number: {sec_number}')
code_url = f'https://rosettacode.org/mw/index.php?title=Sorting_algorithms/{sort_method}&action=edit&section={sec_number}'
code_page = requests.get(code_url)
sp = BeautifulSoup(code_page.content, 'html.parser')

#print(sp.prettify())
res = str(sp.find('textarea').text)

#unwanted_chars = ['=={{header|%s}}=='.format(wanted_language),
                  #'<lang %s'.format(wanted_language.lower())]
#reformat_header_language = {
#    'C.2B.2B' : 'C++'
#}
#
reformat_lang_language = {
    'C++' : 'cpp'
}

replacement_chars = {
    f'=={{header|{formatted_language}}}==' : f'{dividers} {formatted_language} {dividers}\n',
    #f'<lang {reformat_lang_language[formatted_language]}>' : '',
    '<lang cpp>' : '',
    '}</lang>' : '}',
}


stopping_char = '{{out}}'

def remove_unwated_chars(line):
    # check for lang line
    # check for header line
    for key in replacement_chars.keys():
        #print(f'Line: {line} and Key: {key}')
        if line.startswith('<lang'):
            #print(f'Replacing {line} with {line.split(">")[1]}')
            return line.split('>')[1]
        elif line.endswith('</lang>'):
            return line.split('<')[0]
    return line

def format_code(code):
    result = []
    code = code.split('\n')
    for chunk in code:
        if chunk == stopping_char:
            return result
        #if chunk in replacement_chars.keys():
        #    result.append(replacement_chars[chunk])
        else:
            chunk = remove_unwated_chars(chunk)
            result.append(chunk)
    return result


final = '\n'.join(format_code(res))
print(final)

#print(res)
# TODO: Clean this mess
#string = res.split('==')[2]
#string = string.replace('&gt;', '>')
#string = string.replace('&lt;', '<')
#string = string.replace('&gt;=', '>=')
#string = string.replace('&lt;=', '<=')
#string = string.replace('&lt;/lang&gt;', ' ')
#string = string.replace(f'&lt;lang {wanted_language.lower()}>', '')
#print(string)
