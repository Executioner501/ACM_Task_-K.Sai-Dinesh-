def prime_factors(N):
    factors = []
    divisor = 2

    while divisor <= N:
        if N % divisor == 0:
            factors.append(divisor)
            N = N // divisor
        else:
            divisor += 1

    if factors:
        return factors[-1]
    else:
        return none
T=int(input())
for _ in range(T):
    N = int(input("Enter a number: "))
    largest_factor=prime_factors(N)
    maxno=print(largest_factor)



