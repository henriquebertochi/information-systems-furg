MAX_INT=2**63 - 1 # maior inteiro positivo de 64 bits
N=8
d=[1]

def change(n):
    if n==0:
        return 0
    elif n<0: # moeda escolhida maior que o montante que resta
	    return MAX_INT
    else:
        return 1+change(n-d[0])

troco=change(N)
if troco>=MAX_INT:
    print("Valor de troco impossível de ser pago.")
else:
    print("Quantidade de moedas de troco: ", troco)