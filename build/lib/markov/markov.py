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
        '-l', metavar='length', help='length of outputted strings', type=int, default=None)
    parser.add_argument(
        '-c', metavar='count', help='number of outputted strings', type=int, default=1)
    parser.add_argument(
        '-i', metavar='input', help='input file to read words from', default=words_dir)
    parser.add_argument('--alpha', help='forces markov to just read alphebetical characters', action='store_true')
    parser.add_argument('--case', help='forces markov to be case sensitive', action='store_true')
    args = parser.parse_args()

    # Make a counter for each character, and add a count to it whenever another character follows it in args.i 
    counters = collections.defaultdict(collections.Counter)
    words = []

    # Read through args.i, ignore case if --case isn't set, and remove nonalphabetical characters if --alpha is set 
    with open(args.i, 'r') as word_file:
        words = word_file.read().splitlines() 
        if not args.case: 
            words = [word.lower() for word in words]
        if args.alpha: 
            words = [re.sub(r'[^a-zA-Z]', '', word) for word in words]

    # Get a count of following letters for each word and populate counters
    for word in words:
        for index in range(len(word) - 1):
            counters[word[index]][word[index + 1]] += 1
        # Add an "end of word" character (None) onto the last character's counter
        if args.l is None:
            counters[word[-1]][None] += 1

    # Make a list of strings starting with random characters previously found 
    names = [random.choice(counters.keys()) for _ in range(args.c)]

    # Iterate through each name and, using the predetermined probabilities of one letter following another, choose the next letters randomly
    for name in names:
        if args.l is None:
            while True: 
                choices = counters[name[-1]].elements()
                choice = random.choice(list(choices))
                if choice is None:
                    break
                name += choice
        else:
            while len(name) < args.l:
                choices = counters[name[-1]].elements()
                name += random.choice(list(choices))

        print name
