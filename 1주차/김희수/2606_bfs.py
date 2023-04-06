# https://www.acmicpc.net/problem/2606
# 문제이름 : 바이러스, 난이도 : 실버 3
from collections import deque

resultcount = 0
v_count = int(input())  # 컴퓨터 개수
e_count = int(input())  # 연결선 개수
graph = [[] for x in range(v_count + 1)]  # 0번째는 비워둔다, 그래프를 만들고 시작.
visited = [False] * (v_count + 1)  # 방문체크

for i in range(e_count):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True  # 시작 노드(1번컴터)를 방문처리
queue = deque([True])  # 시작노드를 큐에 넣음

while queue:
    nextqueue = queue.popleft()  # 큐에서 노드를 꺼내고
    for i in graph[nextqueue]:
        if visited[i] == False:
            queue.append(i)  # 해당 노드의 인접 노드중 방문안한 노드 모두 큐에 삽입
            visited[i] = True
            resultcount += 1

print(resultcount)