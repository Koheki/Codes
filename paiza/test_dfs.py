import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限
h,w = map(int,input().split())
c = [list(input()) for i in range(h)]

def dfs(x,y):
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == "#": # 壁に当たったり、探索範囲外になった場合はreturn
        return
    if c[x][y] == "g": # ゴールを見つけたら”Yes”を出力して終了
        return True

    c[x][y] = "#" #探索済みを示すためのマーキング
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = i, j # スタート位置
            
print(dfs(sx, sy))

