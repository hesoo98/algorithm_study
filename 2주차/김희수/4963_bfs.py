# https://www.acmicpc.net/problem/4963
# 실버2
from pprint import pprint
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append([x, y])  # 우선 큐에넣고
    while queue:  # 큐의 사이즈가 없으면 탐색 그만
        current_x, current_y = queue.popleft()  # 처음 받은 좌표를 바로 pop한다.

        # 범위안벗어나고, 섬인것만 순환한다
        for i in range(8):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < h and 0 <= next_y < w and box[next_x][next_y] == 1:
                box[next_x][next_y] = 0  # 재탐색하지 말라고 0으로 넣어줌.
                queue.append([next_x, next_y])  # 탐색할 좌표 큐에 넣어줌
    return 1

# 상하좌우 + 대각선 까지해서 총8방향을 돌기위해 더 추가하여야함.
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, 1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    cnt = 0
    # line = [[0] * w for x in range(h)]
    box = []
    for i in range(h):
        box.append([int(x) for x in input().split()])

    for j in range(w):
        for i in range(h):
            if box[i][j] == 1:
                cnt += bfs(i, j)
    print(cnt)
