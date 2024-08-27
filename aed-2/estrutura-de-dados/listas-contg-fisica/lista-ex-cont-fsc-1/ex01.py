# exercício parte do pressuposto que a primeira posição é 0

class ListaProdutos:
    def __init__(self):
        self.lista = []

    def inicializa(self):
        self.lista = []
        print("Lista inicializada:", self.lista)

    def inserir(self, produto, posicao):
        if posicao <= len(self.lista):
            self.lista.insert(posicao, produto)
            print(f"Inserido {produto} na posição {posicao}:", self.lista)
        else:
            print(f"Erro: posição {posicao} inválida para inserção.")

    def remover(self, posicao):
        if posicao <= len(self.lista):
            produto_removido = self.lista.pop(posicao)
            print(
                f"Removido produto da posição {posicao}: {produto_removido}. Lista atual:", self.lista)
        else:
            print(f"Erro: posição {posicao} inválida para remoção.")

    def localizar(self, produto):
        posicao = None
        for i in range(len(self.lista)):
            if self.lista[i] == produto:
                posicao = i
                break
        if posicao is not None:
            print(f"Posição de {produto} na lista:", posicao)
        else:
            print(f"{produto} não encontrado na lista.")

    def limpar(self):
        self.lista = []
        print("Lista limpa:", self.lista)


lista = ListaProdutos()
lista.inicializa()
lista.inserir("Produto A", 0)
lista.inserir("Produto B", 1)
lista.inserir("Produto C", 2)
lista.remover(1)
lista.inserir("Produto D", 3)
lista.inserir("Produto E", 2)
lista.localizar("Produto C")
lista.localizar("Produto F")
lista.limpar()
