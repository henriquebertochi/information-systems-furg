class TabelaHash:
    def __init__(self, tamanhoMax):
        self.tamanhoMax = tamanhoMax
        self.tabela = [[] for _ in range(tamanhoMax)]

    # Função de hash simples
    def hash_func(self, chave):
        return chave % self.tamanhoMax

    def inserir(self, chave, valor):
        hashIndex = self.hash_func(chave)
        # Atualiza o valor se a chave já existir
        for i, (chave_existente, _) in enumerate(self.tabela[hashIndex]):
            if chave_existente == chave:
                self.tabela[hashIndex][i] = (chave, valor)
                return
        # Se não existir, adiciona a nova chave/valor
        self.tabela[hashIndex].append((chave, valor))

    def buscar(self, chave):
        hashIndex = self.hash_func(chave)
        for chave_existente, valor in self.tabela[hashIndex]:
            if chave_existente == chave:
                return valor
        return None

    def remover(self, chave):
        hashIndex = self.hash_func(chave)
        for i, (chave_existente, _) in enumerate(self.tabela[hashIndex]):
            if chave_existente == chave:
                del self.tabela[hashIndex][i]
                return True
        return False

    def destruir(self):
        self.tabela = [[] for _ in range(self.tamanhoMax)]

# Exemplo de uso:
tabela_hash = TabelaHash(10)

print(tabela_hash.buscar(0))  # None, porque ainda está vazia
tabela_hash.inserir(10, 'A')
tabela_hash.inserir(20, 'B')
print(tabela_hash.buscar(10))  # 'A'
print(tabela_hash.buscar(20))  # 'B'

tabela_hash.remover(10)
print(tabela_hash.buscar(10))  # None, porque foi removido

tabela_hash.destruir()
print(tabela_hash.buscar(20))  # None, porque a tabela foi destruída
