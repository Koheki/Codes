N = int(input())
A = [ int(n) for n in input().split()]

ans = [0]*(2001)

for a in A:
    ans[a] += 1

for i in range(N+1):
    if ans[i] == 0:
        print(i)
        break
    else:
        continue