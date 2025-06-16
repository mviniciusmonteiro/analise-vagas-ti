# Análise de Vagas TI 

Este projeto realiza a **extração e análise de tecnologias mencionadas em vagas de emprego da área de TI**. O objetivo é identificar quais habilidades técnicas (linguagens, frameworks, ferramentas) são mais requisitadas no mercado, além de agrupar tecnologias relacionadas por similaridade.

## 🔍 Objetivos

- Extrair e padronizar tecnologias mencionadas em títulos e descrições de vagas.
- Unificar sinônimos e variações linguísticas.
- Identificar os níveis de experiência mais requisitados (júnior, pleno, sênior).
- Detectar padrões de co-ocorrência entre tecnologias.
- Aplicar clusterização hierárquica para agrupar tecnologias similares.
- Visualizar resultados com gráficos, dendrogramas e mapas de calor.

## 🌐 Origem dos Dados

Os dados foram coletados a partir de **vagas publicadas no LinkedIn**, utilizando a ferramenta de **web scraping Octoparse**. Essa coleta envolveu extração automatizada de:

- Títulos das vagas  
- Descrições completas  
- Informações sobre regime de trabalho  

As informações foram exportadas em um arquivo `.xlsx` para posterior processamento e análise.


