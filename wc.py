#!/usr/bin/env python3
import argparse
import sys


def get_text(file):
    with open(file, 'r') as text_file:
        lines = text_file.readlines()
    return lines


def count_frequence(lines):
    freq = dict()
    for line in lines:
        words = line.split()
        for word in words:
            if word in freq:
                freq[word] = freq[word] + 1
            else:
                freq[word] = 1
    return freq


def run(args):
    parser = argparse.ArgumentParser(description='Counts words in a text file and prints their')
    parser.add_argument('-f', '--file', type=str, required=True,
                        help="The text file to read.")

    args = parser.parse_args()
    lines = get_text(args.file)
    freq = count_frequence(lines)
    for word in sorted(freq, key=freq.get, reverse=True):
        if freq[word] > 10:
            print('{}: {}'.format(word, freq[word]))


if __name__ == '__main__':
    run(sys.argv)