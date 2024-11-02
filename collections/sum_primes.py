def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_primes(list_numbers):
    if not list_numbers:
        return None

    prime_sum = sum(num for num in list_numbers if is_prime(num))

    return prime_sum


print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_primes([2, 3, 4, 11, 20, 50, 71]))
print(sum_primes([]))
