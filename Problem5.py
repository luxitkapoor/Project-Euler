import math

# Program to find the smallest multiple
start = 2520
flag = 0

while True:
    if start % 2 != 0 or start % 3 != 0 or start % 5 != 0:
        start = start + 1
        continue
    for number in range(1, 21):

        if number == 20:
            if start % number == 0:
                flag = 1
                break
        if start % number == 0:
            continue
        else:
            break

    if flag == 1:
        break

    start = start + 1

print(start)
