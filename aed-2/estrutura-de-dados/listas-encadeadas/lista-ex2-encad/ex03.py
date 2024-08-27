class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere(self, valor, posicao):
        novo_no = No(valor)
        if posicao == 0:
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no
        else:
            anterior = self._acessar_no(posicao - 1)
            novo_no.proximo = anterior.proximo
            anterior.proximo = novo_no

    def _acessar_no(self, posicao):
        atual = self.primeiro
        pos = 0
        while atual and pos < posicao:
            atual = atual.proximo
            pos += 1
        return atual

    def imprimir_reverso(self):
        self._imprimir_reverso_recursivo(self.primeiro)
    
    def _imprimir_reverso_recursivo(self, no):
        if no:
            self._imprimir_reverso_recursivo(no.proximo)
            print(no.valor, end=" ")

lista = ListaEncadeada()
lista.insere(1, 0)
lista.insere(2, 1)
lista.insere(3, 2)
lista.insere(4, 3)

print("Lista original:")
no_atual = lista.primeiro
while no_atual:
    print(no_atual.valor, end=" ")
    no_atual = no_atual.proximo

print("\n\nImpressão reversa:")
lista.imprimir_reverso()