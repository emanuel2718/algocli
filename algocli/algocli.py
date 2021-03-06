#!/usr/bin/env python

'''
algocli - print common algorithms via the command line
written by Emanuel Ramirez (emanuel2718@gmail.com)
'''

import argparse
import util
from bs4 import BeautifulSoup
from contextlib import closing
from requests import get
from requests.exceptions import RequestException
from time import time
from __init__ import __version__

STOP_FLAGS = ["'''Library'''"]

BOLD = '\033[1m'
ITALIC = '\033[3m'
END = '\033[0m'

STACK = []
SKIP = ['<pre>']
END_SKIP = ['</pre>']

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
                         'AppleWebKit/537.36 (KHTML, like Gecko) '\
                         'Chrome/75.0.3770.80 Safari/537.36'}


class DataHandler:
    def __init__(self, algorithm, language, args):
        '''
            Example variable values:
                self.language                   =: 'cpp'
                self.algorithm_name             =: 'insertionsort'
                self.sanitized_language         =: 'C.2B.2B'
                self.sanitized_algorithm_name   =: 'Insertion_sort'
                self.formal_language            =: 'C++'
                self.formal_algorithm           =: 'Insertion Sort algorithm'
        '''
        self.start_time = time()
        self.language = language
        self.algorithm_name = algorithm

        self.sanitized_language = self.get_sanitized_language()
        self.sanitized_algorithm_name = self.get_sanitized_algorithm_name()

        self.formal_language = util.SUPPORTED_LANGUAGES[self.language][1]
        self.formal_algorithm = util.ALGORITHMS[self.algorithm_name][1]

        self.args = args

        self.data = self._get_data(self.get_url(), True)

        self.section_number, self.formatted_language = self._get_section_and_language()
        self.raw_algorithm_code = self._get_data(self.get_code_url())

        self.output_code = '\n'.join(self._format_code_for_output())
        self._print_code_to_console()
        self.display_tip_if_applicable()
        _print_debug(f'Time taken: {time()-self.start_time:.04} seconds')

    def _print_banner(self, msg):
        print('\n\n' + '=' * 70)
        print(msg.center(70))
        print('=' * 70 + '\n\n')

    def _get_colored_output(self):
        from pygments import highlight
        from pygments.lexers import get_lexer_by_name
        from pygments.formatters import Terminal256Formatter

        theme = self.args['colorscheme']
        user_style = theme if theme in util.COLORS else 'default'
        lexer = get_lexer_by_name(self.language, stripall=True)
        formatter = Terminal256Formatter(bg='dark', linenos=False, style=user_style)
        return highlight(self.output_code, lexer, formatter)

    def display_tip_if_applicable(self):
        if self.args['colorscheme'] not in util.COLORS:
            _print_tip(f'"algocli --list-colors" for available colorschemes\n')


    def _print_code_to_console(self):
        if not self.output_code.startswith('{{task'):
            self._print_banner(f'{self.formal_algorithm} using {self.formal_language}')

            if self.args['no_color']:
                print(self.output_code)
            else:
                print(self._get_colored_output())

            self._print_banner('ALGORITHM OUTPUT ENDS HERE')

        # No modifications done to the raw algorithm means no match was found
        # for that specific language/algorithm
        else:
            _print_error(
                f'No results found for {self.formal_algorithm} using {self.formal_language}')

    def get_replacement_chars(self, line):
        return {f'<lang': f'{line.split(">", 1)[-1]}',
                '}</lang>': '}',
                '}</pre>': '}',
                '</pre>': '',
                '<pre': '',
                '{{works': '',
                '</lang>': f'{line.partition("</")[0]}',
                '=={{header': '',
                '===': f'\n{line}\n',
                '{{trans': '',
                '<br>': '',
                '{{Out}}': '\n=== Output ===',
                '{{out}}Output': f'\n=== {line.rpartition("}")[-1]} ===',
                '{{out}}': '',
                '{{libheader': '',
                'Output:': '',
                "'''Output'''": '',
                "'''": f'\n{line}',
                'Usage:': "\n\n'''How to use'''"
                }

    def _remove_unwated_chars(self, line):
        replacement_chars = self.get_replacement_chars(line)
        for key in replacement_chars.keys():
            if line.startswith(key) or line.endswith(key):
                return self.get_replacement_chars(line)[key]
        return line

    def is_valid_line(self, line):
        if line.startswith('<pre>') and line.endswith('</pre>'):
            return False
        if line.startswith('<pre>'):
            STACK.append('<pre>')
            return False

        if len(STACK) == 0:
            return True

        if line.endswith('</pre>'):
            STACK.pop()
            return False

    def _format_code_for_output(self):
        result = []
        code = self.raw_algorithm_code.split('\n')

        for line in code:
            if line in STOP_FLAGS:
                return result
            else:
                if self.is_valid_line(line):
                    line = self._remove_unwated_chars(line)
                    result.append(line)
        return result

    def get_url(self):
        return f'https://rosettacode.org/wiki/{self.sanitized_algorithm_name}'

    def get_code_url(self):
        return (
            f'https://rosettacode.org/mw/index.php?title={self.sanitized_algorithm_name}'
            f'&action=edit&section={self.section_number}')


    def _get_data(self, url, code=False):
        '''code := the request is for the final algorithm code'''
        try:
            with closing(get(url, headers=HEADERS, stream=True, timeout=5)) as response:
                if self.is_valid_response(response):
                    if code:
                        return BeautifulSoup(response.content, 'html.parser').find(id='toc')
                    return str(BeautifulSoup(response.content, 'html.parser').find('textarea').text)
                else:
                    return None
        except RequestException as e:
            _print_error(e)
            return None

    def is_valid_response(self, resp):
        content_type =  resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)


    def _get_section_and_language(self):
        for category in self.data('li'):
            current_language = category.find('a')['href'].lstrip('#')
            if current_language.lower() == self.sanitized_language.lower():
                section_number = str(category).split('"')[1].split('-')[-1]
                formatted_language = category.find(
                    'span', {'class': 'toctext'}).text
                return section_number, formatted_language
        return None, None


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

