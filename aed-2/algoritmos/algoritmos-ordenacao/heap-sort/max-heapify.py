def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r < heap_size and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)


def build_max_heap(A):
    heap_size = len(A)
    # Começa em (heap_size // 2) - 1 e vai até 0
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(A, i, heap_size)


def heapsort(A):
    build_max_heap(A)
    heap_size = len(A)
    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)
    return A


test_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = heapsort(test_array)
print(sorted_array)