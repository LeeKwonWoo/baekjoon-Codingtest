# NO 1026

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
AA = [0] * N
BB = [0] * N
sum = 0
for i in range(N):
  AA[B.index(max(B))] = A[i]
  BB[B.index(max(B))] = max(B)
  B[B.index(max(B))] = -1

for i in range(N):
  sum = sum + (AA[i] * BB[i])

print(sum)