def fibonacci_sequence(limit):
    series = [1, 2]  
    while series[-1] + series[-2] <= limit:
        next_term = series[-1] + series[-2]
        series.append(next_term)
    return series

def sum_even_terms(series):
    even_sum = 0
    for term in series:
        if term % 2 == 0:
            even_sum += term
    return even_sum
T=int(input())
for _ in range(T):
    N = int(input(""))

    fib_sequence = fibonacci_sequence(N)
    even_sum = sum_even_terms(fib_sequence)
    print(even_sum)

