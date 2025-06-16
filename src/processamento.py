import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import linkage

def construir_matriz_coocorrencia(df, tecnologias_lista):
    matriz_coocorrencia = pd.DataFrame(0, index=tecnologias_lista, columns=tecnologias_lista)
    
    for tecnologias in df['Tecnologias']:
        tecnologias_validas = [tec for tec in tecnologias if tec in tecnologias_lista]
        for i in range(len(tecnologias_validas)):
            for j in range(i, len(tecnologias_validas)):
                matriz_coocorrencia.loc[tecnologias_validas[i], tecnologias_validas[j]] += 1
                if i != j:
                    matriz_coocorrencia.loc[tecnologias_validas[j], tecnologias_validas[i]] += 1
    return matriz_coocorrencia

def calcular_similaridade_e_distancia(matriz_coocorrencia):
    matriz_coocorrencia_normalizada = matriz_coocorrencia.div(matriz_coocorrencia.sum(axis=1), axis=0).fillna(0)
    matriz_similaridade = cosine_similarity(matriz_coocorrencia_normalizada)
    matriz_distancia = 1 - matriz_similaridade
    assert np.allclose(matriz_distancia, matriz_distancia.T), "A matriz de distância deve ser simétrica."
    return matriz_similaridade, matriz_distancia

def aplicar_clusterizacao(matriz_distancia, n_clusters=5):
    linkage_matrix = linkage(matriz_distancia, method='average')
    return linkage_matrix
