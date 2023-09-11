def sum_multiples_3_and_5_below_N(N):
    sum_of_multiples = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i
    return sum_of_multiples
T = int(input("Enter the number of test cases: "))
for _ in range(T):
    # Input N for each test case
    N = int(input("Enter N: "))
    result = (sum_multiples_3_and_5_below_N(N))
    print(result)