# NO 1448 NO
import sys

N = int(input())
a = [0] * N
for i in range(N):
  a[i] = int(sys.stdin.readline())
a.sort(reverse=True)
for i in range(N - 2):
  if a[i] < (a[i + 1] + a[i + 2]):
    print(a[i] + a[i + 1] + a[i + 2])
    exit()

print(-1)