# NO 2839
n = int(input())
cnt = 0
r = n % 5

if n <= 2 or n == 4 or n > 5000 or n == 7:
  print(-1)
  exit()

if r % 3 == 0:
  cnt += n // 5
  cnt += r // 3

else:
  while True:
    n = n - 3
    cnt += 1
    if n % 5 == 0:
      break
  cnt += n // 5

print(cnt)