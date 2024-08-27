from nodo import Nodo

class Fila:
    def __init__(self):
        self.ini = None
        self.fim = None

    def Inserir(self, valor):
        elem = Nodo(valor)
        if self.ini == None and self.fim == None:
            self.ini = elem
        else:
            self.fim.prox = elem
        self.fim = elem

    def Consultar(self):
        if self.ini != None:
            return self.ini.info
        else:
            return None
    
    def Remover(self): # Fila só remove do INICIO
        if self.ini != None:
            self.ini = self.ini.prox
            if self.ini == None:
                self.fim = None

    def Vazia(self):
        return self.ini == None
    
    def Printar(self):
        aux = self.ini
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.prox
        print('')