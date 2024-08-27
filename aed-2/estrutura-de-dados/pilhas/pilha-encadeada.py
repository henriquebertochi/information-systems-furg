class Nodo:
    def __init__(self, valor):
        self.info = valor
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None

    def Empilhar(self, dado):
        novo = Nodo(dado)
        if (not self.Vazia()):
            novo.prox = self.topo
        self.topo = novo

    def Excluir(self):
        if (not self.Vazia()):
            self.topo = self.topo.prox 

    def Excluir(self):
        if (not self.Vazia()):
            aux = self.topo
            self.topo = aux.prox
            del aux

    def Consultar(self):
        if (not self.Vazia()):
            return self.topo.info
        
    def Destruir(self):
        while (not self.Vazia()):
            self.Excluir()

    def Vazia(self):
        return self.topo == None
    

#corrigir o Nodo linha 6

pilha = Pilha()
pilha.Empilhar(10)
pilha.Empilhar(20)
pilha.Empilhar(30)
print(pilha.Consultar())
pilha.Excluir()
print(pilha.Consultar())
pilha.Destruir()
print(pilha.Vazia())