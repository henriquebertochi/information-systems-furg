class Pilha:
    def __init__(self, tamanho):
        self.vetor = [None] * tamanho
        self.lim = tamanho - 1
        self.base = 0
        self.topo = self.base - 1

    def Empilha(self, dado):
        if (self.topo < self.lim):
            self.topo += 1
            self.vetor[self.topo] = dado

    def Excluir(self):
        if (self.topo >= self.base):
            self.topo -= 1

    def Consulta(self):
        if self.topo >= self.base:
            return self.vetor[self.topo]

    def Destruir(self):
        self.topo = self.base - 1

    def Vazia(self):
        return self.topo < self.base
    
    def Cheia(self):
        return self.topo == self.lim
    
pilha = Pilha(3)
pilha.Empilha(10)
pilha.Empilha(20)
pilha.Empilha(30)
print(pilha.Consulta())
pilha.Excluir()
print(pilha.Consulta())
pilha.Destruir()
print(pilha.Vazia())