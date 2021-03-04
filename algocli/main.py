#!/usr/bin/env python

'''
algocli - Print algorithms to the command line
written by Emanuel Ramirez (emanuel2718@gmail.com)
'''

import argparse
import requests
import util
from bs4 import BeautifulSoup
from __init__ import __version__

STOP_FLAGS = ['{{out}}', 'Output:']


class DataHandler:
    def __init__(self, algorithm, language, colorized):
        '''
            Example variable values:
                self.language                   =: 'cpp'
                self.algorithm_name             =: 'insertionsort'
                self.sanitized_language         =: 'C.2B.2B'
                self.sanitized_algorithm_name   =: 'Insertion_sort'
                self.formal_language            =: 'C++'
                self.formal_algorithm           =: 'Insertion Sort algorithm'
        '''
        self.language = language
        self.algorithm_name = algorithm

        self.sanitized_language = self.get_sanitized_language()
        self.sanitized_algorithm_name = self.get_sanitized_algorithm_name()

        self.formal_language = util.SUPPORTED_LANGUAGES[self.language][1]
        self.formal_algorithm = util.ALGORITHMS[self.algorithm_name][1]

        self.colorize_output = colorized

        self.data = self._get_data()

        self.section_number, self.formatted_language = self._get_section_and_language()
        self.raw_algorithm_code = self._get_raw_algorithm_code()

        self.output_code = '\n'.join(self._format_code_for_output())
        self._print_code_to_console()

    def _print_banner(self, msg):
        print('\n\n' + '-' * 78)
        print(msg.center(78))
        print('-' * 78 + '\n\n')

    def _get_colored_output(self):
        from pygments import highlight
        from pygments.lexers import get_lexer_by_name
        from pygments.formatters import Terminal256Formatter

        lexer = get_lexer_by_name(self.language, stripall=True)
        formatter = Terminal256Formatter(bg='dark', linenos=False)
        return highlight(self.output_code, lexer, formatter)


    def _print_code_to_console(self):
        if self.output_code != self.raw_algorithm_code:
            if self.colorize_output:
                self.output_code = self._get_colored_output()

            self._print_banner(f'{self.formal_algorithm} using {self.formal_language}')
            print(self.output_code)
            self._print_banner('ALGORITHM OUTPUT ENDS HERE')

        # No modifications done to the raw algorithm means no match was found
        # for that specific language/algorithm
        else:
            _print_error(
                f'No results found for {self.language} using {self.algorithm_name}')

    def get_replacement_chars(self, line):
        return {f'<lang': f'{line.split(">")[-1]}',
                '}</lang>': '}',
                '</pre>': '}',
                '</lang>': f'{line[:-7]}',
                '=={{header': '',
                '===': f'\n{line}\n'
                }

    def _remove_unwated_chars(self, line):
        replacement_chars = self.get_replacement_chars(line)
        for key in replacement_chars.keys():
            if line.startswith(key) or line.endswith(key):
                return self.get_replacement_chars(line)[key]
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

    def _get_url(self):
        return f'https://rosettacode.org/wiki/{self.sanitized_algorithm_name}'

    def _get_code_url(self):
        return (
            f'https://rosettacode.org/mw/index.php?title={self.sanitized_algorithm_name}'
            f'&action=edit&section={self.section_number}')

    def _get_data(self):
        url = self._get_url()
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.find(id='toc')

    def _get_section_and_language(self):
        for category in self.data('li'):
            current_language = category.find('a')['href'].lstrip('#')
            if current_language.lower() == self.sanitized_language.lower():
                section_number = str(category).split('"')[1].split('-')[-1]
                formatted_language = category.find(
                    'span', {'class': 'toctext'}).text
                return section_number, formatted_language
        return None, None

    def _get_raw_algorithm_code(self):
        code_url = self._get_code_url()
        code_page = requests.get(code_url)
        soup = BeautifulSoup(code_page.content, 'html.parser')

        return str(soup.find('textarea').text)

    def get_sanitized_algorithm_name(self):
        ''' The rosettacode page address must contain the sorting algorithm in
            a specific format. For example, -insertionsort must appear as Insertion_sort

        :param algo: the algorithm flag string (i.e selectionsort)
        :return formatted algorithm string (i.e Selection_sort)
        '''
        for key, value in util.ALGORITHMS.items():
            if self.algorithm_name == key:
                return value[0]
        return None

    def get_sanitized_language(self):
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


def _print_error(err):
    print(f'[ERROR] {err}')


def _print_ok(msg):
    print(f'[OK]: {msg}')


def _print_warning(msg):
    print(f'[WARNING] {msg}')


def _print_debug(msg):
    print(f'[DEBUG] {msg}')


def get_language_from_parser(args):
    for lang in util.SUPPORTED_LANGUAGES.keys():
        if args[lang]:
            return lang
    return None


def get_algorithm_from_parser(args):
    for key, value in args.items():
        if key in util.ALGORITHMS.keys() and value:
            return key
    return None


def get_parser():
    parser = argparse.ArgumentParser(
        description='Print algorithms to the command line',
        usage='algocli [-h] -language -algorithm -color',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        '-v',
        '--version',
        help='displays the current version of algocli',
        action='store_true')

    parser.add_argument(
        '-color',
        '--color',
        help='enables colorized output algorithm',
        action='store_true')

    lang_group = parser.add_argument_group(
        'supported languages (Optional) defaults to Python')
    for key, value in util.SUPPORTED_LANGUAGES.items():
        lang_group.add_argument('-' + key, help=value[1], action='store_true')

    algorithm_group = parser.add_argument_group(
        'supported Algorithms (Required)')
    for key, value in util.ALGORITHMS.items():
        algorithm_group.add_argument(
            '-' + key, help=value[1], action='store_true')

    return parser


def algoCLI():
    parser = get_parser()
    args = vars(parser.parse_args())
    colorized = False

    if args['version']:
        print(f'algocli {__version__}')
        return

    chosen_language = get_language_from_parser(args)
    if chosen_language is None:
        _print_warning(
            'No language flag was provided. Using default language: Python')
        chosen_language = 'python'

    chosen_algorithm = get_algorithm_from_parser(args)
    if chosen_algorithm is None:
        _print_error(
            'Algorithm must be provided alongside language flag. Example: algocli -cpp -insertionsort')
        return

    if args['color']:
        colorized = True

    data_handler = DataHandler(chosen_algorithm, chosen_language, colorized)


if __name__ == '__main__':
    algoCLI()
