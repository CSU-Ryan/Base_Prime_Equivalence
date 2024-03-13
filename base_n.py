import numpy as np
import matplotlib.pyplot as plt

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

base = 10

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


sampling_period = 1

start = 0
end = 100
data_width = (end - start) // sampling_period

inputs = np.zeros(data_width, dtype=int)
outputs = np.zeros(data_width, dtype=int)

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
        # print(number)

plt.title(f"Sampling period: {sampling_period}")
plt.xlabel(f"Base {base}")
plt.ylabel("Base Prime")
plt.yscale("log", base=base)

# print(inputs)
# print(outputs)

plt.plot(inputs, outputs, 'ro')
plt.plot(inputs, inputs)

plt.show()
