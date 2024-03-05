import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
        
    def imprime(self):
        if self.ultimaPosicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultimaPosicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        if self.ultimaPosicao == self.capacidade - 1:
            print("Capacidade cheia")
        else:
            self.ultimaPosicao += 1
            self.valores[self.ultimaPosicao] = valor
        
x = VetorNaoOrdenado(5)
x.insere(10)
x.insere(8)
x.insere(11)
x.insere(18)
x.insere(28)
x.insere(48)
x.insere(58)
x.insere(68)
x.imprime()
