from collections import deque
#bfs

# def bfs(graph, start, visited):
#   queue = deque([start])
#   visited[start] = True
#   while queue:
#     v = queue.popleft()
#     for i in graph[v]:
#
#if not visited[i]:
#queue.append(i)
#       visited[i] = True

# graph = []
# visited = [False] * 9
# bfs(graph, 1, visited)

# 미로탈출
N, M = list(map(int, input().split()))
graph = []
for i in range(N):
  graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(len(dx)):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= N or nx < 0 or ny >= M or ny < 0:
        continue

      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[N - 1][M - 1]


print(bfs(0, 0))
