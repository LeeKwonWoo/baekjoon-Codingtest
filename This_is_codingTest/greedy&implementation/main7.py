# dfs
# def dfs(graph, v, visited):
#   visited[v] = True
#   print(v, end=' ')
#   for i in graph[v]:
#     if not visited[i]:
#       dfs(graph, i, visited)

# graph = []
# visited = [False] * 9
# dfs(graph, 1, visited)

# 음료수 얼음 얼려먹기
N, M = list(map(int, input().split()))
graph = []
for i in range(N):
  graph.append(list(map(int, input())))

cnt = 0


def dfs(x, y):
  if x >= N or x < 0 or y >= M or y < 0:
    return False

  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x + 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)
    dfs(x - 1, y)
    return True

  return False


for i in range(N):
  for j in range(M):
    if dfs(i, j) == True:
      cnt += 1

print(cnt)