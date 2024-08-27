from nodo import Nodo

class Pilha:
    def __init__(self):
        self.topo = None

    def Empilhar(self, dado):
        novo = Nodo(dado)
        if (not self.Vazia()):
            novo.prox = self.topo
        self.topo = novo

    def Desempilhar(self):
        if (not self.Vazia()):
            aux = self.topo
            self.topo = aux.prox
            return aux.info

    def Consultar(self):
        if (not self.Vazia()):
            return self.topo.info
        
    def Destruir(self):
        while (not self.Vazia()):
            self.Excluir()

    def Vazia(self):
        return self.topo == None
    
    def Printar(self):
        aux = self.topo
        while (aux != None):
            print(aux.info, end=' ')
            aux = aux.prox
        print('')