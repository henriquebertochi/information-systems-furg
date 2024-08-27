from pilha_encadeada import PilhaEncadeada
from pilha_contigua import PilhaContigua

print("Testando Pilha Encadeada:")
pilha_enc = PilhaEncadeada()
pilha_enc.empilhar(1)
pilha_enc.empilhar(2)
pilha_enc.empilhar(3)
print("Topo da pilha encadeada:", pilha_enc.topo())
print("Desempilhando:", pilha_enc.desempilhar())
print("Topo da pilha encadeada após desempilhar:", pilha_enc.topo())
print()

print("Testando Pilha Contígua:")
pilha_cont = PilhaContigua(5)
pilha_cont.empilhar(10)
pilha_cont.empilhar(20)
pilha_cont.empilhar(30)
print("Topo da pilha contígua:", pilha_cont.topo())
print("Desempilhando:", pilha_cont.desempilhar())
print("Topo da pilha contígua após desempilhar:", pilha_cont.topo())
