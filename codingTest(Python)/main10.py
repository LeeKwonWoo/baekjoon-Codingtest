# NO 1789
S = int(input())
sum, cnt = 0, 0
while True:
  sum += cnt
  if sum == S:
    break
  elif sum >= S:
    cnt -= 1
    break
  cnt += 1
print(cnt)
