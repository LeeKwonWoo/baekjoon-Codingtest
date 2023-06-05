# 14916
n = int(input())
cnt = 0
r = n % 5

if n <= 1 or n == 3:
  print(-1)
  exit()

if r % 2 == 0:
  cnt += n // 5
  cnt += r // 2

elif r % 2 == 1:
  while True:
    n = n - 2
    cnt += 1
    if n % 5 == 0:
      break
  cnt += n // 5

print(cnt)