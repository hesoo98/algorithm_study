# DFS, BFS 탐색<br><br>


![dfsbfs](https://user-images.githubusercontent.com/8851063/230274180-1e363302-8ecb-415d-bd90-488c840dcb5c.png)

<br>

### 깊이 우선 탐색(DFS)
> 그래프에서 깊은 부분을 우선적으로 탐색하는 방식이다.

* DFS는 깊이 우선 탐색으로 스택을 이용한다.
* DFS는 재귀로도 간단히 구현가능 할 수 있다. 깊은 곳으로 우선 탐색하기 때문에

<br>

### DFS로 노드들을 방문하는 법
1. 시작 노드를 스택에 넣고 방문 처리를 한다.
2. 인접 노드중 방문하지 않은 노드가 있으면 그 노드를 스택에 넣는다 그리고 방문한다. 혹은 인접 노드를 전부 방문했을 경우 스택에서 최상단 노드를 꺼낸다.
3. 2를 수행하지 못할 때까지 계속 반복한다.

<br>

### 너비 우선 탐색(BFS)
> 출발 노드로부터 가까운 노드들 먼저 차례로 탐색하는 방식이다.

* DFS는 깊이 우선 탐색으로 스택을 이용한다.
* DFS는 재귀로도 간단히 구현가능 할 수 있다. 깊은 곳으로 우선 탐색하기 때문에



### BFS로 노드들을 방문하는 법
1. 시작 노드를 큐에 넣고 방문 처리 한다. 
2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문안한 노드를 모두 큐에 삽입하고 방문처리함.
3. 2를 수행하지 못할 때까지 계속 반복한다.

<br><br>





### [silver 3] 2606: 바이러스
#### 입력 
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.</br>
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. </br>
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.<br><br>

#### 출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.<br><br>


<details>
<summary>DFS 재귀로 작성한 코드</summary>

```python
def dfs(v):
    global resultcount
    visited[v] = True  # 방문처리하고
    resultcount += 1
    for x in graph[v]:
        if visited[x] == False:  # 방문하지 않았으면
            dfs(x)


global resultcount
resultcount = 0
v_count = int(input())
e_count = int(input())
graph = [[] for x in range(v_count + 1)]  # 0번째는 비워둔다, 그래프를 만들고 시작.
visited = [False] * (v_count + 1)
for i in range(e_count):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(resultcount - 1)

```

</details>


### 코드 설명



---
출처<br>
이미지 : https://dev.to/danimal92/difference-between-depth-first-search-and-breadth-first-search-6om
