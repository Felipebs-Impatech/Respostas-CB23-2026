import 06_3549_pilha_encadeada as pilha

class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enfileirar(self, valor):
        novo_no = pilha.No(valor)
        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        self.tamanho += 1

    def desenfileirar(self):
        if self.inicio is None:
            raise IndexError("A fila está vazia")
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return valor

    def esta_vazia(self):
        return self.tamanho == 0

    def len(self):
        return self.tamanho

    def repr(self):
        itens = []
        atual = self.inicio
        while atual is not None:
            itens.append(str(atual.valor))
            atual = atual.proximo
        return " <- ".join(itens)