<h1 align="center" style="font-size: 3rem;">
algo-CLI
</h1>

## TODO:

- [x] Handle command line arguments
- [x] `algocli -python -quicksort` or `algocli -cpp -quicksort` cli argument for language of choice
- [x] Handle case of losing first line of output (-haskell -radixsort) (-go -radixsort)
- [x] Replace the =={header}== line in output
- [ ] Include all algorithms (Need to refactor url with wiki/Sorting_algorithms/<sort>). This needs to be inlcluded only when it's a sorting algorithm (i.e wiki/Binary_search)
- [ ] Think about adding {{Out}} to the stopping flags (i.e -python -binarysearch)
- [ ] Think about removing {{trans|Kotlin}} cases (i.e -java -base64)
- [ ] Handle case where the algorithm is not found (-rust -radixsort)
- [ ] Show algorithm in pager
- [ ] Add color to the syntax in output code
- [ ] Make `-l` argument that shows a list of the algorithms sorted by complexities
- [ ] Hanlde user input errors
- [ ] Handle different OS (Windows, Linux, MacOS)
