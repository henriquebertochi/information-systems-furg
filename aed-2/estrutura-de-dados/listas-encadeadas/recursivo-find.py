# Reimplemente de maneira recursiva o método de busca nas seguintes estruturas de dados vistas no primeiro semestre: Lista encadeada (busca linear)

class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None
        self.info = valor

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere(self, valor, posicao):
        novo_no = No(valor)
        if posicao == 0:
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no
        else:
            anterior = self.acessar_no(posicao - 1)
            novo_no.proximo = anterior.proximo
            anterior.proximo = novo_no
        print(f"Inserido valor {valor} na posição {posicao}")

    def acessar_no(self, posicao):
        atual = self.primeiro
        pos = 0
        while atual and pos < posicao:
            atual = atual.proximo
            pos += 1
        return atual

    def len_lista(self):
        atual = self.primeiro
        pos = 0
        while atual:
            atual = atual.proximo
            pos += 1
        print(f"O tamanho da lista é {pos}")
        return pos
    
    def busca(self, valor, nodo=None, posicao=0):
        if posicao == 0:
            nodo = self.primeiro
        if nodo is None:
            return False
        if nodo.info == valor:
            return posicao
        if nodo.info != valor:
            return self.busca(valor, nodo.proximo, posicao + 1)

lista = ListaEncadeada()
lista.insere(10, 0)
lista.insere(20, 1)
lista.insere(30, 2)
lista.insere(40, 3)
print(lista.busca(20))
print(lista.busca(30))
print(lista.busca(40))
print(lista.busca(50))