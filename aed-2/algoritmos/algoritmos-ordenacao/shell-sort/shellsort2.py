def shellsort(A):
    n = len(A)
    
    # Inicializa o incremento usando a sequência de Shell (1, 4, 13, 40, 121, ...)
    inc = 1
    while inc < n:
        inc = inc * 3 + 1
    
    # Reduz o incremento pela sequência inversa
    inc //= 3
    while inc > 0:
        for j in range(inc, n):
            key = A[j]
            i = j - inc
            # Move os elementos maiores que a chave no subgrupo
            while i >= 0 and A[i] > key:
                A[i + inc] = A[i]
                i -= inc
            A[i + inc] = key  # Insere a chave na posição correta no subgrupo
        inc //= 3  # Reduz o incremento pela sequência inversa
    
    return A

# Testando a função com uma lista de exemplo
test_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = shellsort(test_array)
print(sorted_array)
