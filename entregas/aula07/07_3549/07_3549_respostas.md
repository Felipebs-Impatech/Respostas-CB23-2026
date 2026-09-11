## Discussão

O depth-first search (DFS) é muito útil para resolver labirintos perfeitos de maneira veloz, enquanto o breadth-first search (BFS), apesar do grande consumo de memória, evita problemas de estouro de recursão (stack overflow). Ou seja, o BFS pode ser mais útil quando começamos a lidar com labirintos muito grandes, e também, é mais eficiente em questão de número de passos da solução para labirintos não perfeitos.

Com esses levantamentos, optei por implementar um algoritmo BFS, tanto para comparar os dois algoritmos, quanto para testar sua escalibilidade futuramente.
