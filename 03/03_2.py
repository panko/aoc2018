#!/usr/bin/env python3

import collections

def main():
    squares = []
    res = 0
    with open('in.txt', 'r') as f:
        data = f.read().split('\n')
    for line in data:
        segments = line.split(' ')
        a,b =  map(int, segments[2][:-1].split(','))
        x,y = map(int, segments[3].split('x'))
        for i in range(b,b+y):
            for j in range(a,a+x):
                squares.append( (j,i) )
    cnt = collections.Counter(squares)
    for k, v in cnt.items():
        if v >= 2:
            res += 1
    print(res)

if __name__ == '__main__':
    main()