#!/usr/bin/env python3

def main():
    res = 0
    with open('in.txt', 'r') as f:
        for line in f:
            if line[0] == '+':
                res = res + int(line[1:])
            if line[0] == '-':
                res = res - int(line[1:])
        print(res)

if __name__ == '__main__':
    main()