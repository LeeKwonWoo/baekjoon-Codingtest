# NO 1931
N = int(input())
I = [0] * N
for i in range(N):
  I[i] = list(map(int, input().split()))

I.sort(key=lambda x: [x[1], x[0]])
print(I)
cnt = 0
i = 0
idx = 0
while i < N:
  if cnt == 0 or I[idx][1] <= I[i][0]:
    idx = i
    cnt += 1
  i += 1

print(cnt)
