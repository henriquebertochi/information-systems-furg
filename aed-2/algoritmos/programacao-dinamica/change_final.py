MAX_INT=2**63 - 1 # maior inteiro positivo de 64 bits
N=8 #valor do troco
d=[1,4,6] #tipos de moedas

def change(i,n):
    if n==0:
        return 0
    elif n<0: # moeda escolhida maior que o montante que resta
        return MAX_INT
    elif i<0: # tipos de moedas extrapolado
        return MAX_INT
    else:
        return min(1+change(i,n-d[i]), change(i-1,n))

troco=change(len(d)-1,N)
if troco>=MAX_INT:
    print("Valor de troco impossível de ser pago.")
else:
    print("Quantidade de moedas de troco: ", troco)