def _print_tip(msg):
    print(f'{BOLD}[TIP]{END} {msg}')


def _print_error(err):
    print(f'{BOLD}[ERROR]{END} {err}')


def _print_warning(msg):
    print(f'{BOLD}[WARNING]{END} {msg}')


def _print_ok(msg):
    print(f'{BOLD}[OK]{END} {msg}')


def _print_debug(msg):
    print(f'{BOLD}[DEBUG]{END} {msg}')


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
        description='print common algorithms via the command line',
        usage='algocli [-h] [-v] [-algorithm] [-language] [--color COLORSCHEME] [--no-color] [--list-colors] '
              '[--list-lang] [--list-algo]',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        '-v',
        '--version',
        help='displays the current version of algocli',
        action='store_true')

    parser.add_argument(
        '--no-color',
        help='black and white output',
        action='store_true')

    parser.add_argument(
        '--list-colors',
        help='print list of available colorschemes',
        action='store_true')

    parser.add_argument(
        '--list-lang',
        help='print list of supported languages',
        action='store_true')

    parser.add_argument(
        '--list-algo',
        help='print list of supported algorithms',
        action='store_true')

    parser.add_argument(
        '--color',
        help='colorized output',
        nargs='?',
        dest='colorscheme',
        const='default',
        metavar='COLORSCHEME')


    lang_group = parser.add_argument_group(
        'optional supported languages (Defaults to Python)')
    for key, value in util.SUPPORTED_LANGUAGES.items():
        lang_group.add_argument('-' + key, help=value[1], action='store_true')

    algorithm_group = parser.add_argument_group(
        'required supported algorithms')
    for key, value in util.ALGORITHMS.items():
        algorithm_group.add_argument(
            '-' + key, help=value[1], action='store_true')

    return parser

def show_colorschemes():
    print('\nAvailable Colorschemes: [Example: algocli -binarysearch -python --color zenburn]')
    for i, color in enumerate(util.COLORS, start=1):
        print(f'- {color}')
    print()

def print_list(msg, arr):
    print('\n' + msg)
    for item in arr:
        print(f'- {item}')
    print()

def run():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(f'algocli {__version__}')
        return

    if args['list_colors']:
        print_list('Supported Colorscemes: [Example: algocli -b64 -python --color rrt]',
                    util.COLORS)
        #show_colorschemes()
        return

    if args['list_lang']:
        print_list('Supported Languages flags:', util.SUPPORTED_LANGUAGES)
        return

    if args['list_algo']:
        print_list('Supported Algorithms flags:', util.ALGORITHMS)
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

    #if args['colorscheme'] not in util.COLORS:
        #_print_warning('Color not found. Using default colorscheme.')

    data_handler = DataHandler(chosen_algorithm, chosen_language, args)


if __name__ == '__main__':
    run()
