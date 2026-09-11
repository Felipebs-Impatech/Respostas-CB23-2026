## Respostas Aula 6
#### Análise de complexidade da pilha

- push():
Troca o "head" pelo valor adicionado na chamada da função e adiciona um ponteiro à esse nó. Não depende do número de elementos da pilha, portanto tem complexidade constante $O(1)$
- pop():
Remove o item do topo da pilha e atribui o título de "head" ao próximo na pilha. Também não depende do tamanho da pilha, ou seja, tem complexidade constante $O(1)$
- topo()
Retorna o nó com o título de "head", ou seja, o elemento que está no topo da pilha. Também tem complexidade constante por não depender do tamanho da pilha: $O(1)$
- esta_vazia():
Verifica se a pilha está vazia olhando seu atributo "self.len", assim como as funções anteriores, nã depende do tamanho da pilha (ou está vazia ou não, não precisamos contar os elementos). Portanto tem complexidade constante $O(1)$
- len():
Retorna o valor do atributo "self.length", que é salvo a cada alteração da pilha, ou seja, continuamos sem ter que contar quantos elementos tem na pilha pois esse valor já está salvo. Complexidade constante $O(1)$
- repr():
Essa função percorre toda a pilha para retornar todos os seus elementos, ou seja, realiza a ação $n$ vezes, onde $n$ é o tamanho da pilha. Portanto, temos complexidade linear $O(n)$

#### Análise da complexidade da fila

- enfileirar():
Salvamos em uma pilha auxiliar "inicio" o elemento que queremos adicionar. Não depende do tamanho da pilha, portanto $O(1)$
- desenfileirar():
Semelhante à função "enfileirar()", mas caso a pilha auxiliar "fim" esteja vazia, colocamos todos os elementos da pilha "inicio" nesta, e retornamos (excluindo o elemento da fila) o elemento do começo da fila, com o padrão first in, first out. Como é um algoritmo amortecido, pois pode depender do tamanho da fila ou não, varia, dependendo do uso entre $O(n)$ e $O(1)$
- frente():
Segue o mesmo padrão de algoritmo amortecido, se a pilha "fim" estiver vazia, temos uma complexidade $O(n)$, mas se já estiver com elementos, complexidade constante $O(1)$
- len():
Igualmente à função "len()" das pilhas, salvamos o comprimento da fila em um atributo e apenas retornamos o seu valor, portanto tem complexidade constante $O(1)$
- repr():
Novamente bastante parecido com a função respectiva da pilha, percorremos todos os elementos da fila a fim de impirmí-los. Porque realizamos essa ação $n$ vezes, onde $n$ representa o comprimento da fila, temos uma complexidade linear $O(n)$