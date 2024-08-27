def BubbleSort(A):
    n = len(A)
    for j in range(n):
        for i in range(n-1, 0, -1): # range(inicio, fim, passo)
            if A[i] < A[j]:
                if A[i] < A[i-1]:
                    tmp = A[i-1]
                    A[i-1] = A[i]
                    A[i] = tmp
    return A

A = [5, 2, 4, 6, 1, 3]
print(BubbleSort(A))