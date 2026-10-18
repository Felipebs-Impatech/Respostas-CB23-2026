# Relatório — <seu nome> (<sua matrícula>)

<!--Relatório do projeto, preenchido na sua branch. Cada marco acrescenta a sua seção. Responda com as suas palavras e com
os números da sua execução; cada resposta cabe em até 6 linhas, além das tabelas.-->

## Marco 1

### Ambiente

- Saída de "which python":
```bash
/home/al.felipe.santor/venvs/prog2-venv/bin/python`
```
- Etapa 0 do marco1.py:
```bash 
=== Etapa 0: ambiente ===
Python 3.13.15 | NumPy 2.5.4 | fornecido 2.0
```

<!-- Cole aqui a saída de `which python` e da Etapa 0 do `python marco1.py`. -->

### R1 — Expressões regulares

- Exemplo que "re.match" aceita e "re.fullmatch" não aceita:
`AB123 coisa`

Isso implica que a função "valida_tag" irá apenas aceitar tags que cumprirem com os requisitos e não se extenderem para além do tamanho requisitado.

<!-- Uma string que re.match aceita e re.fullmatch rejeita com o padrão de tag; consequência para valida_tag. -->

### R2 — Linhas inválidas

"ler_log" deve devolver as linhas descartadas pois é uma boa prática mostrar ao usuário a razão do erro, ou ao menos, o que resultou em erro. Por exemplo, se uma tag for lançada de maneira incorreta, e não soubermos qual tag foi, precisariamos analisar todas as tags e fazer uma verificação manual em cada uma para poder corrigir o erro.
<!-- Por que ler_log devolve as linhas descartadas; uma situação real em que descartar em silêncio esconderia um problema. -->

### R3 — Late binding

"errados["PT102"](4095)" tenta converter as contagens em kPa, porém, devido ao Late Binding, este guarda uma função lambda c: c * k, com $k = 0.1$, ao invés de $k = 600/4095$, pois k recebe o valor 0.1 em sua última atribuição de "escalas". Já em "criar_conversores", consertamos esse erro ao criar uma variável auxiliar e determinar o valor do parâmetro da função lambda igual à essa variável (como default value), ao invés de passar essa variável diretamente como parâmetro, lambda c, f=fator: c * f [...], assim evitando o Late Binding. 
<!-- Por que errados["PT102"](4095) dá 409,5 e por que a sua criar_conversores não tem o problema. -->

### R4 — Escala nominal

<!-- Hipótese para a diferença da Etapa 2(f) e onde, no código da base, está a explicação. -->

### R5 — Previsão × medição (Etapa 3)

Previsões registradas no commit: <!-- cole o hash curto do commit de previsões -->

| Grandeza | Previsão | Medido |
| --- | --- | --- |
| Memória da lista / memória do `uint16` | | |
| Tempo do laço / tempo vetorizado | | |
| Tempo da compreensão / tempo do laço | | |

<!-- Explique a maior diferença entre previsão e medição; por que uint16 * 20 dá 16364; que dtype você escolheria para contagens e para kPa. -->

### R6 — Tipos da SerieTemporal (Etapa 4d)

| Expressão | Tipo previsto | Tipo observado |
| --- | --- | --- |
| `s + s` | | |
| `s[1:]` | | |
| `s * 2` | | |
| `s.sum()` | | |
| `s[0]` | | |

<!-- Explique o resultado que mais surpreendeu você. -->

### R7 — Issue #4

<!-- Sintoma; o teste de regressão (nome); a causa, em termos da soma acumulada; a correção; por que os testes de aceitação não pegaram o defeito; mais um caso que eles não cobrem e qual teste seu o cobre. -->
