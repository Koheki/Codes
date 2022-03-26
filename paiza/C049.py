N = int(input())
ans = 0
prev = 1

for _ in range(N):
    n = int(input())
    ans += abs(n - prev)
    prev = n

print(ans)