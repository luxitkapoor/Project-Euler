# Factorial digit sum
import math


def getFactorialDigitSum(number):
    factorial = math.factorial(number)
    string = str(factorial)
    number = [int(digit) for digit in string]
    return sum(number)


print(getFactorialDigitSum(100))
