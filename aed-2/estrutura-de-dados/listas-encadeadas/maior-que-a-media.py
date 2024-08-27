class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def adicionar(self, dado):
        novo_no = No(dado)
        if not self.primeiro:
            self.primeiro = novo_no
            return
        ultimo_no = self.primeiro
        while ultimo_no.proximo:
            ultimo_no = ultimo_no.proximo
        ultimo_no.proximo = novo_no

    def calcular_media(self):
        if not self.primeiro:
            return 0

        # Calcular a média dos valores na lista
        atual = self.primeiro
        soma_total = 0
        contador_nos = 0

        while atual:
            soma_total += atual.dado
            contador_nos += 1
            atual = atual.proximo

        if contador_nos == 0:
            return 0

        media = soma_total / contador_nos
        return media

    def imprimir_valores_acima_da_media(self):
        media = self.calcular_media()

        if media == 0:
            print("Lista vazia")
            return

        # Passo 2: Percorrer a lista e imprimir valores maiores que a média
        atual = self.primeiro
        posicao = 0

        while atual:
            if atual.dado > media:
                print(f"Posição {posicao}, Valor {atual.dado}")
            posicao += 1
            atual = atual.proximo


# Exemplo de uso:
# Criando uma lista encadeada e adicionando elementos
lista = ListaEncadeada()
lista.adicionar(3)
lista.adicionar(5)
lista.adicionar(2)
lista.adicionar(7)
lista.adicionar(1)

# Chamada do método para imprimir valores acima da média:
lista.imprimir_valores_acima_da_media()
