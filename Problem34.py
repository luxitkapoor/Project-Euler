# Digit Factorials
# Find the sum of all numbers which are equal to the sum of the factorial of their digits
import math
from datetime import datetime
numbers = []
temp = []


def findNumbers():
    '''
    Brute Force method where each factorial is calculated every time

    '''
    start = datetime.now()
    for i in range(3, 2540160):
        temp = [math.factorial(int(x)) for x in str(i)]
        if i == sum(temp):
            numbers.append(i)
    print(sum(numbers))
    print("Time ", datetime.now() - start)


def improvedFindNumbers():

    start = datetime.now()
    listOfCommonFactorials = [math.factorial(x) for x in range(1, 10)]
    listOfCommonFactorials.insert(0, 1)
    # print(listOfCommonFactorials)
    for i in range(10, 2540160):
        temp = [listOfCommonFactorials[int(y)] for y in str(i)]
        if i == sum(temp):
            numbers.append(i)
    print(sum(numbers))
    print("Time Improved ", datetime.now() - start)


# findNumbers()

improvedFindNumbers()
