import numpy as np
# import sympy
import matplotlib.pyplot as plt

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]


def to_string_base(n: int, base: int) -> str:
    """
    Returns the base-representation of n.
    :param n: the value to be presented.
    :param base: the base to convert to.
    :return: a string representation of n in the given base.
    """
    out = ""
    while n > 0:
        digit = n % base
        out = str(digit) + out
        n //= base
    return out


def base_factor(n: int, base: int):
    """
    Returns the largest power of p which divides n.
    :param n: the n to be factored
    :param base: the base
    :return: the largest power and the remainder.
    """
    exponent = 0
    while n % base == 0:
        exponent += 1
        n //= base
    return exponent, n


def fast_exponentiation(base: int, exponent: int) -> int:
    """
    A fast algorithm for exponentiation
    """
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result


def n_to_prime(n: int, base: int):
    """
    Reads a value in the given base, then evaluates it as though it was in base-prime.
    Where the base-b digits of the number are `a, b, ...`, converting to `2^a * 3^b *...`
    :param n: the value to be converted.
    :param base: the base to read `n` in.
    :return: the new value, interpreted in base-prime.
    """
    pos = 0
    total = 1

    while n > 0:
        digit = n % base

        total *= fast_exponentiation(primes[pos], digit)
        n //= base
        pos += 1

    return total


# def prime_to_n(number: int, base):
#     """
#     Reads a value in base-prime, then evaluates it as though it was in the given base.
#     Effectively the inverse of `n_to_prime()`.
#     :param number: the value to be converted.
#     :param base: the base to convert to.
#     :return: the new value, interpreted in the given base.
#     """
#     pos = 1
#     pos_factor = 1
#     total = 0
#
#     while number > 1:
#         digit, number = base_factor(number, sympy.prime(pos))
#
#         total += digit * pos_factor
#
#         pos += 1
#         pos_factor *= base
#
#     return total


def equivalence_search(base: int, start: int, end: int):
    """
    Finds all equivalent numbers in the given range and base.
    See the README for an understanding of equivalence.
    :param base: the base to search in.
    :param start: the start of the range
    :param end: the end of the range
    :return: Prints all found equivalences
    """
    for number in range(start, end):
        converted_number = n_to_prime(number, base)

        if converted_number == number:
            print(to_string_base(number, base))


def plot_equivalence(base: int, start: int, end: int, sampling_period: int):
    """
    Plots the range of values in the given base versus base-prime. Also includes `y=x` plot.
    :param base: the base for the input values
    :param start: the start of the range
    :param end: the end of the range
    :param sampling_period: how often to calculate these values.
    :return: shows the plot of data.
    """
    data_width = (end - start) // sampling_period + 1

    inputs = np.zeros(data_width, dtype=float)
    outputs = np.zeros(data_width, dtype=float)

    i = 0
    for number in range(start, end, sampling_period):
        converted_number = n_to_prime(number, base)

        inputs[i] = number
        outputs[i] = converted_number
        i += 1

    # Plotting Data
    plt.title(f"Sampling period: {sampling_period}")
    plt.xlabel(f"Base {base}")
    plt.ylabel("Base Prime")
    plt.yscale("log", base=base)

    plt.scatter(inputs, outputs)
    plt.plot(inputs, inputs)

    plt.show()


if __name__ == "__main__":
    base = 10
    start = 1
    end = 1000

    # equivalence_search(base, start, end)

    sampling_period = 10
    plot_equivalence(base, start, end, sampling_period)
