# Complexities
CONSTANT = 'O(1)'
LOGARITHMIC = 'O(log(N))'
LINEAR = 'O(N)'
NLOGN = 'O(Nlog(N))'
CUADRATIC = 'O(N\u00b2)'
CUBIC = 'O(N\u00b3)'

def print_algorithm_info(algorithm=None, complexity=None):
    if algorithm is not None:
        return (f'Algorithm: {algorithm}\n'
                f'Complexity: {complexity}\n')



information = {"binarysearch": print_algorithm_info('Binary Search', LOGARITHMIC),
               "bubblesort": print_algorithm_info('Bubble Sort', CUADRATIC),
               "insertionsort": print_algorithm_info('Insertion Sort', LINEAR),
               "mergesort": print_algorithm_info('Merge Sort', NLOGN),
               "quicksort":     print_algorithm_info('Quick Sort', NLOGN),
               "selectionsort": print_algorithm_info('Selection Sort', CUADRATIC),
               "stoogesort": print_algorithm_info('Stooge Sort', CUADRATIC)
               }
