class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def prefixEsq(self):
        print(self.dado)
        if self.esquerda:
            self.esquerda.prefixEsq()
        if self.direita:
            self.direita.prefixEsq()

    def prefixDir(self):
        print(self.dado)
        if self.direita:
            self.direita.prefixDir()
        if self.esquerda:
            self.esquerda.prefixDir()

    def infixEsq(self):
        if self.esquerda:
            self.esquerda.infixEsq()
        print(self.dado)
        if self.direita:
            self.direita.infixEsq()

    def infixDir(self):
        if self.direita:
            self.direita.infixDir()
        print(self.dado)
        if self.esquerda:
            self.esquerda.infixDir()

    def printtree(self, lado, caminhamento):
        if lado == "esquerda" and caminhamento == "pre":
            self.prefixEsq()
        elif lado == "direita" and caminhamento == "pre":
            self.prefixDir()
        elif lado == "esquerda" and caminhamento == "in":
            self.infixEsq()
        elif lado == "direita" and caminhamento == "in":
            self.infixDir()

    def localiza(self, valor):
        if self != None:
            if self.dado == valor:
                return self
            if self.esquerda:
                aux = self.esquerda.localiza(valor)
                if aux:
                    return aux
            if self.direita:
                aux = self.direita.localiza(valor)
                if aux:
                    return aux

    def localizaPai(self, valor):
        if self is not None:
            if self.esquerda and self.esquerda.dado == valor:
                return self
            if self.direita and self.direita.dado == valor:
                return self
            if self.esquerda:
                aux = self.esquerda.localizaPai(valor)
                if aux:
                    return aux
            if self.direita:
                aux = self.direita.localizaPai(valor)
                if aux:
                    return aux
        else:
            return None

    def inserir(self, pai, filho, lado):
        aux = self.localiza(pai)
        if lado == "esquerda":
            if aux.esquerda == None:
                aux.esquerda = Nodo(filho)
                print("Inserido")
            else:
                print("Já possui filho a esquerda")
        elif lado == "direita":
            if aux.direita == None:
                aux.direita = Nodo(filho)
                print("Inserido")
            else:
                print("Já possui filho a direita")

    def Folha(self):
        return self.esquerda == None and self.direita == None

    def excluirFolha(self, valor):
        pai = self.localizaPai(valor)
        if pai != None:
            if pai.esquerda and pai.esquerda.dado == valor:
                if pai.esquerda.Folha():
                    pai.esquerda = None
                    print("Excluído")
                else:
                    print("Não é folha")
            elif pai.direita and pai.direita.dado == valor:
                if pai.direita.Folha():
                    pai.direita = None
                    print("Excluído")
                else:
                    print("Não é folha")
            else:
                print("Nó não encontrado")
        else:
            print("Nó não encontrado")

t = Nodo("A")
t.esquerda = Nodo("B")
t.direita = Nodo("C")
t.esquerda.direita = Nodo("D")
t.printtree("esquerda", "in")

aux = t.localiza("E")
if aux:
    print(aux.dado)
else:
    print("Não encontrado")

t.inserir("D", "E", "esquerda")

aux = t.localizaPai("E")
if aux:
    print(aux.dado)
else:
    print("Não encontrado")

t.excluirFolha("E")