### [silver 2] 1012: 유기농 배추
https://www.acmicpc.net/problem/1012
#### 입력 
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. <br>
그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50),<br>
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.<br>
그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.<br><br>

#### 출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.<br><br>


<details>
<summary>BFS로 작성한 코드</summary>

```python

# 1012 유기농 배추
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


```

</details>


### 문제 풀이
좌표를 입력받고 함수를 돌았을때 밭의 범위를 벗어나지 않고 지렁이가 있는 장소이면 1을 반환하여 count += 1을 해준다.<br>
처음 1을 발견하면 그것을 큐에 넣고 바로 pop해준다. pop한것을 받아서 처음발견한 위치 기준 상하좌우에 1이있는지찾아보고<br>
있으면 그 좌표를 큐에 append해준다. 큐의 사이즈가 없어질때까지 근처의 좌표들을 다 돌면서 처음 발견한 좌표를 제외한<br>
이후에 찾은 좌표들은 방문후(큐에넣고 돈후) 재탐색을 막기 위해서 0으로 바꿔준다.<br>
만약에 그런식으로 1이있는 주위 탐색을 하고 없으면(큐가 사이즈가 0이되면) 함수는 종료되고 나와서 밭을 다시 탐색하면서<br>
1(지렁이)를 찾는다 찾으면 다시 bfs탐색을 한다.<br>
한번 지나간 지렁이가 있던 장소는 나중에 또 탐색하는것을 막기위해 0을 넣어서 다시 탐색하는일이 없도록 한다.<br>




---
