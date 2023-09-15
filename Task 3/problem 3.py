def sum_multiples_3_and_5_below_N(N):
    n3 = (N - 1) // 3
    n5 = (N - 1) // 5
    n15 = (N - 1) // 15
    sum_of_3 = 3 * n3 * (n3 + 1) // 2
    sum_of_5 = 5 * n5 * (n5 + 1) // 2
    sum_of_15 = 15 * n15 * (n15 + 1) // 2
    result = sum_of_3 + sum_of_5 - sum_of_15
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    result = sum_multiples_3_and_5_below_N(N)
    print(result)
