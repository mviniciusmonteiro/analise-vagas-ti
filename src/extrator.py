import re
from src.utils import padronizar_terminos, padronizar_posicao

def extrair_informacoes(titulo, descricao, sinonimos_patterns, sinonimos_posicao, tecnologias_pattern):
    texto_completo = f"{titulo} {descricao}"
    texto_padronizado = padronizar_terminos(texto_completo, sinonimos_patterns)

    tecnologias = re.findall(tecnologias_pattern, texto_padronizado, re.IGNORECASE)
    tecnologias = list(set(tecnologias))
    
    posicoes = padronizar_posicao([texto_completo], sinonimos_posicao)
    regime_trabalho = re.findall(r'\b(remote|remoto|presencial|híbrido|hibrido)\b', texto_padronizado, re.IGNORECASE)
    
    return tecnologias, posicoes, regime_trabalho
