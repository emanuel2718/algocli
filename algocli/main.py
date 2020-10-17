#!/usr/bin/python3

# Program: algocli
# Author: Emanuel Ramirez Alsina (eramirez)
# Date created: 10/10/2020


import algocli.algorithms as algorithms
import algocli.util as util

import argparse
import sys

SUPPORTED_LANGUAGES = ['cpp', 'java', 'python']

def show_available_algorithms():
    # TODO: implement this (Pager?)
    print('Showing available algorithms')

def check_for_language_flag(args_dict):
    """
    @args_dict: dictionary of possible command-line arguments
    return: language if the language flag was received from cli argument
            None if no language flag was received
    """
    for language in SUPPORTED_LANGUAGES:
        if args_dict[language]:
            return language
    return None

def get_algorithm_from_parser(args):
    """
    @args: dictionary of possible command-line arguments.
    return: algorithm from cli-argument
            None if no algorithm flag was received
    """
    for key, value in args.items():
        if value and not key in SUPPORTED_LANGUAGES:
            return key
    return None

def argument_error_checker(language, algorithm):
    # TODO: raise exceptions and Errors
    if language is None:
        print('Warning: No language flag was provided. Using default language: Python')
    if language is not None and algorithm is None:
        print('Error: Algorithm must be provided alongside language flag. Example: algocli -cpp -insertionsort')
        return False
    return True

def print_algorithm_to_cli(algorithm):
    #print('\n----------------------------------------\n')
    print('\n' + '-'*80 + '\n')
    # TODO: Time complexity will be optional
    print(util.information[algorithm])
    print(algorithms.functions[algorithm])
    print('\n' + '-'*80 + '\n')
    #print('----------------------------------------\n')


def get_parser():
    parser = argparse.ArgumentParser(description='Print algorithms to the command line', usage='algocli [-h] -cpp -quicksort')
    parser.add_argument('-l', '--list', help='Show List of available algorithm', action='store_true')
    parser.add_argument('-c', '--complexity', help='Show time and space complexities of the algorithm', action='store_true')

    lang_group = parser.add_argument_group('supported languages (Optional) defaults to Python')
    lang_group.add_argument('-cpp', '--cpp', help='Show algorithm in C++', action='store_true')
    lang_group.add_argument('-java', '--java', help='Show algorithm in Java', action='store_true')
    lang_group.add_argument('-python', '--python', help='Show algorithm in Python', action='store_true')

    sort_group = parser.add_argument_group('Sorting algorithms (Required)')
    sort_group.add_argument('-bubblesort', help='Bubble Sort algorithm', action='store_true')
    sort_group.add_argument('-insertionsort', help='Insertion Sort algorithm', action='store_true')
    sort_group.add_argument('-mergesort', help='Merge Sort algorithm', action='store_true')
    sort_group.add_argument('-quicksort', help='Quick Sort algorithm', action='store_true')
    sort_group.add_argument('-selectionsort', help='Selection Sort algorithm', action='store_true')
    sort_group.add_argument('-stoogesort', help='Stooge Sort algorithm', action='store_true')

    search_group = parser.add_argument_group('Searching algorithms (Required)')
    search_group.add_argument('-binarysearch', help='Binary Search algorithm', action='store_true')

    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    # TODO: Check if user asked for -list or -h or something else
    if args['list']:
        show_available_algorithms()
        return

    chosen_language = check_for_language_flag(args)
    chosen_algorithm = get_algorithm_from_parser(args)

    if argument_error_checker(chosen_language, chosen_algorithm):
        # TODO: Need to get think about how to call the correct language/algorithm
        print_algorithm_to_cli(chosen_algorithm)


if __name__ == '__main__':
    # TODO: Handle errors
    # TODO: Expand to other languages (need to refactor the file structure (folder per language))
    main()
