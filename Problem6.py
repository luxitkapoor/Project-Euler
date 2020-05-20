# Sum square difference
def sum_of_n_numbers(n):
    total = (n * (n + 1)) / 2
    total = total ** 2
    return total


def sum_of_squares_of_n_numbers(n):
    total = 1
    for i in range(2, n + 1):
        total += (i**2)

    return total


sum_square_difference = sum_of_n_numbers(100) - sum_of_squares_of_n_numbers(100)
print(sum_square_difference)
