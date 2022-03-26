
N, K  = map(int,input().split())
A = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]

table = [0] * N

for i in range(1,N):
    fb = 0
    fa = 0

    if table[i-1] == 0:
        # B[i]はOKか？
        if abs(B[i] - B[i-1]) <= K or abs(B[i] - A[i-1]) <= K:
            fb = 1
        # A[i]はOKか？
        if abs(A[i] - A[i-1]) <= K or abs(A[i] - B[i-1]) <= K:
            fa = 1

    else:
        if abs(B[i] - table[i-1]) <= K:
            fb = 1
        if abs(A[i] - table[i-1]) <= K:
            fa = 1

    if fb ==1 and fa ==1:
        continue
    elif fb == 1:
        table[i] = B[i]
    elif fa == 1:
        table[i] = A[i]
    else:
        print("No")
        exit()

print("Yes")

