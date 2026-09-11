import P06_3549_pilha_encadeada as pilha
import P06_3549_fila_encadeada as fila

if __name__ == "__main__":
    # Teste da pilha
    pilha_encadeada = pilha.PilhaEncadeada()
    pilha_encadeada.push(5)
    pilha_encadeada.push([1, 2, 3])
    pilha_encadeada.push("Bom dia")
    
    print("Pilha:")
    print(pilha_encadeada.repr())
    print("Topo da pilha:", pilha_encadeada.topo())
    print("Tamanho da pilha:", pilha_encadeada.len())
    
    ultimo = pilha_encadeada.pop()
    print("Elemento removido da pilha:", ultimo)
    print("Topo da pilha após remoção:", pilha_encadeada.topo())
    print("Tamanho da pilha após remoção:", pilha_encadeada.len())
    
    # Teste da fila
    fila_encadeada = fila.FilaEncadeada()
    fila_encadeada.enfileirar(123)
    fila_encadeada.enfileirar("arroz")
    fila_encadeada.enfileirar(5*2)
    
    print("\nFila:")
    print(fila_encadeada.repr())
    print("Tamanho da fila:", fila_encadeada.len())
    
    primeiro = fila_encadeada.frente()
    print("Elemento na frente da fila:", primeiro)
    removido = fila_encadeada.desenfileirar()
    print("Elemento removido da fila:", removido)
    print("Tamanho da fila após remoção:", fila_encadeada.len())
    print("Fila após remoção:", fila_encadeada.repr())