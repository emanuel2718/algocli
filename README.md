<h1 align="center" style="font-size: 3rem;">
algo-CLI
</h1>

## TODO:

- [x] Handle command line arguments
- [x] `algocli -quicksort -python` or `algocli -b64 -cpp` cli argument for language of choice
- [x] Handle case of losing first line of output (-haskell -radixsort) (-go -radixsort)
- [x] Replace the =={header}== line in output
- [x] Include all algorithms (Need to refactor url with wiki/Sorting_algorithms/<sort>). This needs to be inlcluded only when it's a sorting algorithm (i.e wiki/Binary_search)
- [x] Add color to the syntax in output code
- [x] Think about removing {{trans|Kotlin}} cases (i.e -java -base64)
- [x] Think about adding {{Out}} to the stopping flags (i.e -python -binarysearch)
- [x] Make the user be able to chose colorscheme (i.e --colorscheme gruvbox)
- [x] Think about adding '''Library''' to the STOP_FLAGS (i.e -binarysearch -cpp)
- [x] Handle case where the algorithm is not found (-rust -radixsort)
- [ ] Add the option of giving (c++, C++, cplusplus, c+++ or cpp as language input)
- [ ] Reduce the amount it takes to output the data (Acceptable range 1-1.9 seconds. Now in 3-4 seconds)
- [ ] Add (-a, --all) flag that prints all the output including explanations (without that it should only print code)
- [ ] Think about removing the explanations and outputs (Maybe a flag --ignore-descriptions, --ignore-output, --ignore-all)
- [ ] Make test suit
- [ ] Handle non-256 terminal
- [ ] Make Colorscheme section with photos in README.
- [ ] Handle different OS (Windows, Linux, MacOS)
- [ ] Make `-l` argument that shows a list of the algorithms sorted by complexities
- [ ] Handle excesive long lines (i.e -b64 -java, -b64 -cpp)
- [ ] Hanlde user input errors
- [ ] Add autcompletion for algorithms? Could be neat!

