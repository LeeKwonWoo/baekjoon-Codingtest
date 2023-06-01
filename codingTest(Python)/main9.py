# NO 2606
from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * len(graph)

def bfs(graph, started, visited):
  cnt = 0
  queue = deque([started])
  visited[started] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        cnt += 1
  return cnt


print(bfs(graph, 1, visited))


# for i in graph:
#   n = 0
#   for j in graph:
#     if i[0] == j[0] or i[0] == j[1] or i[1] == j[0] or i[1] == j[1]:
#       continue
#     else:
#       n += 1
#       if n == M - 1:
#         graph.pop(graph.index([i[0], i[1]]))

# n_graph = []
# for i in graph:
#   n_graph += i
# n_graph = list(set(n_graph))
# print(len(n_graph)-1)
