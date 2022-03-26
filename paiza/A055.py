
H,W = map(int,input().split())

grid = []
x,y = 0,0


for h in range(H):
    s = [ i for i in input()]

    if "S" in s:
        x = s.index("S")
        y = h

    grid.append(s)


def dfs(x,y):
    if grid[y][x] == "#":
        return
    else:
        if (0 <= x < W-1)  and  (0 <= y < H-1) :
            grid[y][x] = "#"
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

dfs(x,y)

flag = 0

for l in grid:
    if l.count(".") == 1:
        flag = 1
        break

    else:
        continue


if flag == 1:
    print("Yes")
else:
    print("NO")
