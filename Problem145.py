# How many reversible numbers are there below one-billion?
# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

# There are 120 reversible numbers below one-thousand.

# How many reversible numbers are there below one-billion (109)?

'''
Range 10 Numbers 0
Range 100 Numbers 20
Range 1000 Numbers 120
Range 10000 Numbers 720
Range 100000 Numbers 720
Range 1000000 Numbers 18720
Range 10000000 Numbers 68720
Range 100000000 Numbers 608720
'''
from datetime import datetime

storage = {}
odd = {"1", "3", "5", "7", "9"}


def isReversible(toRun):
    # storage = {}

    for i in range(100000000, toRun):
        if i in storage or i % 10 == 0:
            continue
        else:
            reverse = reverseNumber(i)
            total = i + reverse
            if (i % 2 != 0 and reverse % 2 != 0) or (i % 2 == 0 and reverse % 2 == 0):
                continue
            if total % 2 == 0:
                continue

            for x in str(total):
                if x not in odd:
                    break
            else:
                storage[i] = 1
                storage[reverse] = 1

    # return len(storage.keys())


def reverseNumber(number):
    return int(str(number)[::-1])


start = datetime.now()

isReversible(10**9)
print(len(storage.keys()) + 608720)
print("Time ", datetime.now() - start)


def sumOfDigits(digit):
    string = str(digit)
    iterate = 0
    length = len(string)
    if length % 2 == 0:
        while iterate < length / 2:
            print(int(string[0 + iterate]) + int(string[-1 - iterate]))
            iterate += 1

    else:
        while iterate <= length / 2:
            print(int(string[0 + iterate]) + int(string[-1 - iterate]))
            iterate += 1


# sumOfDigits(99999)
# times = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
# for i in times:
#     print("Range", i, "Numbers", isReversible(i))
