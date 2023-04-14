### [silver 2] 4963: 섬의 개수
https://www.acmicpc.net/problem/4963
#### 입력 
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.<br>
둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.<br>
입력의 마지막 줄에는 0이 두 개 주어진다.<br><br>

#### 출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.<br><br>


<details>
<summary>BFS로 작성한 코드</summary>

```python

# 1012 유기농 배추
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


```

</details>


### 문제 풀이
유기농배추와 비슷한 유형의 문제이다. bfs라 큐를 이용하여 구현하였고, 나머지는 거의 비슷한데<br>
중앙에 좌표를 이동하는 배열 부분이 4가지 방향 더 추가된것을 볼 수 있다. 대각선 4가지가 추가된것이다.<br>
그외의 설명은 유기농배추와 동일하다.




---
