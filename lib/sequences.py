#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    a, b = 0, 1
    for _ in range(length):
        sequence.append(a)
        a, b = b, a + b
    print(sequence)
    pass