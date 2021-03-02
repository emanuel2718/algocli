<h1 align="center" style="font-size: 3rem;">
algo-CLI
</h1>

## TODO:

- [x] Handle command line arguments
- [x] `algocli -python -quicksort` or `algocli -cpp -quicksort` cli argument for language of choice
- [x] Handle case of losing first line of output (-haskell -radixsort) (-go -radixsort)
- [ ] Replace the =={header}== line in output
- [ ] Handle case where the algorithm is not found (-rust -radixsort)
- [ ] Show algorithm in pager
- [ ] Add color to the syntax in output code
- [ ] Make `-l` argument that shows a list of the algorithms sorted by complexities
- [ ] Fix quicksort algorithm bug with list splicing
- [ ] Add C++ and Java algorithms
- [ ] Make the complexities optional `-c`
- [ ] Think about how to only have to type the algorithm once. Extract it from code somehow?
- [ ] Show list of algorithms by complexities and divided by search and sorting
- [ ] Hanlde user input errors
- [ ] Handle different OS (Windows, Linux, MacOS)
- [ ] Expand to other languages (need to refactor the file structure (folder per language))
