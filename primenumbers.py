def list_primes(n):
    nums = list(range(2, n + 1))
    result = list()

    while nums:
        i = nums.pop(0)
        result.append(i)
        for num in list(nums):
            if num % i == 0:
                nums.remove(num)
    return result

def is_prime(n):
    return n in list_primes(n)

print(list_primes(2000))