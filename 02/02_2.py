#!/usr/bin/env python3

import collections

def hamming2(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def main():
    twos = 0
    threes = 0
    with open('in.txt', 'r') as f:
        data = f.read().split()
    for line in data:
        for line2 in data:
            if hamming2(line, line2) == 1:
                print(line, line2)
                break

if __name__ == '__main__':
    main()