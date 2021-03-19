#!/usr/bin/env python

'''Tests for algocli'''
import unittest
from algocli import algocli


class TestAlgocli(unittest.TestCase):

    def setUp(self):
        args = {
            'input': ['python', 'insertionsort'],
            'version': False,
            'list_colors': False,
            'list_lang': False,
            'list_algo': False,
            'colorscheme': None
        }
        #self.data_handler = algocli.DataHandler('python', 'insertionsort', args)
        #
        #
    def test_evenNumber(self):
        '''Test Number is even'''
        num = 4
        self.assertTrue(num % 2 == 0)
        print(self._testMethodName)

    def test_oddNumber(self):
        '''Test Number is even'''
        num = 5
        self.assertTrue(num % 2 != 0)
        print(self._testMethodName)

    # TODO: test different request (i.e Main page, coding page)
    #       test replacement chars
    #       test EVERYTHING!

if __name__ == '__main__':
    unittest.main(verbosity=2)
