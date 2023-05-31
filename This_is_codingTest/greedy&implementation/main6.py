# 왕실의 나이트
X = input()
rows = list(range(8))
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
c = cols.index(X[0])
r = int(X[1]) - 1
cnt = 0


def move(x, y, cnt):
  nx = x + c
  ny = y + r
  if 8 < nx or nx < 0 or 8 < ny or ny < 0:
    nx = c - x
    nx = r - y
  else:
    cnt += 1

  return cnt


cnt = move(-1, -2, cnt)
cnt = move(-1, 2, cnt)
cnt = move(1, 2, cnt)
cnt = move(1, -2, cnt)
cnt = move(-2, -1, cnt)
cnt = move(-2, 1, cnt)
cnt = move(2, 1, cnt)
cnt = move(2, -1, cnt)

print(cnt)
