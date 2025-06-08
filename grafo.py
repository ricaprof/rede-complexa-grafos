import pandas as pd
from collections import defaultdict

def carregar_dados_padronizados(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)

    # Remove entradas onde 'cast' ou 'director' estejam vazios ou nulos
    df = df[df['cast'].notnull() & df['director'].notnull()]

    total_linhas = len(df)
    linhas_processadas = 0

    elencos = []
    diretores = []

    for _, linha in df.iterrows():
        elenco_raw = linha['cast']
        diretor_raw = linha['director']

        # Padronizar nomes do elenco
        atores = [ator.strip().upper() for ator in elenco_raw.split(',') if ator.strip()]
        if len(atores) < 2:
            continue  # Ignora se não há ao menos dois atores para formar arestas

        # Padronizar nomes dos diretores (pode haver múltiplos separados por vírgula)
        diretores_padronizados = [d.strip().upper() for d in diretor_raw.split(',') if d.strip()]
        if not diretores_padronizados:
            continue  # Ignora se não houver diretores válidos

        elencos.append(atores)
        diretores.append(diretores_padronizados)
        linhas_processadas += 1

    # Verificação
    if linhas_processadas == total_linhas:
        print(f" Todas as {linhas_processadas} linhas válidas foram processadas.")
    else:
        print(f" Foram processadas {linhas_processadas} de {total_linhas} linhas (entradas inválidas foram ignoradas).")

    return elencos, diretores

class Grafo:
    def __init__(self, direcionado=False):
        self.lista_adj = defaultdict(list)
        self.vertices = set()
        self.direcionado = direcionado
        self.num_arestas = 0
    
    def adicionar_vertice(self, v):
        """Adiciona um vértice ao grafo."""
        self.vertices.add(v)
    
    def adicionar_aresta(self, u, v, peso=1):
        """Adiciona uma aresta entre u e v com o peso especificado."""
        # Verifica se os vértices já existem
        self.vertices.add(u)
        self.vertices.add(v)
        
        # Verifica se a aresta já existe e atualiza o peso se for o caso
        for i, (vizinho, peso_atual) in enumerate(self.lista_adj[u]):
            if vizinho == v:
                self.lista_adj[u][i] = (vizinho, peso_atual + peso)
                if not self.direcionado:
                    for j, (vizinho2, peso_atual2) in enumerate(self.lista_adj[v]):
                        if vizinho2 == u:
                            self.lista_adj[v][j] = (vizinho2, peso_atual2 + peso)
                            return
                return
        
        # Se a aresta não existir, adiciona
        self.lista_adj[u].append((v, peso))
        self.num_arestas += 1
        
        # Se for não direcionado, adiciona a aresta em ambas direções
        if not self.direcionado:
            # Verifica se a aresta já existe no sentido oposto
            aresta_existe = False
            for i, (vizinho, peso_atual) in enumerate(self.lista_adj[v]):
                if vizinho == u:
                    aresta_existe = True
                    break
            
            if not aresta_existe:
                self.lista_adj[v].append((u, peso))
    
    def obter_info(self):
        """Retorna o número de vértices e arestas do grafo."""
        num_vertices = len(self.vertices)
        return num_vertices, self.num_arestas if self.direcionado else self.num_arestas // 2
    
    def __str__(self):
        """Representação em string do grafo."""
        saida = f"Grafo {'direcionado' if self.direcionado else 'não direcionado'}\n"
        saida += f"Vértices: {len(self.vertices)}, Arestas: {self.num_arestas if self.direcionado else self.num_arestas // 2}\n"
        
        for vertice in sorted(self.vertices):
            saida += f"{vertice}: "
            vizinhos = [f"{v}({p})" for v, p in self.lista_adj[vertice]]
            saida += ", ".join(vizinhos) + "\n"
        
        return saida


def construir_grafo_atores(elencos):
    """
    Constrói um grafo não direcionado onde os vértices são atores e as arestas
    representam atores que atuaram juntos. O peso da aresta é o número de vezes
    que eles atuaram juntos.
    
    Args:
        elencos: Lista de listas, onde cada lista interna contém os atores de um filme/série
        
    Returns:
        Grafo não direcionado dos atores
    """
    grafo_atores = Grafo(direcionado=False)
    
    # Para cada filme/série
    for elenco in elencos:
        # Para cada par de atores no elenco
        for i in range(len(elenco)):
            for j in range(i+1, len(elenco)):
                ator1 = elenco[i]
                ator2 = elenco[j]
                grafo_atores.adicionar_aresta(ator1, ator2, 1)
    
    return grafo_atores


def construir_grafo_direcional(elencos, diretores):
    """
    Constrói um grafo direcionado onde cada aresta vai de um ator para um diretor.
    O peso da aresta é o número de filmes em que o ator trabalhou com esse diretor.
    
    Args:
        elencos: Lista de listas, onde cada lista interna contém os atores de um filme
        diretores: Lista de listas, onde cada lista interna contém os diretores do filme correspondente
        
    Returns:
        Grafo direcionado dos atores para diretores
    """
    grafo_direcionado = Grafo(direcionado=True)
    
    # Percorre cada filme/série e seus respectivos elencos e diretores
    for i in range(len(elencos)):
        elenco = elencos[i]
        diretores_filme = diretores[i]
        
        # Para cada ator, adiciona uma aresta para cada diretor
        for ator in elenco:
            for diretor in diretores_filme:
                grafo_direcionado.adicionar_aresta(ator, diretor, 1)
    
    return grafo_direcionado