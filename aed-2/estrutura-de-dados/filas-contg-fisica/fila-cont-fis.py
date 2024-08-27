class FilaCont:
    def __init__(self, max):
        self.max = max
        self.ini = None
        self.fim = None
        self.vetor = max * [None]
        self.tam = 0
    
    def inserir(self, valor):
        if self.ini == None:
            self.tam += 1
            self.ini = 0
            self.vetor[self.ini] = valor
        elif self.tam < self.max:
            if self.ini <= self.fim and self.fim < self.max - 1:
                self.fim += 1
                self.vetor[self.fim] = valor
                self.tam += 1



var = FilaCont(5)
var.inserir(10)
var.inserir(20)
print(var.vetor)

