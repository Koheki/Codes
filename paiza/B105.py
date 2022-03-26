N,H,W = map(int,input().split())

board = [[ 0 for _ in range(W) ] for _ in range(H)]
L = {1,2,3}

def converter(i,j):
    if j == 0 or i == j:
        return i
    else:
        return (L-{i,j}).pop()

for _ in range(N):
    x1,y1,s1 = map(int,input().split())
    x2,y2,s2 = map(int,input().split())
    x3,y3,s3 = map(int,input().split())

    board[y1:y1+s1] = [ [converter(1,l[i]) if x1 <= i < x1+s1 else l[i] for i in range(len(l)) ]  for l in board[y1:y1+s1]]
    # print(x1,y1,s1)
    # print(board)
    
    board[y2:y2+s2] = [ [converter(2,l[i]) if x2 <= i < x2+s2 else l[i] for i in range(len(l)) ]  for l in board[y2:y2+s2]]
    # print(x2,y2,s2)
    # print(board)
    
    board[y3:y3+s3] = [ [converter(3,l[i]) if x3 <= i < x3+s3 else l[i] for i in range(len(l)) ]  for l in board[y3:y3+s3]]


    # print(x3,y3,s3)
    # print(board)

ans1 = sum([b.count(1) for b in board])
ans2 = sum([b.count(2) for b in board])
ans3 = sum([b.count(3) for b in board])

print(ans1,ans2,ans3)
