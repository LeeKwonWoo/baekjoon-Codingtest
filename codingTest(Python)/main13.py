# NO 11399
N = int(input())
P = list(map(int, input().split()))
P.sort()
sum = P[0]
for i in range(0, len(P), 1):
  if len(P) == i + 1:
    break
  for j in P[:i + 2]:
    sum += j

print(sum)