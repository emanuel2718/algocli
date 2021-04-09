#!/usr/bin/env python

'''Tests for algocli'''
import unittest
from algocli import algocli
from algocli import util


class TestAlgocli(unittest.TestCase):

    #def setUp(self):
    #    self.args = {
    #        'input': None,
    #        'version': False,
    #        'list_colors': False,
    #        'list_lang': False,
    #        'list_algo': False,
    #        'colorscheme': None,
    #    }

    #    self.data_handler = algocli.DataHandler(self.args, 'insertionsort', 'cpp')
    #    self.sanitized_algorithm_name = 'Sorting_algorithms/Insertion_sort'
    #    self.section_number = '23'

    #def test_get_url(self):
    #    ''' Test valid base url is returned
    #        Search: `algocli insertionsort cpp`
    #    '''
    #    valid_url = f'https://rosettacode.org/wiki/{self.sanitized_algorithm_name}'
    #    self.assertTrue(valid_url == self.data_handler.get_url())
    #    print(self._testMethodName)

    #def test_get_code_url(self):
    #    ''' Test valid code url is returned
    #        Search: `algocli insertionsort cpp`
    #    '''
    #    valid_code_url = (
    #        f'https://rosettacode.org/mw/index.php?title='
    #        f'{self.sanitized_algorithm_name}&action=edit&section={self.section_number}')

    #    self.assertTrue(valid_code_url == self.data_handler.get_code_url())
    #    print(self._testMethodName)


    #def test_python_algorithms(self):
    #    import os
    #    with open('results.txt', 'w') as output_file:
    #        for algo in util.ALGORITHMS.keys():
    #            print(f'Testing: algocli {algo} python', end='')
    #            try:
    #                os.system(f'python -m algocli {algo} python --file')
    #                print(': OK!\n')
    #            except:
    #                print(': Failed!')

    def test_all_algorithms(self):
        import os
        with open('results.txt', 'w') as output_file:
            for lang in util.SUPPORTED_LANGUAGES:
                print(f'\n----- *{lang.upper()}* -----\n')
                for algo in util.ALGORITHMS.keys():
                    print(f'Testing: algocli {algo} {lang}', end='')
                    try:
                        os.system(f'python -m algocli {algo.upper()} {lang.upper()} --file')
                        print(': OK!\n')
                    except:
                        print(': Failed!')




if __name__ == '__main__':
    unittest.main(verbosity=2)
