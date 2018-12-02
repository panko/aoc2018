#!/usr/bin/env python3

import itertools

def main():
    res = 0
    dick = {}
    with open('in.txt', 'r') as f:
        data = f.read().split()
    for i in itertools.cycle(data):
        if i[0] == '+':
            res = res + int(i[1:])
        if i[0] == '-':
            res = res - int(i[1:])
        dick[res] = dick.get(res, 0) + 1
        if dick[res] == 2:
            print(res)
            break
        

if __name__ == '__main__':
    main()