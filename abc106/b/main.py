#!/usr/bin/env python3
N = input()
N = int(N)
n_list = list(range(1, N+1, 2))

def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def cal_divisors(n_list):
    result = 0
    for n in n_list:
        r = len(make_divisors(n))
        if r == 8:
            result += 1
    return result

result = cal_divisors(n_list)
print(result)