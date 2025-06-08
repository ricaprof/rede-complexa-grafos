from grafo import carregar_dados_padronizados, construir_grafo_atores, construir_grafo_direcional, Grafo
import os

def mostrar_menu():
    print("\n===== ANÁLISE DE REDES COMPLEXAS =====")
    print("1. Informações básicas dos grafos")
    print("0. Sair")
    print("======================================")
    return input("Escolha uma opção: ")

def main():
    # Verifica se o arquivo CSV existe
    arquivo_csv = 'netflix_amazon_disney_titles.csv'
    if not os.path.exists(arquivo_csv):
        print(f"ERRO: O arquivo {arquivo_csv} não foi encontrado.")
        print(f"Certifique-se de que o arquivo está no diretório: {os.getcwd()}")
        return
    
    print("Carregando dados do arquivo CSV... (isso pode levar alguns minutos)")
    elencos, diretores = carregar_dados_padronizados(arquivo_csv)
    
    print("Construindo grafos... (isso pode levar alguns minutos)")
    grafo_atores = construir_grafo_atores(elencos)
    grafo_direcional = construir_grafo_direcional(elencos, diretores)
    
    print("Grafos construídos com sucesso!")
    opcao = ""
    while opcao != "0":
        opcao = mostrar_menu()
        
        if opcao == "1":
            # Informações básicas dos grafos
            num_vertices_atores, num_arestas_atores = grafo_atores.obter_info()
            print("\nGrafo não-direcionado (atores):")
            print(f"- Número de vértices: {num_vertices_atores}")
            print(f"- Número de arestas: {num_arestas_atores}")
            
            num_vertices_dir, num_arestas_dir = grafo_direcional.obter_info()
            print("\nGrafo direcionado (atores -> diretores):")
            print(f"- Número de vértices: {num_vertices_dir}")
            print(f"- Número de arestas: {num_arestas_dir}")
        
        elif opcao == "0":
            print("Saindo do programa...")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

        if opcao != "0":
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
