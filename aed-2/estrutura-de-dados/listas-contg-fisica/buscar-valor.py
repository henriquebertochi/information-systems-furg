class ListaInt:
    def __init__(self):
        self.lista = []

    def inicializa(self, lista):
        self.lista = lista
        print("Lista inicializada:", self.lista)

    def buscar(self, valor):
        posicao = None
        for i in range(len(self.lista)):
            if self.lista[i] == valor:
                posicao = i
                break

        if posicao is not None:
            print(f"Posição de {valor} na lista:", posicao)
            return posicao
        else:
            print(f"{valor} não encontrado na lista.")
            return None

lista = ListaInt()
lista.inicializa([5, 8, 9, 3, 4, 2, 1])
lista.buscar(7)
lista.buscar(4)