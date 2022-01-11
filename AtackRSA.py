# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:46:02 2022

@author: chere
"""

import random
import Prime

from itertools import combinations

def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def fermat(n):
    a = isqrt(n)
    b2 = a * a - n
    b = isqrt(n)
    count = 0
    while b * b != b2:
        a = a + 1
        b2 = a * a - n
        b = isqrt(b2)
        count += 1
    p = a + b
    q = a - b
    assert n == p * q
    return p, q

prime_range = Prime.get_prime_range(17, 100)
p, q = random.sample(prime_range, 2)
n = p * q
e, d = Prime.generate_keys(p, q)

print(p, q, e, d)

for i, pair in enumerate(combinations(prime_range, 2)):
    fp, fq = fermat(pair[0] * pair[1])
    fe, fd = Prime.generate_keys(fp, fq)
    if (fd == d):
        print("Iter number: ", i)
        break
