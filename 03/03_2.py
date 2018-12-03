#!/usr/bin/env python3

import collections

def isOverlap(squares, cnt):
    for i in squares:
        if cnt[i] >= 2:
            return True
    return False


def second(data, cnt):
    for line in data:
        squares = []
        segments = line.split(' ')
        thisid =  segments[0][1:]
        a,b =  map(int, segments[2][:-1].split(','))
        x,y = map(int, segments[3].split('x'))
        for i in range(b,b+y):
            for j in range(a,a+x):
                squares.append( (j,i) )
        if not isOverlap(squares,cnt):
            print(thisid, 'is not overlap')

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
    second(data, cnt)

if __name__ == '__main__':
    main()