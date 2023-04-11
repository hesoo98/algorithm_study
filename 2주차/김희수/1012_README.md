### [silver 2] 1012: 바이러스
https://www.acmicpc.net/problem/1012
#### 입력 
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. <br>
그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50),<br>
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.<br>
그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.<br><br>

#### 출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.<br><br>


<details>
<summary>DFS 재귀로 작성한 코드</summary>

```python

# 1012 유기농 배추
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


```

</details>


### 문제 풀이
2차원배열 형태를 이용하여 어떤형태로 배추밭이 생겼는지 변환해주는것부터 먼저해준다.<br>
순서가 헷갈릴 수 있는데 배열,리스트는 왼쪽에서 오른쪽으로, 위에서 아래로 갈 수록 크다고 생각한다.<br>
지렁이가 있는곳이 1인데 지렁이가 있는곳기준 상하좌우 한칸옆에 지렁이가 있으면 인접한것으로 보고,<br>
인접한 지렁이들을 다 이었을때 하나의 덩어리라고 생각하며 그 덩어리들을 새는것이 목표이다.<br>
<br><br>

좌표를 입력받고 함수를 돌았을때 밭의 범위를 벗어나지 않고 지렁이가 있는 장소이면 count+=1을 해준다.<br>
한번 지나간 지렁이가 있던 장소는 나중에 또 탐색하는것을 막기위해 0을 넣어서 다시 탐색하는일이 없도록 한다.<br>




---
