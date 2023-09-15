def largest_prime_factor(N):
    factor = 2

    while factor * factor <= N:
        if N % factor == 0:
            N //= factor
        else:
            factor += 1

    return N

T = int(input())
for _ in range(T):
    N = int(input())
    largest_factor = largest_prime_factor(N)
    print(largest_factor)
