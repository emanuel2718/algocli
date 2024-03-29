[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
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
* [Contributions](#contributions)
* [Credits](#credits)


# Installation

Use pip:

    $ pip install algocli

Manual installation:

    $ git clone https://github.com/emanuel2718/algocli.git
    $ cd algocli
    $ python setup.py install


# Description

**algocli** is a command-line tool that lets users print common algorithms directly into the terminal. Why open
a browser search through countless articles about how to do [insertionsort in python](#insertionsort-python) when you can just type `algocli python insertionsort` in the terminal.

    $ algocli [INPUT ...] [OPTIONS]
    
    
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
    

## Supported Languages:

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
    
    $ algocli radixsort cpp
    $ algocli cpp radixsort
    
&nbsp; 

#### List of supported languages
    
    $ algocli --list-lang

#### List of supported algorithms

    $ algocli --list-algo

#### Insertion Sort with Python *without* color

    $ algocli insertionsort python

#### Insertion Sort with Python *with* color

    $ algocli insertionsort python -c

#### Insertion Sort with Python *with* material colorscheme

    $ algocli insertionsort python -c material
    
#### Radix Sort with C++

    $ algocli radixsort cpp
    
#### Fibonacci Sequence calculation with Java

    $ algocli fib java

&nbsp; 

# Available Themes

[List of available Themes](https://github.com/emanuel2718/algocli/blob/master/THEMES.md)

&nbsp; 

    
# Contributions

*insert contributions message here*

&nbsp; 

# Credits

This project couldn't have been possible without [Rosetta Code](https://www.rosettacode.org/wiki/Rosetta_Code), which is a wonderful resource for any programmer looking to learn about how to do different things in almost any programming language in existence.

All credits go to Rosetta Code and all the contributors of the site.



