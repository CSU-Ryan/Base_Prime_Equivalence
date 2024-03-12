import numpy as np

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]


def fast_exponentiation(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result


def decimal_to_prime(number: int):
    pos = 0
    total = 1
    while number > 0:
        digit = number % 10

        if pos == 0 and digit not in (2, 4, 6, 8):
            return None
        if pos == 2 and digit != 0:
            return None

        total *= fast_exponentiation(primes[pos], digit)
        number //= 10
        pos += 1

    return total


start = 1000000000
for number in range(start, start*10):

    converted_number = decimal_to_prime(number)

    # print(number, converted_number)
    if converted_number is not None and number == converted_number:
        print(number)
