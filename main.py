from grafo import carregar_dados_padronizados, construir_grafo_atores, construir_grafo_direcional, Grafo
from algoritmos import (
    componentes_conexas,
    componentes_fortemente_conexas,
    agm_prim,
    degree_centrality,
    betweenness_centrality,
    closeness_centrality
)
import os

def mostrar_menu():
    print("\n===== ANÁLISE DE REDES COMPLEXAS =====")
    print("1. Informações básicas dos grafos")
    print("2. Componentes conexas")
    print("3. Árvore geradora mínima (grafo atores)")
    print("4. Centralidade de grau")
    print("5. Centralidade de intermediação")
    print("6. Centralidade de proximidade")
    print("0. Sair")
    print("======================================")
    return input("Escolha uma opção: ")

def main():
    arquivo_csv = 'netflix_amazon_disney_titles.csv'
    if not os.path.exists(arquivo_csv):
        print(f"ERRO: O arquivo {arquivo_csv} não foi encontrado.")
        return
    
    print("Carregando dados...")
    elencos, diretores = carregar_dados_padronizados(arquivo_csv)
    
    print("Construindo grafos...")
    grafo_atores = construir_grafo_atores(elencos)
    grafo_direcional = construir_grafo_direcional(elencos, diretores)
    
    print("Grafos prontos!")

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            print("\n--- INFORMAÇÕES BÁSICAS ---")
            v1, a1 = grafo_atores.obter_info()
            print(f"Grafo Atores (não direcionado): {v1} vértices, {a1} arestas")
            v2, a2 = grafo_direcional.obter_info()
            print(f"Grafo Direcional (atores → diretores): {v2} vértices, {a2} arestas")

        elif opcao == "2":
            print("\n--- COMPONENTES CONEXAS ---")
            comp_nao_dir = componentes_conexas(grafo_atores)
            print(f"Grafo de atores: {len(comp_nao_dir)} componentes conexas")
            comp_dir = componentes_fortemente_conexas(grafo_direcional)
            print(f"Grafo direcional: {len(comp_dir)} componentes fortemente conexas")

        elif opcao == "3":
            print("\n--- ÁRVORE GERADORA MÍNIMA ---")
            raiz = input("Informe um vértice de partida: ").strip().upper()
            if raiz not in grafo_atores.vertices:
                print("Vértice não encontrado!")
            else:
                agm, custo = agm_prim(grafo_atores, raiz)
                print(f"Árvore geradora mínima com raiz {raiz}:")
                for u, v, p in agm:
                    print(f"{u} --({p})-- {v}")
                print(f"Custo total: {custo}")

        elif opcao == "4":
            print("\n--- CENTRALIDADE DE GRAU ---")
            graus_atores = degree_centrality(grafo_atores)
            graus_direcional = degree_centrality(grafo_direcional)
            print(f"Top 5 graus (grafo atores):")
            for v, g in sorted(graus_atores.items(), key=lambda x: -x[1])[:5]:
                print(f"{v}: {g}")
            print(f"\nTop 5 graus (grafo direcionado):")
            for v, g in sorted(graus_direcional.items(), key=lambda x: -x[1])[:5]:
                print(f"{v}: {g}")

        elif opcao == "5":
            print("\n--- CENTRALIDADE DE INTERMEDIAÇÃO ---")
            centralidade = betweenness_centrality(grafo_atores)
            print("Top 5 vértices por intermediação:")
            for v, c in sorted(centralidade.items(), key=lambda x: -x[1])[:5]:
                print(f"{v}: {c:.4f}")

        elif opcao == "6":
            print("\n--- CENTRALIDADE DE PROXIMIDADE ---")
            centralidade = closeness_centrality(grafo_atores)
            print("Top 5 vértices por proximidade:")
            for v, c in sorted(centralidade.items(), key=lambda x: -x[1])[:5]:
                print(f"{v}: {c:.4f}")

        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
