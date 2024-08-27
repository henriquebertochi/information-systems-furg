#Algoritmo tradicional de multiplicacao
# coding=utf-8
import time
import numpy as np

n = 800                 # numero de algarismos
op1 = np.ones(n) * 9    # geracao do operando 1 com todos algarismos iguais a 9
op2 = np.ones(n) * 9    # geracao do operando 2 com todos algarismos iguais a 9
R = np.zeros(n + n)     # resultado final
R_aux = np.zeros(n + 1) # resultados intermediarios

start_time = time.time()
for i in range(n-1, -1, -1):                # percorre op1 da direita para esquerda
    vai_um = 0
    for j in range(n-1, -1, -1):            # percorre op2 da direita para esquerda
        aux_mult = op1[i] * op2[j] + vai_um # multiplica digitos e soma vai_um
        # print(aux_mult)
        R_aux[j + 1] = aux_mult % 10        # mod - R_aux[j + 1] recebe o resto da divisao inteira por 10
        # print(R_aux[j+1])
        vai_um = aux_mult // 10  # div      # div - resultado da divisao inteira por 10 eh atribuido a vai_um
        # print(vai_um)
    R_aux[0] = vai_um                       # ultimo vai_um

    vai_um = 0
    for j in range(n, -1, -1):              # resultado intermediario R_aux eh somado a R com deslocamento correto
        # print(R_aux[j])
        aux_soma = R_aux[j] + R[i + j] + vai_um
        R[i + j] = aux_soma % 10  # mod
        vai_um = aux_soma // 10  # div

end_time = time.time()
print(R)

print("--- %s seconds ---" % (end_time - start_time))
