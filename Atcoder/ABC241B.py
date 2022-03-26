N,M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

pasta = {}
flag = 1

for a in A:
    if a in pasta:
        pasta[a] += 1
    else:
        pasta[a] = 1


for b in B:

    if b in pasta:
        pasta[b] -= 1
    else:
        flag = 0
        break

if min(pasta.values()) < 0 or flag == 0:
    print("No")
else:
    print("Yes")
