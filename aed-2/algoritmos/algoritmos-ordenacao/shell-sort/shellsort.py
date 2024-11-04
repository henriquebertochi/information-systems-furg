def shellsort(A):
    n = len(A)
    inc = n // 2  # Define o incremento inicial como metade do tamanho do array

    while inc > 0:
        for j in range(inc, n):
            key = A[j]
            i = j - inc
            # Move elementos maiores que a chave para frente no subgrupo
            while i >= 0 and A[i] > key:
                A[i + inc] = A[i]
                i -= inc
            A[i + inc] = key  # Insere a chave na posição correta no subgrupo
        inc //= 2  # Reduz o incremento pela metade a cada iteração

    return A

test_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = shellsort(test_array)
print(sorted_array)