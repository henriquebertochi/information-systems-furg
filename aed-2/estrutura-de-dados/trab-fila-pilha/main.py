'''

'''

from fila import Fila
from pilha import Pilha
from nodo import Nodo

fila = Fila()
fila.Inserir(8)
fila.Inserir(71)
fila.Inserir(16)
fila.Inserir(2)
fila.Inserir(25)
fila.Inserir(10)
print('Fila inicial:')
fila.Printar()

pilha_temp = Pilha()
pilha_ord = Pilha()

while not fila.Vazia():
    pilha_temp.Empilhar(fila.Consultar())
    fila.Remover()

    while not pilha_temp.Vazia():
        elem_temp = pilha_temp.Desempilhar()
        while not pilha_ord.Vazia() and pilha_ord.Consultar() > elem_temp:
            pilha_temp.Empilhar(pilha_ord.Desempilhar())
        pilha_ord.Empilhar(elem_temp)

while not pilha_ord.Vazia():
    pilha_temp.Empilhar(pilha_ord.Desempilhar())

while not pilha_temp.Vazia():
    fila.Inserir(pilha_temp.Desempilhar())
    
print('Fila ordenada:')
fila.Printar()