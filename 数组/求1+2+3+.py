def sum_solution(n):
    if n == 1:
        return 1
    return n + sum_solution(n - 1)


print(sum_solution(10))
