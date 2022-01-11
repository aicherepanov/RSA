# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 06:09:23 2022

@author: chere
"""

import random

"""
Возвращает True, если число num - простое, иначе False
"""
def is_prime(num: int) -> bool:
    return all(num % i != 0 for i in range(2, num))

"""
Создает список простых чисел от start до кол-ва amount
"""
def get_prime_range(start = 17, amount = 100) -> list:
    primes = list()
    
    # Обработка входных значений
    start = 2 if start < 2 else start
    amount = 1 if amount < 1 else amount
    if start == 2:
        primes.append(2)
        start += 1

    while len(primes) < amount:
        if is_prime(start):
            primes.append(start)
        start += 1

    return primes

"""
Возвращает 2 случайных простых числа
"""
def get_2_primes():
    primes = get_prime_range(start=17, amount=100)
    
    p = random.choice(primes)
    q = random.choice(primes)
    return p, q

"""
Возвращает Наибольший общий делитель 2 чисел
"""
def greatest_common_divisor(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

"""
Возвращает число e, которое не имеет общих делителей с fi
"""
def get_e(fi: int) -> int:
    e = 3
    while True:
        if greatest_common_divisor(fi, e) == 1:
            return e
        e += 2

"""
Расширенный алгоритм Евклида
"""
def greatest_common_divisor_extended(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = greatest_common_divisor_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x

"""
Возвращает число d
"""
def get_d(fi: int, e: int) -> int:
    div, v, u = greatest_common_divisor_extended(fi, e)
    return u % fi

"""
Генерирует открытый и закрытый ключи
"""
def generate_keys():
    p,q = get_2_primes()    
    n = p * q
    # Функция Эйлера
    fi = (p - 1) * (q - 1)
    # Открытая экспонента
    e = get_e(fi)
    d = get_d(fi, e)
    print('P = ', p, '; Q = ', q, '; N = ', n, '; E = ', e, '; D = ', d)
    
    public_key = [n, e]
    private_key = [n, d]
    RSA_keys = {}
    RSA_keys['public_key'] = public_key
    RSA_keys['private_key'] = private_key
    return RSA_keys

"""
Генерирует открытый и закрытый ключи
"""
def generate_keys(p, q):    
    n = p * q
    # Функция Эйлера
    fi = (p - 1) * (q - 1)
    # Открытая экспонента
    e = get_e(fi)
    d = get_d(fi, e)
    
    return e, d

if __name__ == '__main__':
    generate_keys()
    