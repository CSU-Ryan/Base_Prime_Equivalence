import numpy as np
import sympy
import matplotlib.pyplot as plt

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]

base = 10


def to_string_base(n: int, b: int) -> str:
    out = ""
    while n > 0:
        digit = n % b
        out = str(digit) + out
        n //= b
    return out


def log_p(n: int, p: int):
    exponent = 0
    while n % p == 0:
        exponent += 1
        n //= p
    return exponent, n


def fast_exponentiation(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result


def n_to_prime(number: int):
    pos = 0
    total = 1

    while number > 0:
        digit = number % base

        total *= fast_exponentiation(primes[pos], digit)
        number //= base
        pos += 1

    return total


def prime_to_n(number: int):
    pos = 1
    pos_factor = 1
    total = 0

    while number > 1:
        digit, number = log_p(number, sympy.prime(pos))

        total += digit * pos_factor

        pos += 1
        pos_factor *= base

    return total


def base_to_prime_equivalence():
    sampling_period = 1

    start = 1
    end = 100000
    data_width = (end - start) // sampling_period + 1

    inputs = np.zeros(data_width, dtype=float)
    outputs = np.zeros(data_width, dtype=float)

    i = 0
    for number in range(start, end, sampling_period):
        converted_number = n_to_prime(number)

        inputs[i] = number
        try:
            outputs[i] = converted_number
        except OverflowError:
            outputs[i] = 0
        i += 1

        # if converted_number is not None and number == converted_number:
        #     print(to_string_base(number, base))

    plt.title(f"Sampling period: {sampling_period}")
    plt.xlabel(f"Base {base}")
    plt.ylabel("Base Prime")
    plt.yscale("log", base=base)

    # print(inputs)
    # print(outputs)

    plt.scatter(inputs, outputs, s=0.05)
    plt.plot(inputs, inputs)

    plt.show()

base_to_prime_equivalence()
