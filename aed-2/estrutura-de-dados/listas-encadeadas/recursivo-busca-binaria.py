# Reimplemente de maneira recursiva o método de busca nas seguintes estruturas de dados vistas no primeiro semestre: Lista por contiguidade (busca binária).

class ListaInt:
    def __init__(self):
        self.lista = []

    def inicializa(self, lista):
        self.lista = lista
        print("Lista inicializada:", self.lista)

    def busca_binaria(self, inicio, valor, fim):
        if inicio > fim:
            return False
        meio = (inicio + fim) // 2
        if self.lista[meio] == valor:
            return meio
        if self.lista[meio] < valor:
            return self.busca_binaria(meio + 1, valor, fim)
        if self.lista[meio] > valor:
            return self.busca_binaria(inicio, valor, meio - 1)
       
        
lista = ListaInt()
lista.inicializa([1, 2, 3, 7, 8, 9, 10])
print(lista.busca_binaria(0, 3, 6))
print(lista.busca_binaria(0, 7, 6))
print(lista.busca_binaria(0, 5, 6))