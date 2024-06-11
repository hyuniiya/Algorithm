import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

node, edge, start_node = map(int, input().split())
# graph = [[], [], [], [], [], []]
graph = []
for i in range(node + 1):  # 인덱스 0은 사용 안함
    graph.append([])
# 각 노드 연결하기
# graph = [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]
for i in range(edge):
    node_u, node_v = map(int, input().split())
    graph[node_u].append(node_v)
    graph[node_v].append(node_u)
#오름차순 정렬
#graph = [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]
for i in range(node + 1):
    graph[i].sort()

visited = [0] * (node + 1)  # 방문 여부
count = 1
def dfs(graph, start_node, visited):
    global count
    visited[start_node] = count

    for i in graph[start_node]:
        if visited[i] == 0:
            count += 1
            dfs(graph, i, visited)

dfs(graph, start_node, visited)

for i in range(1, node + 1):
    print(visited[i])