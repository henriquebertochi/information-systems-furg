class PilhaContigua:
    def __init__(self, tamanho_max):
        self.tamanho_max = tamanho_max
        self.items = []
    
    def vazia(self):
        return len(self.items) == 0
    
    def cheia(self):
        return len(self.items) == self.tamanho_max
    
    def empilhar(self, valor):
        if self.cheia():
            raise IndexError("Pilha cheia")
        self.items.append(valor)
    
    def desempilhar(self):
        if self.vazia():
            raise IndexError("Pilha vazia")
        return self.items.pop()
    
    def topo(self):
        if self.vazia():
            raise IndexError("Pilha vazia")
        return self.items[-1]