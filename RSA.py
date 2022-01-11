# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 07:53:25 2022

@author: chere
"""
from sys import argv
import Prime

def readTextFromFile(input, encoding='utf-8'):
    f = open(input, "r", encoding=encoding)
    text = f.read()
    f.close()
    return text

def writeTextToFile(text, output, encoding='utf-8'):
    f = open(output, "w", encoding=encoding)
    f.write(text)
    f.close()

def quick_pow_mod(a, b, c):
    a = a % c
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a % c) * (a % c)
    return ans

def encrypt(message, public_key):
    digits = []
    for sym in message: digits.append(ord(sym))
    
    res = []
    for digit in digits:
        res.append(quick_pow_mod(digit, public_key[1], public_key[0]))
    
    out = []
    for k in res:
        out.append(''.join(chr(k)))
        
    return str(''.join(out))

def decrypt(secret, private_key):
    digits = []
    for sym in secret: digits.append(ord(sym))
    
    res = []
    for digit in digits:
        res.append(quick_pow_mod(digit, private_key[1], private_key[0]))
    
    out = []
    for k in res:
        out.append(''.join(chr(k)))
        
    return str(''.join(out))

if __name__ == '__main__':

    if len(argv) <= 4:
        print("Неверное число аргументов")
        quit(-1)

    try:
        inputFile = argv[argv.index("-i") + 1]
        outputFile = argv[argv.index("-o") + 1]
        # Генерируем ключи
        RSA_keys = Prime.generate_keys()
        print(RSA_keys)
        
        secret = encrypt(readTextFromFile(inputFile), RSA_keys['public_key'])
        writeTextToFile(secret, outputFile)
        
        message = decrypt(readTextFromFile(outputFile), RSA_keys['private_key'])
        writeTextToFile(message, "decrypted_" + inputFile)

    except ValueError:
        print("Некорректные аргументы")
        quit(-1)