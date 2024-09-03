MAX_INT = 2**63 - 1  # maior inteiro positivo de 64 bits
N = 8
d = [1, 4]


def change(i, n):
    if n == 0:
        return 0

    elif n < 0:  # moeda escolhida maior que o montante que resta
        return MAX_INT

    else:
        return 1+change(i, n-d[i])

troco = change(1, N)
if troco >= MAX_INT:
    print("Valor de troco impossível de ser pago.")
else:
    print("Quantidade de moedas de troco: ", troco)
