# 곱하기 혹은 더하기: 문제 설명
S = input()
n = [0] * len(S)
result = 0
for i in range(len(S)):
  n[i] = int(S[i])
  if n[i] != 0:
    result = result * n[i]
  elif n[i] == 1 or n[i] == 0:
    result = result + n[i]
print(result)