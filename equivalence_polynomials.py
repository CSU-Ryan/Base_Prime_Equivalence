import numpy as np
import numpy.polynomial as npoly
import sympy
import matplotlib.pyplot as plt


def fast_exp(base: float, exponent: float) -> float:
    """
    A fast algorithm for exponentiation
    """
    result = 1
    while exponent > 0:

        if exponent % 2 == 1:
            result *= base
            exponent -= 1

        base *= base
        exponent /= 2

    return result


def base_prime(digits) -> int:
    total = 1
    primes = [sympy.prime(n+1) for n in range(len(digits))]

    for digit, prime in zip(digits, primes):
        total *= fast_exp(prime, digit)

    return total


def increment_digits(digits, base: int, pos=0):
    while digits[pos] + 1 >= base:
        digits[pos] = 0
        pos += 1

    digits[pos] += 1

    return digits


def get_root(roots):
    epsilon = 0.05
    for x in roots:
        if np.imag(x) < epsilon and (np.real(x) % 1) < epsilon:
            return np.real(x)


def find_equivalence_polynomials(digits, val_prime):
    digits[0] -= val_prime
    polynomial = npoly.Polynomial(digits)
    # polynomial.domain = np.array([2, 10])

    roots = polynomial.roots()
    return get_root(roots)


if __name__ == '__main__':
    base = 1000
    digits = np.array([0, 1, 0], dtype=float)
    end = 1000

    bases = np.zeros((end-1), dtype=float)

    for i in range(end-1):
        val_prime = base_prime(digits)

        root = find_equivalence_polynomials(np.copy(digits), val_prime)

        if root is not None:
            # print(f"repr:{digits} b:{root} -> val:{val_prime}")
            bases[i] = root

        digits = increment_digits(digits, base)

    print(bases)
    plt.scatter(list(range(len(bases))), bases)
    plt.yscale("log")
    plt.show()
