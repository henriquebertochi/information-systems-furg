class NoLista:
    def __init__(self, valor=0, proximo=None):
        self.info = valor
        self.proximo = proximo

def listas_encadeadas_iguais(lista1, lista2):
    while lista1 is not None and lista2 is not None:
        if lista1.info != lista2.info:
            return False
        lista1 = lista1.proximo
        lista2 = lista2.proximo
    
    return lista1 is None and lista2 is None

lista1 = NoLista(1, NoLista(2, NoLista(3)))
lista2 = NoLista(1, NoLista(2, NoLista(3)))

print(listas_encadeadas_iguais(lista1, lista2))