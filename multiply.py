#!/usr/bin/env python
from sys import argv

def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2
    middle = max(len(str(num1)), len(str(num2))) / 2
    high1 = num1 / 10 ** middle
    low1 = num1 % 10 ** middle
    high2 = num2 / 10 ** middle
    low2 = num2 % 10 ** middle
    res0 = karatsuba(low1, low2)
    res1 = karatsuba(low1 + high1, low2 + high2)
    res2 = karatsuba(high1, high2)
    return (res2 * 10 ** (2 * middle)) + ((res1 - res2 - res0) * 10 ** middle) + res0

if __name__ == "__main__":
    if len(argv) != 3:
        print("usage: ./multiply.py number1 number2")
        exit()
    print(karatsuba(int(argv[1]), int(argv[2])))
