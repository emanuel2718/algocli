#!/usr/bin/env python

'''
algocli - Print algorithms to the command line
written by Emanuel Ramirez (emanuel2718@gmail.com)
'''

import argparse
import requests
import util
from bs4 import BeautifulSoup


class DataHandler:
    def __init__(self, algorithm, language=None):
        self.algorithm = algorithm
        self.language = language

        self.fixed_algorithm = self.get_fixed_algorithm(self.algorithm)
        self.fixed_language = self.get_fixed_language(self.language)
        print(self.fixed_language)


    def get_fixed_algorithm(self, algo):
        ''' The rosettacode page address must contain the sorting algorithm in
            a specific format. For example, -insertionsort must appear as Insertion_sort

        :param algo: the algorithm flag string (i.e selectionsort)
        :return formatted algorithm string (i.e Selection_sort)
        '''
        for key, value in util.SORTING_ALGORITHMS.items():
            if algo == key:
                return value[0]
        return None

    def get_fixed_language(self, lang):
        # Python is the default language if no language flag was given
        if lang is None:
            return 'Python'
        for key, value in util.SUPPORTED_LANGUAGES.items():
            if lang == key:
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
    parser = argparse.ArgumentParser(description='Print algorithms to the command line',
                                     usage='algocli [-h] -language -algorithm',
                                     formatter_class=argparse.RawTextHelpFormatter)

    sort_group = parser.add_argument_group('Sorting algorithms (Required)')
    for key, value in util.SORTING_ALGORITHMS.items():
        sort_group.add_argument('-'+key, help=value[1], action='store_true')

    # TODO: offer a pager list of the available algorithms. It makes
    # the parser to long. And future new algorithms (i.e Search Algorithms will have no place)
    lang_group = parser.add_argument_group('Supported languages (Optional) defaults to Python')
    for key, value in util.SUPPORTED_LANGUAGES.items():
        lang_group.add_argument('-'+key, help=value[1], action='store_true')

    return parser

def algoCLI():
    parser = get_parser()
    args = vars(parser.parse_args())

    chosen_language = get_language_from_parser(args)
    chosen_algorithm = get_algorithm_from_parser(args)

    if no_error_in_arguments(chosen_language, chosen_algorithm):
        data_handler = DataHandler(chosen_algorithm, chosen_language)
        #print(f'Language: {chosen_language}')
        #print(f'Algorithm: {chosen_algorithm}')
        #print('No error')
    else:
        exit(1)




if __name__ == '__main__':
    algoCLI()
