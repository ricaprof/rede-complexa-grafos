def componentes_conexas(grafo):
    visitado = set()
    componentes = []

    for v in grafo.vertices:
        if v not in visitado:
            pilha = [v]
            componente = []

            while pilha:
                atual = pilha.pop()
                if atual not in visitado:
                    visitado.add(atual)
                    componente.append(atual)
                    for vizinho, _ in grafo.lista_adj[atual]:
                        if vizinho not in visitado:
                            pilha.append(vizinho)

            componentes.append(componente)

    return componentes


def componentes_fortemente_conexas(grafo):
    def dfs(v, visitado, pilha):
        visitado.add(v)
        for viz, _ in grafo.lista_adj[v]:
            if viz not in visitado:
                dfs(viz, visitado, pilha)
        pilha.append(v)

    def dfs_transposto(v, visitado, componente, transposto):
        visitado.add(v)
        componente.append(v)
        for viz, _ in transposto.get(v, []):
            if viz not in visitado:
                dfs_transposto(viz, visitado, componente, transposto)

    # 1ª passagem: ordem de finalização
    visitado = set()
    pilha = []
    for v in grafo.vertices:
        if v not in visitado:
            dfs(v, visitado, pilha)

    # 2ª passagem: grafo transposto
    transposto = {}
    for u in grafo.lista_adj:
        for v, peso in grafo.lista_adj[u]:
            transposto.setdefault(v, []).append((u, peso))

    # DFS no transposto
    visitado.clear()
    componentes = []
    while pilha:
        v = pilha.pop()
        if v not in visitado:
            componente = []
            dfs_transposto(v, visitado, componente, transposto)
            componentes.append(componente)

    return componentes


import heapq

def agm_prim(grafo, inicio):
    visitado = set()
    agm = []
    custo_total = 0
    fila = []

    visitado.add(inicio)
    for viz, peso in grafo.lista_adj[inicio]:
        heapq.heappush(fila, (peso, inicio, viz))

    while fila:
        peso, u, v = heapq.heappop(fila)
        if v not in visitado:
            visitado.add(v)
            agm.append((u, v, peso))
            custo_total += peso
            for viz, p in grafo.lista_adj[v]:
                if viz not in visitado:
                    heapq.heappush(fila, (p, v, viz))

    return agm, custo_total


def degree_centrality(grafo):
    centralidade = {}
    for v in grafo.vertices:
        centralidade[v] = len(grafo.lista_adj[v])
    return centralidade


from collections import deque, defaultdict

def betweenness_centrality(grafo):
    centralidade = defaultdict(float)

    for s in grafo.vertices:
        S = []
        P = defaultdict(list)
        sigma = dict.fromkeys(grafo.vertices, 0)
        d = dict.fromkeys(grafo.vertices, -1)
        sigma[s], d[s] = 1, 0
        Q = deque([s])

        while Q:
            v = Q.popleft()
            S.append(v)
            for w, _ in grafo.lista_adj[v]:
                if d[w] < 0:
                    Q.append(w)
                    d[w] = d[v] + 1
                if d[w] == d[v] + 1:
                    sigma[w] += sigma[v]
                    P[w].append(v)

        delta = dict.fromkeys(grafo.vertices, 0)
        while S:
            w = S.pop()
            for v in P[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
            if w != s:
                centralidade[w] += delta[w]

    for v in centralidade:
        centralidade[v] /= 2

    return dict(centralidade)


def closeness_centrality(grafo):
    centralidade = {}
    for v in grafo.vertices:
        dist = {v: 0}
        fila = deque([v])
        while fila:
            u = fila.popleft()
            for w, _ in grafo.lista_adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    fila.append(w)
        if len(dist) > 1:
            centralidade[v] = (len(dist) - 1) / sum(dist.values())
        else:
            centralidade[v] = 0
    return centralidade
