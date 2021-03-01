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

def print_algorithm_info(algorithm=None, complexity=None):
    if algorithm is not None:
        return (f'Algorithm: {algorithm}\n'
                f'Complexity: {complexity}\n')



information = {"binarysearch": print_algorithm_info('Binary Search', LOGARITHMIC),
               "bogosort": print_algorithm_info('Bogo Sort', NFACTORIAL),
               "bubblesort": print_algorithm_info('Bubble Sort', CUADRATIC),
               "cocktailsort": print_algorithm_info('Cocktail Sort', CUADRATIC),
               "cyclesort": print_algorithm_info('Cycle Sort', CUADRATIC),
               "gnomesort": print_algorithm_info('Gnome Sort', CUADRATIC),
               "heapsort": print_algorithm_info('Heap Sort', NLOGN),
               "insertionsort": print_algorithm_info('Insertion Sort', LINEAR),
               "mergesort": print_algorithm_info('Merge Sort', NLOGN),
               "quicksort":     print_algorithm_info('Quick Sort', NLOGN),
               "radixsort":     print_algorithm_info('Radix Sort', NK),
               "selectionsort": print_algorithm_info('Selection Sort', CUADRATIC),
               "shellsort": print_algorithm_info('Shell Sort', NLOGNSQUARED),
               "stoogesort": print_algorithm_info('Stooge Sort', CUADRATIC)
               }


''' The keys in this dictionary will represent the command line arguments that the user
    inputs to select the desired algorithm:
        i.e algocli -insertionsort

    The values need to match the formatting of rosettacode sorting page address tail because it varies
    from sorter to sorter. It's also case sensitive. For example:
        Insertion sort: https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort <---
        Heap sort: https://rosettacode.org/wiki/Sorting_algorithms/Heapsort <----
'''
SORTING_ALGORITHMS = {
    'beadsort': ['Bead_sort', 'Bead Sort algorithm'],
    'bogosort': ['Bogo_sort', 'Bogo Sort algorithm'],
    'bubblesort': ['Bubble_sort', 'Bubble Sort algorithm'],
    'cocktailsort': ['Cocktail_sort', 'Cocktail Sort algorithm'],
    'combsort': ['Comb_sort', 'Comb Sort algorithm'],
    'countingsort': ['Counting_sort', 'Counting Sort algorithm'],
    'cyclesort': ['Cycle_sort', 'Cycle Sort algorithm'],
    'gnomesort': ['Gnome_sort', 'Gnome Sort algorithm'],
    'heapsort': ['Heapsort', 'Heap Sort algorithm'],
    'insertionsort': ['Insertion_sort', 'Insertion Sort algorithm'],
    'mergesort': ['Merge_sort', 'Merge Sort algorithm'],
    'pancakesort': ['Pancake_sort', 'Pancake Sort algorithm'],
    'patiencesort': ['Patience_sort', 'Patience Sort algorithm'],
    'permutationsort': ['Permutation_sort', 'Permutation Sort algorithm'],
    'quicksort': ['Quicksort', 'Quick Sort algorithm'],
    'radixsort': ['Radix_sort', 'Radix Sort algorithm'],
    'selectionsort': ['Selection_sort', 'Selection Sort algorithm'],
    'shellsort': ['Shell_sort', 'Shell Sort algorithm'],
    'sleepsort': ['Sleep_sort', 'Sleep Sort algorithm'],
    'stoogesort': ['Stooge_sort', 'Stooge Sort algorithm'],
    'strandsort': ['Strand_sort', 'Strand Sort algorithm']
}


''' If the user input a language flag in the cli arguments the it will be valid if it exists
    as in the keys of this dictionary and if the value language is found for the requested sorter.

    Supported languages. Some lanagues (like Java) in different sorter pages will appear as java or java5
'''
# TODO: Fix the first entry of the values it must match the page source name!!!
SUPPORTED_LANGUAGES = {
    'actionscript': ['ActionScript', 'Show algorithm in Actionscript'],
    'ada' : ['Ada', 'Show algorithm in Ada'],
    'algol68': ['ALGOL_68', 'Show algorithm in ALGOL68'],
    'applescript': ['AppleScript', 'Show algorithm in Applescript'],
    'arm': ['ARM_Assembly', 'Show algorithm in ARM Assembly'],
    'autohotkey': ['AutoHotkey', 'Show algorithm in Autohotkey'],
    'awk': ['AWK', 'Show algorithm in AWK'],
    'bash': ['bash', 'Show algorithm in Bash'],
    'c': ['C', 'Show algorithm in C'],
    'cobol': ['COBOL', 'Show algorithm in COBOL'],
    'cpp': ['C.2B.2B', 'Show algorithm in C++'],
    'csharp': ['C.23', 'Show algorithm in C#'],
    'd': ['D', 'Show algorithm in D'],
    'delphi': ['Delphi', 'Show algorithm in Delphi'],
    'fsharp': ['F.23', 'Show algorithm in F#'],
    'eiffel': ['Eiffel', 'Show algorithm in Eiffel'],
    'euphoria': ['Euphoria', 'Show algorithm in Euphoria'],
    'fortran': ['Fortran', 'Show algorithm in Fortran'],
    'freebasic': ['FreeBASIC', 'Show algorithm in FreeBASIC'],
    'go': ['Go', 'Show algorithm in Go'],
    'haskell': ['Haskell', 'Show algorithm in Haskell'],
    'objc': ['Objective-C', 'Show algorithm in Objective-C'],
    'java': ['Java', 'Show algorithm in Java'],
    'javascript': ['JavaScript', 'Show algorithm in Javascript'],
    'lisp': ['Lisp', 'Show algorithm in Lisp'],
    'lua': ['Lua', 'Show algorithm in Lua'],
    'matlab': ['MATLAB', 'Show algorithm in Matlab'],
    'ocaml': ['Ocaml', 'Show algorithm in Ocaml'],
    'pascal': ['Pascal', 'Show algorithm in Pascal'],
    'perl': ['Perl', 'Show algorithm in Perl'],
    'php': ['PHP', 'Show algorithm in PHP'],
    'powershell': ['PowerShell', 'Show algorithm in PowerShell'],
    'purebasic': ['PureBasic', 'Show algorithm in PureBasic'],
    'python': ['Python', 'Show algorithm in Python'],
    'ruby': ['Ruby', 'Show algorithm in Ruby'],
    'rust': ['Rust', 'Show algorithm in Rust'],
    'scala': ['Scala', 'Show algorithm in Scala'],
    'swift': ['Swift', 'Show algorithm in Swift']

}
