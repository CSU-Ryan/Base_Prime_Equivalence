import numpy as np

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]


def fast_exponentiation(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result


def binary_to_prime(number: int):
    pos = 0
    total = 1
    while number > 0:
        bit = number & 1

        if bit == 1:
            total *= primes[pos]
        number = number >> 1
        pos += 1

    return total


start = 100000000
for number in range(start, start*10):
# for number in range(1, 1000000):

    converted_number = binary_to_prime(number)

    # print(number, converted_number)
    if number is not None and number == converted_number:
        print(number)
