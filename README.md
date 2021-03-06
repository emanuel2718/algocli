<h1 align="center" style="font-size: 3rem;">
algo-CLI
</h1>

Print common algorithms to the command line


# Index

* [Installation](#installation)
* [Description](#description)
* [How to use](#how-to-use)
  - [Options](#options)
  - [Supported Languages](#supported-languages)
  - [Supported Algorithms](#supported-algorithms)
* [Examples](#examples)
* [Available Themes](#available-themes)
* [Things to do](#things-to-do)
* [Contributions](#contributions)
* [Credits](#credits)


# Installation

Use pip:

    pip install algocli
    
macOS users can install using [Homebrew](https://brew.sh):

    brew install algocli

Manual installation:

    git clone https://github.com/emanuel2718/algocli.git
    cd algocli
    python setup.py install


# Description

**algocli** is a command-line tool that lets users print common algorithms directly into the terminal. Why open
a browser search through countless articles about how to do [insertionsort in python](#insertionsort-python) when you can just type `algocli python insertionsort` in the terminal.

    algocli [INPUT ...] [OPTIONS]
    
    
![bubblesortPython](https://user-images.githubusercontent.com/55965894/110212969-cb68e780-7e52-11eb-8f34-1b02a11b4c56.png)

&nbsp; 

# How to use

&nbsp; 

## Options:

    -h, --help              show this help message and exit
    -v, --version           displays the current version of algcli
    --list-colors           print list of available colorschemes
    --list-lang             print list of supported languages
    --list-algo             print list of supported algorithms
    
    -c [COLORSCHEME], --color [COLORSCHEME]
                            colorized output
    

## Supported Language:

Correct language query (shown on the left) must be given for **algocli** to understand

    actionscript         Actionscript
    ada                  Ada
    algol68              ALGOL68
    applescript          Applescript
    autohotkey           Autohotkey
    awk                  AWK
    c                    C
    cpp                  C++
    csharp               C#
    d                    D
    delphi               Delphi
    fsharp               F#
    eiffel               Eiffel
    fortran              Fortran
    go                   Go
    haskell              Haskell
    objc                 Objective-C
    java                 Java
    javascript           Javascript
    lua                  Lua
    matlab               Matlab
    ocaml                Ocaml
    pascal               Pascal
    perl                 Perl
    php                  PHP
    powershell           PowerShell
    python               Python
    ruby                 Ruby
    rust                 Rust
    scala                Scala
    swift                Swift
    
## Supported Algorithms:

Correct language query (shown on the left) must be given for **algocli** to understand

    avltrees             AVL Trees
    b64                  Decode Base64 data
    beadsort             Bead Sort algorithm
    binarysearch         Binary Search algorithm
    bogosort             Bogo Sort algorithm
    bubblesort           Bubble Sort algorithm
    caesarcipher         Caesar Cipher
    cocktailsort         Cocktail Sort algorithm
    combsort             Comb Sort algorithm
    countingsort         Counting Sort algorithm
    cyclesort            Cycle Sort algorithm
    damm                 Damm algorithm
    dijkstra             Dijkstra algorithm
    e                    Calculate the value of e
    eulermethod          Euler method
    evolutionary         Evolutionary algorithm
    factorial            Calculate factorials
    factorions           Calculate factorions
    fft                  Fast Fourier Transforms
    fib                  Fibonacci Sequence
    fibnstep             Fibonacci N-step Number Sequence
    fileexists           Check if a given file exists or not
    fizzbuzz             FizzBuzz
    floydwarshall        Floy Warshall algorithm
    gnomesort            Gnome Sort algorithm
    hammingnumbers       Hamming numbers
    heapsort             Heap Sort algorithm
    huffman              Huffman coding
    insertionsort        Insertion Sort algorithm
    isaac                ISAAC Cipher
    knapsack             Knapsack Problem 0-1
    knapsackbound        Knapsack Problem Bounded
    knapsackcont         Knapsack Problem Continous
    knapsackunbound      Knapsack Problem Unbounded
    kolakoski            Kolakoski Sequence
    mandelbrot           Mandelbrot Set
    mazegen              Maze Generation
    mazesolve            Maze Solving
    md4                  How to use MD4
    md5                  How to use MD5
    md5imp               MD5 Algorithm implementation
    mergesort            Merge Sort algorithm
    nqueen               N-Queens Problem
    pancakesort          Pancake Sort algorithm
    patiencesort         Patience Sort algorithm
    permutationsort      Permutation Sort algorithm
    quickselect          Quickselect Algorithm
    quicksort            Quick Sort algorithm
    radixsort            Radix Sort algorithm
    recaman              Recaman Sequence
    regex                Simple Regular Expressions
    rot13                Rot-13 Algorithm
    rsa                  RSA code
    selectionsort        Selection Sort algorithm
    sexyprime            Sexy primes
    sha1                 SHA-1 Algorithm
    sha256               SHA-256 Algorithm
    shellsort            Shell Sort algorithm
    sieve                Sieve of Eratosthenes Algorithm
    sleepsort            Sleep Sort algorithm
    stoogesort           Stooge Sort algorithm
    strandsort           Strand Sort algorithm
    subcipher            Substitution Cipher
    toposort             Topological Sort Algorithm

&nbsp; 

# Examples

**NOTE**: The order of the options do not matter, but for the sake of simplicity all the examples will be shown with the algorithm first followed by the language. The following are equivalent:
    
    algocli radixsort cpp
    algocli cpp radixsort
    
&nbsp; 

#### List of supported languages
    
    algocli --list-lang

#### List of supported algorithms

    algocli --list-algo

#### Insertion Sort with Python *without* color

    algocli insertionsort python

#### Insertion Sort with Python *with* color

    algocli insertionsort python -c

#### Insertion Sort with Python *with* material colorscheme

    algocli insertionsort python -c material
    
#### Radix Sort with C++

    algocli radixsort cpp
    
#### Fibonacci Sequence calculation with Java

    algocli fib java

&nbsp; 

# Available Themes

&nbsp; 

### default

![defaultColor](https://user-images.githubusercontent.com/55965894/110213518-48955c00-7e55-11eb-83a1-a2620b1479d0.png)

### fruity

![fruityColor](https://user-images.githubusercontent.com/55965894/110213548-68c51b00-7e55-11eb-9124-560d29d2d09b.png)

### igor

![igorColor](https://user-images.githubusercontent.com/55965894/110213563-75e20a00-7e55-11eb-9277-aa0aee20444a.png)

### lovelace

![lovelaceColor](https://user-images.githubusercontent.com/55965894/110213574-7e3a4500-7e55-11eb-8308-410d9de99ac9.png)

### material

![materialColor](https://user-images.githubusercontent.com/55965894/110213587-85615300-7e55-11eb-851f-68e2d74cb23c.png)

### monokai

![monokaiColor](https://user-images.githubusercontent.com/55965894/110213595-8d20f780-7e55-11eb-9aa5-72a69d2c4bf2.png)

### pastie

![pastieColor](https://user-images.githubusercontent.com/55965894/110213604-96aa5f80-7e55-11eb-8e5a-34c74f586840.png)

### rrt

![rrtoColor](https://user-images.githubusercontent.com/55965894/110213610-9b6f1380-7e55-11eb-971f-7e844120ccdf.png)

### solarized-dark

![solarized-darkColor](https://user-images.githubusercontent.com/55965894/110213618-a033c780-7e55-11eb-986b-83e1d2f0a792.png)

### stata-dark

![stataDarkColor](https://user-images.githubusercontent.com/55965894/110213627-aa55c600-7e55-11eb-8c54-5391afa7a3f0.png)

### trac

![tracColor](https://user-images.githubusercontent.com/55965894/110213634-b04ba700-7e55-11eb-8ea3-a4134c3b4517.png)

### zenburn

![zenburnColor](https://user-images.githubusercontent.com/55965894/110213645-b6da1e80-7e55-11eb-8236-f5f10ec444b9.png)

&nbsp; 
    
# Contributions

*insert contributions message here*



# Things to do:

- [ ] Fix bug with color flag (i.e algocli -c radixsort cpp)
- [ ] Let the user change the default language and colorscheme (This works with insalled packages? How?)
- [ ] Add the option of giving (c++, C++, cplusplus, c+++ or cpp as language input)
- [ ] Reduce the amount it takes to output the data (Acceptable range 1-1.9 seconds. Now in 3-4 seconds)
- [ ] Add (-a, --all) flag that prints all the output including explanations (without that it should only print code)
- [ ] Think about removing the explanations and outputs (Maybe a flag --ignore-descriptions, --ignore-output, --ignore-all)
- [ ] Make test suit
- [ ] Publish version 0.1 to pip and Homebrew. (Maybe macports?)
- [ ] Handle non-256 terminal
- [ ] Make Colorscheme section with photos in README.
- [ ] Handle different OS (Windows, Linux, MacOS)
- [ ] Make `-l` argument that shows a list of the algorithms sorted by complexities
- [ ] Handle excesive long lines (i.e -b64 -java, -b64 -cpp)
- [ ] Hanlde user input errors
- [ ] Add autcompletion for algorithms? Could be neat!

&nbsp; 

# Credits

This project couldn't have been possible without [Rosetta Code](https://www.rosettacode.org/wiki/Rosetta_Code), which is a wonderful resource for any programmer looking to learn about how to do different things in almost any programming language in existence.

All credits go to Rosetta Code and all the contributors of the site.



