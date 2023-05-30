# 모험가 길드
N = int(input())
X = list(map(int, input().split()))
X.sort()
cnt = 0
result = 0

for i in X:
  cnt += 1
  if cnt >= i:
    result += 1
    cnt = 0
  else:
    continue
print(result)
