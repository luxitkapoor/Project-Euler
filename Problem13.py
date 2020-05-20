# Large Sum
# Calculate the sum of 100 numbers each 50 digits long.

file = open("ListOfNumbers.txt")
numbers = []
trial = 0
for line in file:
    numbers.append(int(line))
    trial += int(line[:12])

total = sum(numbers)
total = str(total)
print(total[:10])
print("Trial ", trial)
