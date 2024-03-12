from timeit import default_timer as timer

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]


def binary_to_prime(number: int):
    product = 1
    prime_iter = iter(primes)

    while number > 0:
        next_prime = next(prime_iter)
        if (number & 1) == 1:
            product *= next_prime
        number >>= 1

    return product


# for number in range(start, start*10):
out = []
start = timer()
first_val = 10000000
for number in range(first_val, first_val*10):

    prime = binary_to_prime(number)
    # print(f"{number:08b}: {prime}")
    if number == prime:
        out.append(number)

end = timer()
print(f"t: {end - start:0.2f} seconds")
for number in out:
    print(f"{number:b}")
