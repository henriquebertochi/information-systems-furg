class ListaValores:
    def __init__(self):
        self.lista = []

    def inicializa(self, lista):
        self.lista = lista
        print("Lista inicializada:", self.lista)

    def buscarInserir(self, n1, n2):
        posicao = None
        for i in range(len(self.lista)):
            if self.lista[i] == n1:
                posicao = i
                break

        if posicao is not None:
            print(f"Posição de {n1} na lista:", posicao)
            self.lista.insert(posicao+1, n2)
            print(
                f"Inserido {n2} após {n1} na posição {posicao+1}:", self.lista)
        else:
            print(f"{n1} não encontrado na lista.")

n1 = 10
n2 = 5
lista = ListaValores()
lista.inicializa([13, 8, 10, 4, 20])
lista.buscarInserir(n1, n2)
