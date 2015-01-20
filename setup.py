#!/usr/bin/env/python
from setuptools import setup

setup(
    name = 'markov',
    version = '1.0',
    description = 'A Markov chain generator for building words',
    author = 'useanalias',
    packages = ['markov'],
    package_data = {'markov': ['data/*']},
    entry_points = {
        'console_scripts': [
            'markov = markov.markov:run'
        ]
    }
    
)
      


