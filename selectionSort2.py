N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

for i in range(N-1, 0, -1):
    m = A.index(max(A[:i+1]))

    if i != m:
        A[m], A[i] = A[i], A[m]
        cnt += 1
        if cnt == K:
            break
s = ''
if K > cnt:
    print(-1)
else:
    for i in range(N):
        s += str(A[i]) + " "
    print(s)
