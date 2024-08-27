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
        print(f"Inserido valor {valor} na posição {posicao}")

    def remove(self, posicao):
        if posicao == 0:
            removido = self.primeiro
            if self.primeiro:
                self.primeiro = self.primeiro.proximo
        else:
            anterior = self._acessar_no(posicao - 1)
            if anterior and anterior.proximo:
                removido = anterior.proximo
                anterior.proximo = removido.proximo
        if removido:
            print(f"Removido valor {removido.valor} da posição {posicao}")
            return removido.valor
        else:
            print(f"Nada foi removido na posição {posicao}")
            return None

    def posicao(self, valor):
        atual = self.primeiro
        pos = 0
        while atual:
            if atual.valor == valor:
                print(f"Posição do valor {valor} é {pos}")
                return pos
            atual = atual.proximo
            pos += 1
        print(f"Valor {valor} não encontrado na lista")
        return -1

    def valor(self, posicao):
        no = self._acessar_no(posicao)
        if no:
            print(f"Valor na posição {posicao} é {no.valor}")
            return no.valor
        else:
            print(f"Posição {posicao} inválida")
            return None

    def destroi(self):
        self.primeiro = None
        print("Lista destruída")

    def _acessar_no(self, posicao):
        atual = self.primeiro
        pos = 0
        while atual and pos < posicao:
            atual = atual.proximo
            pos += 1
        return atual

    def imprimir_lista(self):
        atual = self.primeiro
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

lista = ListaEncadeada()
lista.insere(10, 0)
lista.insere(20, 1)
lista.insere(30, 2)
lista.insere(40, 3)

lista.remove(2)

lista.posicao(40)

lista.valor(1)

lista.imprimir_lista()

lista.insere(50, 2)

lista.imprimir_lista()

lista.destroi()