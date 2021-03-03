# Complexities
CONSTANT = 'O(1)'
LOGARITHMIC = 'O(log(N))'
LINEAR = 'O(N)'
NK = 'O(NK)'
NLOGN = 'O(Nlog(N))'
CUADRATIC = 'O(N\u00b2)'
NLOGNSQUARED = 'O(NLOG(N)\u00b2)'
CUBIC = 'O(N\u00b3)'
NFACTORIAL = 'N * N!'

# def print_algorithm_info(algorithm=None, complexity=None):
#    if algorithm is not None:
#        return (f'Algorithm: {algorithm}\n'
#                f'Complexity: {complexity}\n')
#
#
#
# information = {"binarysearch": print_algorithm_info('Binary Search', LOGARITHMIC),
#               "bogosort": print_algorithm_info('Bogo Sort', NFACTORIAL),
#               "bubblesort": print_algorithm_info('Bubble Sort', CUADRATIC),
#               "cocktailsort": print_algorithm_info('Cocktail Sort', CUADRATIC),
#               "cyclesort": print_algorithm_info('Cycle Sort', CUADRATIC),
#               "gnomesort": print_algorithm_info('Gnome Sort', CUADRATIC),
#               "heapsort": print_algorithm_info('Heap Sort', NLOGN),
#               "insertionsort": print_algorithm_info('Insertion Sort', LINEAR),
#               "mergesort": print_algorithm_info('Merge Sort', NLOGN),
#               "quicksort":     print_algorithm_info('Quick Sort', NLOGN),
#               "radixsort":     print_algorithm_info('Radix Sort', NK),
#               "selectionsort": print_algorithm_info('Selection Sort', CUADRATIC),
#               "shellsort": print_algorithm_info('Shell Sort', NLOGNSQUARED),
#               "stoogesort": print_algorithm_info('Stooge Sort', CUADRATIC)
#               }


''' The keys in this dictionary will represent the command line arguments that the user
    inputs to select the desired algorithm:
        i.e algocli -insertionsort

    The values need to match the formatting of rosettacode sorting page address tail because it varies
    from sorter to sorter. It's also case sensitive. For example:
        Insertion sort: https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort <---
        Heap sort: https://rosettacode.org/wiki/Sorting_algorithms/Heapsort <----
'''
ALGORITHMS = {
    'avltrees': ['AVL_tree', 'AVL Trees'],
    'binarysearch': ['Binary_search', 'Binary Search algorithm'],
    'base64': ['Base64_decode_data', 'Decode Base64 data'],
    'beadsort': ['Sorting_algorithms/Bead_sort', 'Bead Sort algorithm'],
    'bogosort': ['Sorting_algorithms/Bogo_sort', 'Bogo Sort algorithm'],
    'bubblesort': ['Sorting_algorithms/Bubble_sort', 'Bubble Sort algorithm'],
    'caesarcipher': ['Sorting_algorithms/Caesar_cipher', 'Caesar Cipher'],
    'cocktailsort': ['Sorting_algorithms/Cocktail_sort', 'Cocktail Sort algorithm'],
    'combsort': ['Sorting_algorithms/Comb_sort', 'Comb Sort algorithm'],
    'countingsort': ['Sorting_algorithms/Counting_sort', 'Counting Sort algorithm'],
    'cyclesort': ['Sorting_algorithms/Cycle_sort', 'Cycle Sort algorithm'],
    'e': ['Calculating_the_value_of_e', 'Calculate the value of e'],
    'fileexist': ['Check_that_file_exists', 'Check if a given file exists or not'],
    'gnomesort': ['Sorting_algorithms/Gnome_sort', 'Gnome Sort algorithm'],
    'heapsort': ['Sorting_algorithms/Heapsort', 'Heap Sort algorithm'],
    'insertionsort': ['Sorting_algorithms/Insertion_sort', 'Insertion Sort algorithm'],
    'mergesort': ['Sorting_algorithms/Merge_sort', 'Merge Sort algorithm'],
    'pancakesort': ['Sorting_algorithms/Pancake_sort', 'Pancake Sort algorithm'],
    'patiencesort': ['Sorting_algorithms/Patience_sort', 'Patience Sort algorithm'],
    'permutationsort': ['Sorting_algorithms/Permutation_sort', 'Permutation Sort algorithm'],
    'quicksort': ['Sorting_algorithms/Quicksort', 'Quick Sort algorithm'],
    'radixsort': ['Sorting_algorithms/Radix_sort', 'Radix Sort algorithm'],
    'selectionsort': ['Sorting_algorithms/Selection_sort', 'Selection Sort algorithm'],
    'shellsort': ['Sorting_algorithms/Shell_sort', 'Shell Sort algorithm'],
    'sleepsort': ['Sorting_algorithms/Sleep_sort', 'Sleep Sort algorithm'],
    'stoogesort': ['Sorting_algorithms/Stooge_sort', 'Stooge Sort algorithm'],
    'strandsort': ['Sorting_algorithms/Strand_sort', 'Strand Sort algorithm']
}


