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
        exponent //= 2

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


def solve_linear(coefficients):
    a = coefficients[0]
    b = coefficients[1]

    if b == 0:
        return None

    x = (-a) / b

    # Check for integer solution
    if x % 1 != 0:
        return None

    return x


def solve_quadratic(coefficients):
    c = coefficients[0]
    b = coefficients[1]
    a = coefficients[2]

    # Check if the system is actually quadratic
    if a == 0:
        return solve_linear(coefficients[:2])

    in_sqrt = b*b - (4 * a * c)

    if in_sqrt < 0:
        return None
    else:
        x = (-b + np.sqrt(in_sqrt)) / (2 * a)

    # Check for integer solution
    if x % 1 != 0 or x < 0:
        return None

    return x


def find_equivalence_polynomials(digits: list, val_prime):
    digits[0] -= val_prime

    if len(digits) == 2:
        return solve_linear(digits)

    if len(digits) == 3:
        return solve_quadratic(digits)

    # Last resort, using numpy solver.
    polynomial = npoly.Polynomial(digits)

    roots = polynomial.roots()
    return get_root(roots)


if __name__ == '__main__':
    base = 10
    digits = np.array([0, 1, 0], dtype=float)
    end = 100

    bases = np.zeros((end-1), dtype=float, )

    for i in range(end-1):
        val_prime = base_prime(digits)

        root = find_equivalence_polynomials(np.copy(digits), val_prime)

        if root is not None:
            print(f"repr:{digits} b:{root} -> val:{val_prime}")
            bases[i] = root

        digits = increment_digits(digits, base)

    # print(bases)
    # plt.scatter(list(range(len(bases))), bases)
    # plt.yscale("log")
    # plt.show()
