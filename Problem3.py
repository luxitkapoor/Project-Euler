# Largest Prime Factor of 600851475143
import math

number = 600851475143


def isOdd(value):
    if value % 2 != 0:
        return True
    else:
        return False


def isPrime(x):
    root = math.sqrt(x)
    root = int(root)
    for i in range(3, root, 2):
        if x % i == 0:
            return False
        else:
            continue
    return True


def findLargestPrimeFactor(x):

    root = math.sqrt(x)
    root = int(root)
    factors = []
    for i in range(1, root):
        if x % i == 0:
            factors.append(i)

    factors.reverse()
    # print(factors)
    for factor in factors:
        if isOdd(factor):
            if isPrime(factor):
                print(factor)


findLargestPrimeFactor(number)
