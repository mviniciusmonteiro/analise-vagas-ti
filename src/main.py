import pandas as pd
from extrator import criar_pattern, extrair_informacoes, sinonimos, sinonimos_posicao
from processamento import construir_matriz_coocorrencia, calcular_similaridade_e_distancia, aplicar_clusterizacao
from visualizacao import (plot_dendrogram, plot_heatmap, plot_clusters,
                          plot_frequencias_tecnologias, plot_frequencias_posicoes, plot_frequencias_regime_trabalho)
import re
from sklearn.cluster import AgglomerativeClustering

# Lista de tecnologias para extração
tecnologias_lista = [
    "HTML", "CSS", "JavaScript", "Python", "SQL", "TypeScript", "Bash/Shell", "Java",
    "C#", "C++", "PHP", "PowerShell", "Rust", "Kotlin", "Lua", "Dart",
    "Assembly", "Swift", "Visual Basic", "MATLAB", "VBA", "Groovy",
    "Scala", "Perl", "GDScript", "Objective-C", "Elixir", "Haskell", "Delphi",
    "MicroPython", "Lisp", "Clojure", "Julia", "Zig", "Fortran", "Solidity", "Ada",
    "Erlang", "F#", "Apex", "Prolog", "OCaml", "Cobol", "Crystal", "Nim", "Zephyr",
    "Node.js", "React", "jQuery", "Next.js", "Express", "Angular", "ASP.NET CORE",
    "Vue.js", "ASP.NET", "Flask", "API REST", "Spring Boot", "Django", "WordPress",
    "FastAPI", "Laravel", "AngularJS", "Svelte", "NestJS", "Blazor", "Ruby on Rails",
]

def main():
    # Criar padrão regex para tecnologias
    escaped_tec_list = [re.escape(tec) for tec in tecnologias_lista]
    tecnologias_pattern = r'\b(' + '|'.join(escaped_tec_list) + r')\b'

    # Criar padrões para sinônimos
    sinonimos_patterns = criar_pattern(sinonimos)

    # Carregar dados
    file_path = "../data/dados_atuais.xlsx"
    df = pd.read_excel(file_path)

    df['Descricao'] = df['Descricao'].fillna('')
    df['Titulo da vaga'] = df['Titulo da vaga'].fillna('')

    # Extrair informações
    df['Tecnologias'], df['Posicao'], df['Regime Trabalho'] = zip(*df.apply(
        lambda x: extrair_informacoes(x['Titulo da vaga'], x['Descricao'], sinonimos_patterns, tecnologias_pattern, sinonimos_posicao),
        axis=1))

    # Salvar resultado
    output_path = "../data/TDadosExtraidos.xlsx"
    df.to_excel(output_path, index=False)
    print(f"Arquivo salvo em: {output_path}")

    # Visualização frequências
    plot_frequencias_tecnologias(df)

    # Filtrar tecnologias frequentes
    tecnologias_explodidas = df.explode('Tecnologias')
    frequencias = tecnologias_explodidas['Tecnologias'].value_counts()
    tecnologias_frequentes = frequencias[frequencias > 4].index.tolist()

    tecnologias_lista_frequentes = [tec for tec in tecnologias_lista if tec in tecnologias_frequentes]

    # Matriz co-ocorrência
    matriz_coocorrencia = construir_matriz_coocorrencia(df, tecnologias_lista_frequentes)

    # Similaridade e distância
    matriz_similaridade, matriz_distancia = calcular_similaridade_e_distancia(matriz_coocorrencia)

    # Dendrograma
    linkage_matrix = aplicar_clusterizacao(matriz_distancia)
    plot_dendrogram(linkage_matrix, tecnologias_lista_frequentes)
    plot_heatmap(matriz_coocorrencia)

    # Clusterização final
    n_clusters = 5
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, linkage='average')
    clusters = clustering_model.fit_predict(matriz_distancia)

    plot_clusters(matriz_similaridade, tecnologias_lista_frequentes, clusters)

    # Visualizar posições e regimes
    plot_frequencias_posicoes(df)
    plot_frequencias_regime_trabalho(df)

if __name__ == "__main__":
    main()
