def StringMachine(T, P, n, m):
    for i in range(n - m):
        j = 0
        while j < m and T[i + j] == P[j]: 
            print(T[i + j], P[j]) # visual para entender
            j += 1
        if j == m:
            return i
    return -1

T = "AABRAACADABRAACAADABRA"
P = "AACAD"
n = len(T)
m = len(P)
print(StringMachine(T, P, n, m))