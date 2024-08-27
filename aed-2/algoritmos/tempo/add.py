#Algoritmo tradicional de adicao
# coding=utf-8
import time
import numpy as np

n = 800000          # numero de algarismos
op1 = np.ones(n)*9  # geracao do operando 1 com todos algarismos iguais a 9
op2 = np.ones(n)*9  # geracao do operando 2 com todos algarismos iguais a 9
R = np.zeros(n+1)   # resultado

start_time = time.time()
vai_um=0
for i in range(n-1, -1, -1):       # percorre os operando da direita para esquerda
    aux_soma=op1[i]+op2[i]+vai_um  # realiza a soma digito por digito
    R[i+1]=aux_soma % 10           # mod - R[i+1] recebe o resto da divisao inteira por 10
    vai_um=aux_soma // 10          # div - resultado da divisao inteira por 10 eh atribuido a vai_um
R[0]=vai_um                        # ultimo vai_um
end_time = time.time()
print(R)

print("--- %s seconds ---" % (end_time- start_time)) # mostra tempo de execução