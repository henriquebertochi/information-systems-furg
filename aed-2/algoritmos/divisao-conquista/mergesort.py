def merge(A, p, q, r):
    n1 = q - p
    n2 = r - q
    L = []
    R = []
    inf = 999999999999999
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j])
    L.append(inf)
    R.append(inf)
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


A = [2, 4, 0, 5, 15, 7, 1, 66, 2, 3, 6, 12, 90]
merge_sort(A, 0, len(A))
print(A)

#resolver com o gpt, 0 esta ficando no meio e outras tentativas tambem dao errado