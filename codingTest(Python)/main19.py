# NO 11047
N, K = list(map(int, input().split()))
A = [0] * N
idx = 0
sum = 0
for i in range(N):
  A[i] = int(input())
  if A[i] <= K:
    idx = i

for i in range(idx, -1, -1):
  result = K // A[i]
  sum += result
  K = K % A[i]

  if A[i] <= K:
    idx = i

print(sum)