'''
3) Adaptar a implementação do TAD Tabela realizada anteriormente criando uma nova função de pesquisa baseada na função hash resto da divisão. Utilize tratamento de colisão separate chaining baseado em listas encadeadas.
'''

class Nodo:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class TabelaHash:
    def __init__(self, tamanhoMedio):
        self.tamanhoMax = self.proximo_primo(int(tamanhoMedio + tamanhoMedio / 2))
        self.tabela = [None] * self.tamanhoMax  # Lista de nós (encadeamento)

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
        return chave % self.tamanhoMax  # Resto da divisão

    def inserir(self, chave, valor):
        indice = self.hash_func(chave)
        novo_nodo = Nodo(chave, valor)

        # Caso a lista no índice esteja vazia, simplesmente insere o nó
        if self.tabela[indice] is None:
            self.tabela[indice] = novo_nodo
        else:
            # Colisão: percorre a lista encadeada até o fim e insere o novo nó
            atual = self.tabela[indice]
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def buscar(self, chave):
        indice = self.hash_func(chave)
        atual = self.tabela[indice]

        # Percorre a lista no índice para encontrar a chave
        while atual is not None:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo

        return None  # Chave não encontrada

    def remover(self, chave):
        indice = self.hash_func(chave)
        atual = self.tabela[indice]
        anterior = None

        while atual is not None:
            if atual.chave == chave:
                if anterior is None:
                    # O primeiro elemento da lista é o que deve ser removido
                    self.tabela[indice] = atual.proximo
                else:
                    # Remove o elemento ajustando o ponteiro do anterior
                    anterior.proximo = atual.proximo
                return True  # Chave removida
            anterior = atual
            atual = atual.proximo

        return False  # Chave não encontrada

    def exibir(self):
        for i in range(self.tamanhoMax):
            atual = self.tabela[i]
            print(f"Índice {i}: ", end="")
            while atual is not None:
                print(f"({atual.chave}, {atual.valor}) -> ", end="")
                atual = atual.proximo
            print("None")

# Exemplo de uso da TabelaHash com separate chaining
tabela_hash = TabelaHash(7)

tabela_hash.inserir(73, "João")
tabela_hash.inserir(15, "Carlos")
tabela_hash.inserir(44, "Marcia")
tabela_hash.inserir(37, "Ronaldo")
tabela_hash.inserir(30, "Michel")
tabela_hash.inserir(59, "Darci")
tabela_hash.inserir(61, "Joana")
tabela_hash.inserir(99, "Denise")

tabela_hash.exibir()

# Testando a função de busca
print(tabela_hash.buscar(59))  # Deve retornar Darci
print(tabela_hash.buscar(12))  # Deve retornar None (não encontrado)

# Testando a função de remoção
tabela_hash.remover(59)
tabela_hash.exibir()
