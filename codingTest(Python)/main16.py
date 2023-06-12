# NO 18310
N = int(input())
M = list(map(int, input().split()))
M.sort()
median = 0
m = []
MM = []
if N % 2 == 0:
  median = int((M[int(len(M) / 2) - 1] + M[int(len(M) / 2)]) / 2)
  MM = M
  m = list(map(lambda x: abs(x - median), MM))
  print(M[m.index(min(m))])
else:
  median = M[int(len(M) / 2)]
  MM = M
  m = list(map(lambda x: abs(x - median), MM))
  print(M[m.index(min(m))])
