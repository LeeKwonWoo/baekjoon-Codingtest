# NO 14469 NO
N = int(input())
a = [0] * N
for i in range(N):
  a[i] = list(map(int, input().split()))
a.sort()
sum = a[0][0] + a[0][1]
for i in range(N):

  if i == N - 1:
    break

  if sum <= a[i + 1][0]:
    sum += a[i + 1][0] + a[i + 1][1] - sum
  else:
    sum += a[i + 1][1]
print(sum)
