import pandas as pd

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

arquivo_csv = 'netflix_amazon_disney_titles.csv'
elencos, diretores = carregar_dados_padronizados(arquivo_csv)
'''
# Exemplo: mostrar os 3 primeiros pares de elenco e diretor
for i in range(3):
    print(f"Diretores: {diretores[i]}")
    print(f"Elenco: {elencos[i]}")
    print("---")
'''