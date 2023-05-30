#상하좌우

N = int(input())
A = input().split()

x, y = 1, 1

for i in A:
  
  if i in 'L':
    dy = -1
    y = y + dy
    if x > N or x < 1 or y > N or y < 1:
      dy = 1
      y = y + dy

  elif i in 'R':
    dy = 1
    y = y + dy
    if x > N or x < 1 or y > N or y < 1:
      dy = -1
      y = y + dy
  elif i in 'U':
    dx = -1
    x = x + dx
    if x > N or x < 1 or y > N or y < 1:
      dx = 1
      x = x + dx
      
  elif i in 'D':
    dx = 1
    x = x + dx
    if x > N or x < 1 or y > N or y < 1:
      dx = -1
      x = x + dx
      
print(x, y)
