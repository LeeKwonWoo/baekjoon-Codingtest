# NO 10610
N = list(input())
N = sorted(N, reverse=True)
s = ""
for i in N:
  s += i
s = int(s)

if s % 30 == 0:
  print(s)
else:
  print(-1)
