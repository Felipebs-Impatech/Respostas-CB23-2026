import P06_3549_pilha_encadeada as pilha

class FilaEncadeada:
    def __init__(self):
        self.inicio = pilha.PilhaEncadeada()  
        self.fim = pilha.PilhaEncadeada()
        self.tamanho = 0

    def enfileirar(self, valor):
        self.inicio.push(valor)
        self.tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        if self.fim.topo() is None:
            while self.inicio.len() > 0:
                self.fim.push(self.inicio.pop())
        valor = self.fim.pop()
        self.tamanho -= 1
        return valor

    def frente(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        if self.fim.topo() is None:
            while self.inicio.len() > 0:
                self.fim.push(self.inicio.pop())
        return self.fim.topo()

    def esta_vazia(self):
        return self.tamanho == 0

    def len(self):
        return self.tamanho

    def repr(self):
        if self.esta_vazia():
            return ""

        fim_temp = []
        while self.fim.len() > 0:
            fim_temp.append(self.fim.pop())

        inicio_temp = []
        while self.inicio.len() > 0:
            inicio_temp.append(self.inicio.pop())

        itens = fim_temp + list(reversed(inicio_temp))

        for item in reversed(fim_temp):
            self.fim.push(item)
        for item in reversed(inicio_temp):
            self.inicio.push(item)

        return " <- ".join(str(item) for item in itens)