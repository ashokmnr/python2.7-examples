#!/usr/bin/python2.7

import argparse

parser = argparse.ArgumentParser(
    description="Search for works including partial word")
parser.add_argument(
    "snippet", help="partial (or complete) string to search for in the words file")

args = parser.parse_args()

snippet = args.snippet.lower()

words = open("/usr/share/dict/words").readlines()

print([word.strip() for word in words if snippet in word.lower()])


"""
numbers = [1, 2, 3, 4]
print([x * x for x in numbers])



matches = []

for word in words:
    if snippet in word.lower():
        matches.append(word)

print(matches)
"""
