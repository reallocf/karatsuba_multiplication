#!/usr/bin/env python
from sys import argv

def split_at_middle(num, middle):
    if (len(str(num)) > middle):
        return int(str(num)[:middle]), int(str(num)[middle:])
    else:
        return 0, num

def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2
    maxLen = max(len(str(num1)), len(str(num2)))
    if maxLen % 2:
        middle = maxLen / 2 + 1
    else:
        middle = maxLen / 2
    print middle
    high1, low1 = split_at_middle(num1, middle)
    high2, low2 = split_at_middle(num2, middle)
    print str(high1) + " " + str(low1) + "   " + str(high2) + " " + str(low2)
    res0 = karatsuba(low1, low2)
    res1 = karatsuba(low1 + high1, low2 + high2)
    res2 = karatsuba(high1, high2)
    return (res2 * 10 ** (2 * middle)) + ((res1 - res2 - res0) * 10 ** middle) + res0

if __name__ == "__main__":
    if len(argv) != 3:
        print("usage: ./multiply.py number1 number2")
        exit()
    print(karatsuba(int(argv[1]), int(argv[2])))
