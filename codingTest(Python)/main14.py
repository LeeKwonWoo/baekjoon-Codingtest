# NO 1541

o = input()
o = o.split('-')
op = []

for i in range(len(o)):
  if '+' in o[i]:
    result = 0
    op = o[i].split('+')
    for j in range(len(op)):
      op[j] = int(op[j])
      result += op[j]
    o[i] = result

result = 0
for i in range(len(o)):
  if len(op) > 0:
    if i == 0:
      result = int(o[i]) - result
    else:
      result -= int(o[i])
  else:
    if i == 0:
      result = int(o[i])
    else:
      result -= int(o[i])
print(result)
