def MakeChange(n):
    coins = [100, 25, 10, 5, 1]
    S = [] # conjunto solução
    soma = 0
    while (soma != n):
        for c in coins:
            if (soma + c <= n):
                S.append(c)
                soma += c
                break
    return S

print(MakeChange(123))