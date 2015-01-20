#!/usr/bin/env/python
import argparse
import collections
import os
import random
import re
import string

def run():
    # Get directory for the words file 
    current_dir = os.path.dirname(os.path.realpath(__file__))
    words_dir = os.path.join(current_dir, 'data', 'words')

    # Set up terminal interface using argparse
    parser = argparse.ArgumentParser(
        description='Generate a word using a Markov chain.')
    parser.add_argument(
        '-l', metavar='length', help='length of outputted strings', type=int, default=10)
    parser.add_argument(
        '-c', metavar='count', help='number of outputted strings', type=int, default=1)
    parser.add_argument(
        '-i', metavar='input', help='input file to read words from', default=words_dir)

    args = parser.parse_args()
    alphabet = string.ascii_lowercase

    # Make a counter for each lowercase letter, and add a count to it
    # whenever a letter follows it in /usr/share/dict/words
    counters = {letter: collections.Counter() for letter in alphabet}
    raw_words = [word for word in open(args.i, 'r').read().splitlines()]

    # Clean up the words by making them lowercase and removing any
    # non-alphabetical characters
    words = [re.sub(r'[^a-z]', r'', word.lower()) for word in raw_words]

    # Get a count of following letters for each word and populate counters
    for word in words:
        for index in range(len(word) - 1):
            counters[word[index]][word[index + 1]] += 1

    # Make a list of strings starting with random letters
    names = [random.choice(alphabet) for _ in range(args.c)]

    # Iterate through each name and, using the predetermined probabilities
    # of one letter following another, choose the next letters randomly
    for name in names:
        while len(name) < args.l:
            choices = counters[name[-1]].elements()
            name += random.choice(list(choices))
        print name
