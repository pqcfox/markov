markov
======

A simple command-line program designed to generate words using Markov chains.
The idea for this project belongs to leb2, and the 'words' file is from /usr/share/dict/words on my Mac OSX install.

To run the program, simply type `markov`. For fun (on Mac OSX), type in `watch 'markov | say'` and be amused by a new word every 2 seconds.

Features:

* End of word state allows markov to automatically know when to end a word
* Comes with list of words, but can be supplied with new list via -i
* A character length can be imposed using -l
* Will output multiple words given a count with -c
* Case-sensitivity can be set with --case
* Restriction to alphabetical characters can be set with --alpha

Features (upcoming):

* For known files, will read/write frequency files making chain generation faster.
