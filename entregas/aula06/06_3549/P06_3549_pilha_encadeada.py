class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def __repr__(self):
        return str(self.valor)


class PilhaEncadeada:
    def __init__(self):
        self.length = 0
        self.head = None

    def esta_vazia(self):
        return self.length == 0

    def push(self, item):
        novo_no = No(item)
        novo_no.proximo = self.head
        self.head = novo_no
        self.length += 1

    def pop(self):
        if self.esta_vazia():
            raise ValueError("Lista vazia")

        valor = self.head.valor
        self.head = self.head.proximo
        self.length -= 1
        return valor

    def topo(self):
        if self.esta_vazia():
            return None
        return self.head.valor

    def len(self):
        return self.length

    def repr(self):
        atual = self.head
        itens = []

        while atual is not None:
            itens.append(str(atual.valor))
            atual = atual.proximo

        return " -> ".join(itens)