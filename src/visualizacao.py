import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
import pandas as pd

def plot_dendrogram(linkage_matrix, labels):
    plt.figure(figsize=(12, 10))
    dendrogram(linkage_matrix, labels=labels, orientation='top', leaf_rotation=90, leaf_font_size=12)
    plt.title('Dendrograma de Tecnologias')
    plt.xlabel('Tecnologia')
    plt.ylabel('Distância')
    plt.show()

def plot_heatmap(matriz_coocorrencia):
    plt.figure(figsize=(12, 8))
    sns.heatmap(matriz_coocorrencia, annot=True, cmap='viridis')
    plt.title('Matriz de Co-ocorrência de Tecnologias')
    plt.xlabel('Tecnologia')
    plt.ylabel('Tecnologia')
    plt.show()

def plot_clusters(matriz_similaridade, tecnologias_lista_frequentes, clusters):
    df_similaridade = pd.DataFrame(matriz_similaridade, index=tecnologias_lista_frequentes, columns=tecnologias_lista_frequentes)
    df_similaridade['Cluster'] = clusters

    pca = PCA(n_components=2)
    componentes = pca.fit_transform(df_similaridade.iloc[:, :-1])

    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=componentes[:, 0], y=componentes[:, 1], hue=clusters, palette='viridis', legend='full')
    plt.title('Clusters de Tecnologias com PCA')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.show()

def plot_frequencias_tecnologias(df):
    tecnologias_explodidas = df.explode('Tecnologias')
    frequencias = tecnologias_explodidas['Tecnologias'].value_counts()

    plt.figure(figsize=(10, 8))
    frequencias.head(30).plot(kind='barh')
    plt.xlabel('Frequência')
    plt.ylabel('Tecnologia')
    plt.title('Frequência das Tecnologias nas Vagas de Emprego')
    plt.gca().invert_yaxis()
    plt.show()

def plot_frequencias_posicoes(df):
    posicoes_explodidas = df.explode('Posicao')
    contagem_posicoes = posicoes_explodidas['Posicao'].value_counts()

    plt.figure(figsize=(10, 6))
    contagem_posicoes.plot(kind='barh')
    plt.title('Distribuição de Posições nas Vagas de Emprego')
    plt.xlabel('Frequência')
    plt.ylabel('Posição')
    plt.gca().invert_yaxis()
    plt.show()

def plot_frequencias_regime_trabalho(df):
    regime_trabalho_explodido = df.explode('Regime Trabalho')
    contagem_regime_trabalho = regime_trabalho_explodido['Regime Trabalho'].value_counts()

    plt.figure(figsize=(10, 6))
    contagem_regime_trabalho.plot(kind='barh')
    plt.title('Distribuição de Regimes de Trabalho nas Vagas de Emprego')
    plt.xlabel('Frequência')
    plt.ylabel('Regime de Trabalho')
    plt.gca().invert_yaxis()
    plt.show()
