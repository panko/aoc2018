#!/usr/bin/env python3

import collections


def main():
    twos = 0
    threes = 0
    with open('in.txt', 'r') as f:
        data = f.read().split()
    for line in data:
        cnt = set(collections.Counter(line).values())
        if 2 in cnt:
            twos += 1
        if 3 in cnt:
            threes += 1
    print(twos,'x',threes,'=', twos*threes)
        

if __name__ == '__main__':
    main()