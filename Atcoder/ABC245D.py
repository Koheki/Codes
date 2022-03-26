
N,M = map(int,input().split())

A = [int(n) for n in input().split()]
C = [int(n) for n in input().split()]

B = [0] * (M+1)

if C[0] != 0:
    B[0] = C[0]//A[0]

length = max(N,M)

for i in range(1, N+M+1):
    sp = C[i]








