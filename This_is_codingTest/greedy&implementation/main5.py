# 시각
N = int(input())
m = 60
s = 60
cnt = 0
for i in range(N + 1):
  s1 = str(i)
  for j in range(m):
    s2 = str(j)
    for k in range(s):
      s3 = str(k)
      st = s1 + s2 + s3
      if '3' in st:
        cnt += 1
print(cnt)
