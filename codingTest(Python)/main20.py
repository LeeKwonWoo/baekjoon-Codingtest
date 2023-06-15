# NO 11508
N = int(input())
C = [0] * N
sum = 0
for i in range(N):
  C[i] = int(input())
C.sort(reverse=True)

for i in range(0, N, 3):
  if i == N - 1:
    sum += C[i]
    break
  sum += C[i] + C[i + 1]

print(sum)
