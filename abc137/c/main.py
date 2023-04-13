from collections import defaultdict

N = int(input())

num = defaultdict(int)
for i in range(N):
    s = "".join(sorted(input()))
    num[s] += 1 # 文字列をキーとして数をカウント

result = 0
for s in num.keys():

    n = num[s] # 文字列sのカウントを取得

    result += n * (n-1) // 2

print(result)