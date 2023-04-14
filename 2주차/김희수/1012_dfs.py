# 1012 유기농 배추 dfs
import sys

sys.setrecursionlimit(100000)


def dfs(x, y):
    if x < 0 or y < 0 or y > m - 1 or x > n - 1:
        return False
    if box[x][y] == 0:
        return False
    elif box[x][y] == 1:
        box[x][y] = 0
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    box = [[0] * m for xx in range(n)]
    for __ in range(k):
        a, b = map(int, input().split())
        box[b][a] = 1
    cnt = 0
    for b in range(n):
        for a in range(m):
            if dfs(b, a):
                cnt += 1
    print(cnt)
