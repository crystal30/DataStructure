#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    print(fibonacci(4))











