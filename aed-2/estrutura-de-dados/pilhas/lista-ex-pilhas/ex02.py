from pilha_encadeada import PilhaEncadeada
from pilha_contigua import PilhaContigua

def pilhas_iguais(pilha1, pilha2):
    if len(pilha1.items) != len(pilha2.items):
        return False
    
    for item1, item2 in zip(pilha1.items, pilha2.items):
        if item1 != item2:
            return False
    
    return True

def pilhas_iguais_encadeadas(pilha1, pilha2):
    no1 = pilha1.topo_no
    no2 = pilha2.topo_no
    
    while no1 and no2:
        if no1.valor != no2.valor:
            return False
        no1 = no1.proximo
        no2 = no2.proximo
    
    return no1 is None and no2 is None

pilha_enc1 = PilhaEncadeada()
pilha_enc1.empilhar(1)
pilha_enc1.empilhar(2)
pilha_enc1.empilhar(3)

pilha_enc2 = PilhaEncadeada()
pilha_enc2.empilhar(1)
pilha_enc2.empilhar(2)
pilha_enc2.empilhar(3)

print("Pilhas encadeadas são iguais?", pilhas_iguais_encadeadas(pilha_enc1, pilha_enc2))

pilha_cont1 = PilhaContigua(5)
pilha_cont1.empilhar(90)
pilha_cont1.empilhar(60)
pilha_cont1.empilhar(40)

pilha_cont2 = PilhaContigua(5)
pilha_cont2.empilhar(10)
pilha_cont2.empilhar(20)
pilha_cont2.empilhar(30)

print("Pilhas contíguas são iguais?", pilhas_iguais(pilha_cont1, pilha_cont2))
