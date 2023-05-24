# 주어진 수를 key 주어진 index를 value로 하는 맵 또는 딕셔너리
# A.keys() A.values()
N, K = map(int, input().split())
k = list(map(int, input().split()))
ks = sorted(k)
A = {a:i for i, a in enumerate(k)}
cnt = 0

for i in range(N-1, -1, -1):
    if k[i] != ks[i]:
        temp = [k[i], k[A[ks[i]]]]
        k[i], k[A[ks[i]]] = k[A[ks[i]]], k[i]
        A[temp[0]], A[temp[1]] = A[temp[1]], A[temp[0]]
        cnt += 1
        if cnt == K:
            print(' '.join(str(n) for n in k))
            break

if K > cnt:
    print(-1)