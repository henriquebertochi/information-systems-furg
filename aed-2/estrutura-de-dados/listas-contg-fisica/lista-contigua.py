class ListaContigua:
    def __init__(self):
        self.lista = []
    
    def inicializa(self):
        self.lista = []
        print("Lista inicializada:", self.lista)
    
    def inserir(self, posicao, elemento):
        if posicao <= len(self.lista) + 1:
            self.lista.insert(posicao - 1, elemento)
            print(f"Inserido {elemento} na posição {posicao}:", self.lista)
        else:
            print(f"Erro: posição {posicao} inválida para inserção.")
    
    def remover(self, posicao):
        if posicao <= len(self.lista):
            elemento_removido = self.lista.pop(posicao - 1)
            print(f"Removido elemento da posição {posicao}: {elemento_removido}. Lista atual:", self.lista)
        else:
            print(f"Erro: posição {posicao} inválida para remoção.")
    
    def localizar(self, elemento):
        posicao = None
        for i in range(len(self.lista)):
            if self.lista[i] == elemento:
                posicao = i + 1
                break
        
        if posicao is not None:
            print(f"Posição de {elemento} na lista:", posicao)
        else:
            print(f"{elemento} não encontrado na lista.")
    
    def limpar(self):
        self.lista = []
        print("Lista limpa:", self.lista)

lista = ListaContigua()

lista.inicializa()
lista.inserir(1, "Carro")
lista.inserir(2, "Moto")
lista.inserir(2, "Bicicleta")
lista.remover(3)
lista.inserir(10, "Caminhão")
lista.inserir(1, lista.lista[1])
lista.inserir(1, lista.lista[1])
lista.limpar()