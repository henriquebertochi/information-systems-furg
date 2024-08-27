
class Tabela_CTGF:
    def __init__(self, tamanhoMax):
        self.chave = [None] * tamanhoMax
        self.valor = [None] * tamanhoMax
        self.tamanho = 0
        self.max = tamanhoMax

    def vazia(self):
        return self.tamanho == 0
    
    def cheia(self):
        return self.tamanho == self.max
    
    def tamanho(self):
        return self.tamanho
    
    def inserir(self, chave, valor):
        if self.cheia():
            return False
        self.chave[self.tamanho] = chave
        self.valor[self.tamanho] = valor
        self.tamanho += 1
        return True
    
    def inserir_ordenado(self, chave, valor):
        if self.cheia():
            return False
        i = 0
        while i < self.tamanho and self.chave[i] < chave:
            i += 1
        for j in range(self.tamanho, i, -1):
            self.chave[j] = self.chave[j - 1]
            self.valor[j] = self.valor[j - 1]
        self.chave[i] = chave
        self.valor[i] = valor
        self.tamanho += 1
        return True
    
    def buscar(self, chave):
        for i in range(self.tamanho):
            if self.chave[i] == chave:
                return self.valor[i]
        return None
    
    def buscar_binaria(self, chave):
        inicio = 0
        fim = self.tamanho - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.chave[meio] == chave:
                return self.valor[meio]
            if chave < self.chave[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
        return None
    
    def remover(self, chave):
        for i in range(self.tamanho):
            if self.chave[i] == chave:
                self.chave[i] = self.chave[self.tamanho - 1]
                self.valor[i] = self.valor[self.tamanho - 1]
                self.tamanho -= 1
                return True
        return False
    
    def destruir(self):
        self.chave = [None] * len(self.chave)
        self.valor = [None] * len(self.valor)
        self.tamanho = 0

tabela = Tabela_CTGF(10)

print(tabela.vazia())
tabela.inserir(0, 'A')
print(tabela.buscar(0))
print(tabela.buscar(3))
tabela.remover(0)
print(tabela.tamanho)
print(tabela.vazia())
print(tabela.cheia())

tabela.inserir_ordenado(0, 'A')
tabela.inserir_ordenado(1, 'B')
tabela.buscar_binaria(1)
print(tabela.tamanho)

tabela.destruir()
print(tabela.tamanho)