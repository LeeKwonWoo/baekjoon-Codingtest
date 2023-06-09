# NO 16953
A, B = list(map(int, input().split()))
cnt = 0

while True:

  if A == B:
    break
  elif A > B:
    print(-1)
    exit()
  else:
    s = str(B)
  
    if '1' in s[len(s) - 1]:
      B = int(s[:len(s) - 1])
  
    elif B % 2 == 0:
      B = int(B / 2)
    else:
      print(-1)
      exit()
    cnt += 1

print(cnt + 1)
