'''
Ponto extra - Hashing
Considerando o TAD tabela hash com função hash resto da divisão, tratamento de colisão opening adressing com pesquisa linear e encadeamento, implementa a operação de exclusão. 
Dica: percorrer todos os encadeamentos e sobrescrever valores do fim para o início.
'''

class Nodo:
    def __init__(self, chave, valor, proximo=None):
        self.chave = chave
        self.valor = valor
        self.proximo = proximo

class TabelaHash:
    def __init__(self, tamanhoMedio):
        self.tamanhoMax = self.proximo_primo(int(tamanhoMedio + tamanhoMedio / 2))
        self.tabela = [None] * self.tamanhoMax
        
    def proximo_primo(self, n):
        def eh_primo(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        while not eh_primo(n):
            n += 1
        return n

    def hash_func(self, chave):
        return chave % self.tamanhoMax

    def inserir(self, chave, valor):
        indice = self.hash_func(chave)
        novo_nodo = Nodo(chave, valor)
        
        if self.tabela[indice] is None:
            self.tabela[indice] = novo_nodo
        else:
            atual = self.tabela[indice]
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def buscar(self, chave):
        indice = self.hash_func(chave)
        atual = self.tabela[indice]
        
        while atual is not None:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        return None

    def remover(self, chave):
        indice = self.hash_func(chave)
        atual = self.tabela[indice]
        anterior = None
        
        while atual is not None:
            if atual.chave == chave:
                if anterior is None:
                    self.tabela[indice] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

hash_table = TabelaHash(10)

hash_table.inserir(10, "valor1")
hash_table.inserir(20, "valor2")
hash_table.inserir(30, "valor3")

print(hash_table.buscar(10))
print(hash_table.buscar(30))

hash_table.remover(20)
print(hash_table.buscar(20))