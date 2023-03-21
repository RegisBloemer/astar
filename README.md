Este script define uma classe `Graph` simples para representar um gráfico não direcionado com arestas ponderadas. Ele também implementa o algoritmo de busca A\* para encontrar o caminho mais curto entre dois nós no grafo usando uma heurística de distância de Manhattan. Finalmente, inclui uma função para plotar o gráfico e o caminho encontrado usando a biblioteca `matplotlib`.

O script segue os seguintes passos:

1. Importe os módulos necessários (heapq, defaultdict e matplotlib).
2. Defina a classe `Graph` com métodos para adicionar arestas entre nós com distâncias.
3. Defina a função `manhattan_distance` para calcular a distância de Manhattan entre dois nós.
4. Defina a função `a_star` para encontrar o caminho mais curto em um gráfico usando o algoritmo A\*.
5. Defina a função `plot_graph` para plotar o gráfico e o caminho encontrado usando `matplotlib`.
6. Crie um grafo simples com 4 nós e 4 arestas (formando um quadrado).
7. Execute o algoritmo A\* para encontrar o caminho mais curto entre dois nós no grafo (neste caso, de (0, 0) a (1, 1)).
8. Imprima o caminho encontrado.
9. Plote o gráfico e o caminho encontrado usando a função `plot_graph`.

O script exibirá o gráfico com o caminho mais curto entre os nós inicial e final especificados. O caminho será mostrado em vermelho, enquanto os nós e arestas do gráfico serão exibidos em azul.