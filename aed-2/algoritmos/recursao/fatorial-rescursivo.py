def Fatorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * Fatorial_rec(n-1)
    
print(Fatorial_rec(4))