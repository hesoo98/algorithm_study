# https://www.acmicpc.net/problem/2606
# 문제이름 : 바이러스, 난이도 : 실버 3
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
#print(visited)
