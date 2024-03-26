import numpy as np
import numpy.polynomial as npoly
import sympy


def fast_exp(base: int, exponent: int) -> int:
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


def string_to_digits(string: str) -> list:
    out = []
    for digit in string[::-1]:
        out.append(int(digit))
    return out


def base_to_digits(n, base) -> list:
    digits = []

    while n > 0:
        digits.append(n % base)
        n //= base

    return digits


def base_prime(digits: list) -> int:
    total = 1
    primes = [sympy.prime(n+1) for n in range(len(digits))]
    # prime = 2

    for digit, prime in zip(digits, primes):
        total *= fast_exp(prime, digit)
        # prime = sympy.nextprime(prime)

    return total


def increment_digits(digits: list, base: int, pos=0) -> list:
    while digits[pos] + 1 >= base:
        digits[pos] = 0
        pos += 1

    digits[pos] += 1

    return digits


def get_root(roots):
    epsilon = 0.1
    for x in roots:
        if np.imag(x) < epsilon and np.real(x) % 1 < epsilon:
            return x


def find_equivalence_polynomials(digits: list, val_prime):
    digits[0] -= val_prime
    polynomial = npoly.Polynomial(digits)
    # polynomial.domain = np.array([2, 10])

    roots = polynomial.roots()
    return get_root(roots)


if __name__ == '__main__':
    base = 10
    digits = [0, 0, 0]
    end = 100

    for _ in range(end-1):
        val_prime = base_prime(digits)

        root = find_equivalence_polynomials(digits[:], val_prime)

        if root is not None:
            print(f"repr:{str(digits[::-1]):12s} b:{int(root)} -> val:{val_prime}")

        digits = increment_digits(digits, base)
