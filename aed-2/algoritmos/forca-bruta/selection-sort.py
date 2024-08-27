def SelectionSort(A):
    n = len(A)
    for j in range(n-1):
        smallest = j
        for i in range(j+1, n):
            if A[i] < A[smallest]:
                smallest = i
        tmp = A[j]
        A[j] = A[smallest]
        A[smallest] = tmp
    return A

A = [5, 2, 4, 6, 1, 3]
print(SelectionSort(A))