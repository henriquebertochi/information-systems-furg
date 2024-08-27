class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.topo_no = None
    
    def vazia(self):
        return self.topo_no is None
    
    def empilhar(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.topo_no
        self.topo_no = novo_no
    
    def desempilhar(self):
        if self.vazia():
            raise IndexError("Pilha vazia")
        valor = self.topo_no.valor
        self.topo_no = self.topo_no.proximo
        return valor
    
    def topo(self):
        if self.vazia():
            raise IndexError("Pilha vazia")
        return self.topo_no.valor