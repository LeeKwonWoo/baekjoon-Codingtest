# NO 2012
N = int(input())
rank = [0] * N
for i in range(N):
  rank[i] = int(input())
rank.sort()
sum = 0
for i in range(N):
  n = i + 1
  sum += abs(rank[i] - n)
print(sum)
