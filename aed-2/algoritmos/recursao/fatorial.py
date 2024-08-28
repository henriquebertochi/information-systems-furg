def Fatorial_ireracao(n): #iteracao = repeticao
	resultado = 1
	while n > 0:
		resultado = resultado * n
		n = n - 1
	return resultado

print(Fatorial_ireracao(4))