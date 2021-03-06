#!/usr/bin/env python

'''Tests for algocli'''
import unittest
from algocli import algocli


class TestAlgocli(unittest.TestCase):

    def setup(self):

        args = {
            'input': ['python', 'insertionsort'],
            'version': False,
            'list_colors': False,
            'list_lang': False,
            'list_algo': False,
            'colorscheme': None
        }
#        self.data_handler = algocli.DataHandler('python', 'insertionsort', args)

if __name__ == '__main__':
    unittest.main()
