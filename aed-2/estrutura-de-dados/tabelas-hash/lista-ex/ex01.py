'''
1) Considerando a estrutura de um registro {chave: inteiro, nome: string}, uma distribuição média de 7 registros, uma função de dispersão h(chave) = chave mod tamanho(tabela) + 1, tratamento de colisão opening adressing com pesquisa linear e encadeamento, apresente a tabela hash resultante da inserção elementos abaixo na ordem apresentada.
{73, João}
{15, Carlos}
{44, Marcia}
{37, Ronaldo}
{30, Michel}
{59, Darci}
{61, Joana}
{99, Denise}
'''

class Registro:
    def __init__(self, chave, nome):
        self.chave = chave
        self.nome = nome

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
        return (chave % self.tamanhoMax) + 1

    def inserir(self, chave, nome):
        registro = Registro(chave, nome)
        hashIndex = self.hash_func(chave)
        original_index = hashIndex
        
        while self.tabela[hashIndex] is not None:
            hashIndex = (hashIndex + 1) % self.tamanhoMax
            if hashIndex == original_index:
                print("Tabela cheia!")
                return False

        self.tabela[hashIndex] = registro
        return True

    def exibir(self):
        for i, registro in enumerate(self.tabela):
            if registro is not None:
                print(f"Posição {i}: ({registro.chave}, {registro.nome})")
            else:
                print(f"Posição {i}: Vazia")

# Exemplo com os registros
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
