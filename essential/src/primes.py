def primesUpTo(num):
    if not isinstance(num, int) or num < 0: return None

    primes = [2] if num >=2 else []
    for number in range(3, num):
        sqrtNum = number ** 0.5
        for factor in primes:
            if number % factor == 0: break # number not prime

            if factor > sqrtNum:
                primes.append(number)
                break
    return primes

print(primesUpTo(10))