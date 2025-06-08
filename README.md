# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ

## RESOLUÇÃO DE PROBLEMAS COM GRAFOS

**Professor:** Vinícius Mourão Alves de Souza

---

## Análise de Redes Complexas

### Considerações Iniciais

- Códigos copiados da Internet e/ou de ferramentas de Inteligência Artificial Generativa receberão **nota 0 (zero)**;
- Códigos que utilizem **bibliotecas externas** que fornecem estruturas de grafos ou algoritmos para sua manipulação ou processamento receberão **nota 0 (zero)**;
- Todas as implementações serão avaliadas mediante um **teste de autoria**. Todos os estudantes do grupo devem apresentar o teste;
- A **falta de apresentação ou o desconhecimento** de partes importantes do código apresentado pelo grupo resultará em **nota 0 (zero)** ao estudante;
- A entrega do código-fonte, link com o vídeo da apresentação e relatório deverá ser feita em **um único arquivo zip**;
- **Entregas em atraso serão desconsideradas**.

---

### Visão Geral do Projeto

Neste projeto, você e sua equipe irão:

1. Aplicar o código desenvolvido em uma rede complexa de larga escala para extrair informações de um problema real de plataformas de streaming de vídeo utilizando **grafos** e **algoritmos adequados**;
2. Analisar os resultados obtidos, interpretá-los e discuti-los em um **relatório técnico**.

---

### Formato da Entrega

A entrega deve conter um arquivo `.zip` com:

- O **código-fonte** com as implementações solicitadas;
- **Link do vídeo** de até 15 minutos explicando a lógica e testes;
- Um **relatório em PDF** com as respostas às questões.

---

## Descrição do Problema e dos Dados

Você irá explorar os relacionamentos entre criadores de conteúdo nas plataformas **Netflix**, **Amazon Prime Video** e **Disney+**.

O dataset contém:

- 19.621 filmes e séries;
- 61.811 atores/atrizes;
- 10.870 diretores.

Você deverá construir **dois grafos**:

1. **Grafo direcionado e ponderado**: conexões entre atores/atrizes e diretores.
2. **Grafo não-direcionado e ponderado**: conexões entre atores/atrizes que atuaram juntos em uma mesma obra.

**Pesos das arestas**: número de colaborações (filmes/séries).

> Importante: Padronize os nomes em **letras maiúsculas**, sem espaços no início/fim. Ignore entradas com `cast` ou `director` vazios.

---

## Atividades de Implementação (6 pontos)

### 1. Construção dos Grafos (1 ponto)

- Utilizar **lista de adjacências**.
- Retornar número de vértices e arestas de cada grafo.

### 2. Componentes Conexas (1 ponto)

- Para o **grafo direcionado**: quantidade de **componentes fortemente conexas**;
- Para o **grafo não-direcionado**: quantidade de **componentes conexas**.

### 3. Árvore Geradora Mínima (1 ponto)

- Receber um vértice `X` e retornar a **árvore geradora mínima** da componente de `X` no grafo não-direcionado;
- Informar o **custo total da árvore**.

### 4. Centralidade de Grau (1 ponto)

- Calcular a **degree centrality** (grafo direcionado e não-direcionado).

### 5. Centralidade de Intermediação (1 ponto)

- Calcular a **betweenness centrality**.

### 6. Centralidade de Proximidade (1 ponto)

- Calcular a **closeness centrality**.

---

## Relatório com Análise das Redes (4 pontos)

### 1. Distribuição de graus (0.5 ponto)

- Para ambos os grafos.
- A distribuição segue um padrão de redes complexas?

### 2. Componentes (0.5 ponto)

- Quantas componentes conexas (não-direcionado) e fortemente conexas (direcionado)?
- Qual a **distribuição da ordem** dessas componentes?

### 3. Centralidade de Grau - Direcionado (0.5 ponto)

- Top 10 diretores com maior grau.
- Interpretar essa métrica no contexto.

### 4. Centralidade de Intermediação - Direcionado (0.5 ponto)

- Top 10 diretores mais influentes.
- Interpretar essa métrica.

### 5. Centralidade de Proximidade - Direcionado (0.5 ponto)

- Top 10 diretores mais influentes.
- Interpretar essa métrica.

### 6. Centralidade de Grau - Não-Direcionado (0.5 ponto)

- Top 10 atores/atrizes mais influentes.

### 7. Centralidade de Intermediação - Não-Direcionado (0.5 ponto)

- Top 10 atores/atrizes mais influentes.

### 8. Centralidade de Proximidade - Não-Direcionado (0.5 ponto)

- Top 10 atores/atrizes mais influentes.

---
