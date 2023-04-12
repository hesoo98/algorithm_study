from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            next_x = xx + dx[i]
            next_y = yy + dy[i]

        if (0 <= next_x < n and 0 <= next_y < m) and box[next_x][next_y] == 1:
            queue.append([next_x, next_y])
            box[next_x][next_y] = 0

    return 1


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    box = [[0] * m for xx in range(n)]
    for __ in range(k):
        a, b = map(int, input().split())
        box[b][a] = 1
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for b in range(n):
        for a in range(m):
            if box[b][a] == 1:
                cnt += bfs(b, a)

    print(cnt)
