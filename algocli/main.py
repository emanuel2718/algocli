#!/usr/bin/env python

'''
algocli - Print algorithms to the command line
written by Emanuel Ramirez (emanuel2718@gmail.com)
'''

import argparse
import requests
import util
from bs4 import BeautifulSoup

STOP_FLAGS = ['{{out}}', 'Output:']


class DataHandler:
    def __init__(self, algorithm, language):
        self.language = language
        self.algorithm_name = algorithm

        self.fixed_language = self.get_fixed_language()
        self.fixed_algorithm_name = self.get_fixed_algorithm_name()

        self.data = self._get_data()

        self.section_number, self.formatted_language = self._get_section_and_language()
        self.raw_algorithm_code = self._get_raw_algorithm_code()

        self.clean_code = '\n'.join(self._format_code_for_output())
        self._print_code_to_console()

    def _print_code_to_console(self):
        print('\n-------------------------------------------------------------\n')
        print(self.clean_code)
        print('\n-------------------------------------------------------------\n')

    def get_replacement_chars(self, line):
        return {f'<lang {self.language}>': f'{line.split(">")[-1]}',
                '}</lang>': '}',
                '</pre>': '}',
                '</lang>': f'{line[:-7]}'
                }

    def _remove_unwated_chars(self, line):
        replacement_chars = self.get_replacement_chars(line)
        for key in replacement_chars.keys():
            if line.startswith(key) or line.endswith(key):
                return self.get_replacement_chars(line)[key]
                #return replacement_chars[key]
        return line

    def _format_code_for_output(self):
        result = []
        code = self.raw_algorithm_code.split('\n')

        for line in code:
            if line in STOP_FLAGS:
                return result
            else:
                line = self._remove_unwated_chars(line)
                result.append(line)

        return result

    def _get_data(self):
        url = f'https://rosettacode.org/wiki/Sorting_algorithms/{self.fixed_algorithm_name}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.find(id='toc')

    def _get_section_and_language(self):
        for category in self.data('li'):
            current_language = category.find('a')['href'].lstrip('#')
            if current_language.lower() == self.fixed_language.lower():
                section_number = str(category).split('"')[1].split('-')[-1]
                formatted_language = category.find(
                    'span', {'class': 'toctext'}).text
                return section_number, formatted_language
        return None, None

    def _get_raw_algorithm_code(self):
        code_url = (
            f'https://rosettacode.org/mw/index.php?title=Sorting_algorithms/'
            f'{self.fixed_algorithm_name}&action=edit&section={self.section_number}')
        code_page = requests.get(code_url)
        soup = BeautifulSoup(code_page.content, 'html.parser')

        return str(soup.find('textarea').text)

    def get_fixed_algorithm_name(self):
        ''' The rosettacode page address must contain the sorting algorithm in
            a specific format. For example, -insertionsort must appear as Insertion_sort

        :param algo: the algorithm flag string (i.e selectionsort)
        :return formatted algorithm string (i.e Selection_sort)
        '''
        for key, value in util.SORTING_ALGORITHMS.items():
            if self.algorithm_name == key:
                return value[0]
        return None

    def get_fixed_language(self):
        ''' To get the data some language are reprensented in different in the
            rosettacode website. For example, C++ is reprenseted as C.2B.2B in the page source

            Python is the default language if no language flag was given

        :param algo: the language flag string (i.e csharp)
        :return formatted language string (i.e C.23)
        '''
        if self.language is None:
            return 'Python'
        for key, value in util.SUPPORTED_LANGUAGES.items():
            if self.language == key:
                return value[0]
        return None


def get_language_from_parser(args):
    for lang in util.SUPPORTED_LANGUAGES.keys():
        if args[lang]:
            return lang
    return None


def get_algorithm_from_parser(args):
    for key, value in args.items():
        if key in util.SORTING_ALGORITHMS.keys() and value:
            return key
    return None


def no_error_in_arguments(lang, algo):
    if lang is None:
        print('Warning: No language flag was provided. Using default language: Python')

    if lang is not None and algo is None:
        print('Error: Algorithm must be provided alongside language flag. Example: algocli -cpp -insertionsort')
        return False
    return True


def get_parser():
    parser = argparse.ArgumentParser(
        description='Print algorithms to the command line',
        usage='algocli [-h] -language -algorithm',
        formatter_class=argparse.RawTextHelpFormatter)

    sort_group = parser.add_argument_group('Sorting algorithms (Required)')
    for key, value in util.SORTING_ALGORITHMS.items():
        sort_group.add_argument('-' + key, help=value[1], action='store_true')

    # TODO: offer a pager list of the available algorithms. It makes
    # the parser to long. And future new algorithms (i.e Search Algorithms
    # will have no place)
    lang_group = parser.add_argument_group(
        'Supported languages (Optional) defaults to Python')
    for key, value in util.SUPPORTED_LANGUAGES.items():
        lang_group.add_argument('-' + key, help=value[1], action='store_true')

    return parser


def algoCLI():
    parser = get_parser()
    args = vars(parser.parse_args())

    chosen_language = get_language_from_parser(args)
    if chosen_language is None:
        print('Warning: No language flag was provided. Using default language: Python')
        chosen_language = 'python'

    chosen_algorithm = get_algorithm_from_parser(args)
    if chosen_algorithm is None:
        print('Error: Algorithm must be provided alongside language flag. Example: algocli -cpp -insertionsort')
        sys.exit(1)

    data_handler = DataHandler(chosen_algorithm, chosen_language)



if __name__ == '__main__':
    algoCLI()