#SORTING_ALGORITHMS = [
#    'beadsort',
#    'bogosort',
#    'bubblesort',
#    'cocktailsort',
#    'combsort',
#    'countingsort',
#    'cyclesort',
#    'gnomesort',
#    'heapsort',
#    'insertionsort',
#    'mergesort',
#    'pancakesort',
#    'patiencesort',
#    'permutationsort',
#    'quicksort',
#    'radixsort',
#    'selectionsort',
#    'shellsort',
#    'sleepsort',
#    'stoogesort',
#    'strandsort'
#]


''' If the user input a language flag in the cli arguments the it will be valid if it exists
    as in the keys of this dictionary and if the value language is found for the requested sorter.

    Supported languages. Some lanagues (like Java) in different sorter pages will appear as java or java5
'''
# TODO: Fix the first entry of the values it must match the page source name!!!
SUPPORTED_LANGUAGES = {
    'actionscript': ['ActionScript', 'Actionscript'],
    'ada': ['Ada', 'Ada'],
    'algol68': ['ALGOL_68', 'ALGOL68'],
    'applescript': ['AppleScript', 'Applescript'],
    'arm': ['ARM_Assembly', 'ARM Assembly'],
    'autohotkey': ['AutoHotkey', 'Autohotkey'],
    'awk': ['AWK', 'AWK'],
    'bash': ['bash', 'Bash'],
    'c': ['C', 'C'],
    'cobol': ['COBOL', 'COBOL'],
    'cpp': ['C.2B.2B', 'C++'],
    'csharp': ['C.23', 'C#'],
    'd': ['D', 'D'],
    'delphi': ['Delphi', 'Delphi'],
    'fsharp': ['F.23', 'F#'],
    'eiffel': ['Eiffel', 'Eiffel'],
    'euphoria': ['Euphoria', 'Euphoria'],
    'fortran': ['Fortran', 'Fortran'],
    'freebasic': ['FreeBASIC', 'FreeBASIC'],
    'go': ['Go', 'Go'],
    'haskell': ['Haskell', 'Haskell'],
    'objc': ['Objective-C', 'Objective-C'],
    'java': ['Java', 'Java'],
    'javascript': ['JavaScript', 'Javascript'],
    'lisp': ['Lisp', 'Lisp'],
    'lua': ['Lua', 'Lua'],
    'matlab': ['MATLAB', 'Matlab'],
    'ocaml': ['Ocaml', 'Ocaml'],
    'pascal': ['Pascal', 'Pascal'],
    'perl': ['Perl', 'Perl'],
    'php': ['PHP', 'PHP'],
    'powershell': ['PowerShell', 'PowerShell'],
    'purebasic': ['PureBasic', 'PureBasic'],
    'python': ['Python', 'Python'],
    'ruby': ['Ruby', 'Ruby'],
    'rust': ['Rust', 'Rust'],
    'scala': ['Scala', 'Scala'],
    'swift': ['Swift', 'Swift']

}
