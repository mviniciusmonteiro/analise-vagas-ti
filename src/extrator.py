import re

# Definir mapeamento de sinônimos e variantes
sinonimos = {
     ".NET": [".NET", ".NET Framework", ".NET Core", ".NET MAUI", ".NET 5", ".NET 6", ".net"],
    "API REST": ["API REST", "REST API", "RESTful API"],
    "JavaScript": ["JavaScript"],
    "TypeScript": ["TypeScript"],
    "Java": ["Java", "J2EE"],
    "C#": ["C#", "C Sharp"],
    "Python": ["python", "Py"],
    "SQL": ["SQL", "Structured Query Language"],
    "HTML": ["HTML", "HyperText Markup Language", "HTML5"],
    "CSS": ["CSS", "Cascading Style Sheets", "CSS3"],
    "React": ["React", "React.js"],
    "Angular": ["Angular", "AngularJS", "Angular 2+", "AngularJS"],
    "Vue.js": ["Vue.js", "Vue"],
    "Node.js": ["Node.js", "Node"],
    "Django": ["Django", "Django REST Framework"],
    "Flask": ["Flask", "Flask RESTful"],
    "Laravel": ["Laravel", "Laravel PHP"],
    "Spring Boot": ["Spring Boot", "Spring", "Springboot"],
    "WordPress": ["WordPress", "WP"],
    "Swift": ["Swift", "SwiftUI"],
    "Flutter": ["Flutter", "Flutter SDK"],
    "TensorFlow": ["TensorFlow", "TF"],
    "PyTorch": ["PyTorch", "Torch"],
    "Keras": ["Keras", "Keras Deep Learning"],
    "NumPy": ["NumPy", "Numerical Python"],
    "Pandas": ["Pandas", "pandas"],
    "Docker": ["Docker", "Docker Container"],
    "Kubernetes": ["Kubernetes", "K8s"],
    "AWS": ["AWS", "Amazon Web Services"],
    "Azure": ["Azure", "Microsoft Azure"],
    "Google Cloud": ["Google Cloud", "Google Cloud Platform", "GCP"],
    "Firebase": ["Firebase", "Firebase Realtime Database"],
    "MongoDB": ["MongoDB", "Mongo"],
    "PostgreSQL": ["PostgreSQL", "Postgres"],
    "MySQL": ["MySQL", "My SQL"],
    "SQLite": ["SQLite", "SQLite3"],
    "Redis": ["Redis", "Redis DB"],
    "Oracle": ["Oracle", "Oracle Database"],
    "Elasticsearch": ["Elasticsearch", "ES"],
    "Supabase": ["Supabase", "Supabase DB"],
    "GraphQL": ["GraphQL", "GraphQL API"],
    "PHP": ["PHP", "Hypertext Preprocessor"],
    "Rust": ["Rust", "Rustlang"],
    "Ruby": ["Ruby", "Ruby Programming Language"],
    "MATLAB": ["MATLAB", "MATLAB Language"],
    "VBA": ["VBA", "Visual Basic for Applications"],
    "Groovy": ["Groovy", "Groovy Language"],
    "Scala": ["Scala", "Scala Programming Language"],
    "Perl": ["Perl", "Perl Programming Language"],
    "Haskell": ["Haskell", "Haskell Language"],
    "Elixir": ["Elixir", "Elixir Language"],
    "Erlang": ["Erlang", "Erlang Language"],
    "F#": ["F#", "F Sharp"],
    "Apex": ["Apex", "Salesforce Apex"],
    "Prolog": ["Prolog", "Prolog Language"],
    "OCaml": ["OCaml", "Objective Caml"],
    "Cobol": ["Cobol", "COBOL"],
    "Crystal": ["Crystal", "Crystal Programming Language"],
    "Nim": ["Nim", "Nim Programming Language"],
    "Zig": ["Zig", "Zig Programming Language"],
    "Fortran": ["Fortran", "Fortran Language"],
    "Solidity": ["Solidity", "Solidity Language"],
    "Ada": ["Ada", "Ada Language"],
    "Clojure": ["Clojure", "Clojure Language"],
    "Lisp": ["Lisp", "Lisp Language"],
    "Julia": ["Julia", "Julia Language"],
    "Zig": ["Zig", "Zig Programming Language"],
    "Flutter": ["Flutter", "Flutter SDK"],
    "Apache Kafka": ["Apache Kafka", "Kafka"],
    "Apache Spark": ["Apache Spark", "Spark"],
    "Hadoop": ["Hadoop", "Hadoop Framework"],
    "ElasticSearch": ["ElasticSearch", "Elastic Search", "ES"],
    "Hugging Face Transformers": ["Hugging Face Transformers", "Hugging Face"],
    "OpenCV": ["OpenCV", "Open Source Computer Vision Library"],
    "Electron": ["Electron", "Electron.js"],
    "Ionic": ["Ionic", "Ionic Framework"],
    "Capacitor": ["Capacitor", "Capacitor Framework"],
    "Tauri": ["Tauri", "Tauri Framework"],
    "Xamarin": ["Xamarin", "Xamarin.Forms"],
    "Unity": ["Unity", "Unity3D"],
    "Unreal Engine": ["Unreal Engine", "UE4", "UE5"],
}

sinonimos_posicao = {
    "Junior": [ "junior", "júnior"],
    "Pleno": ["pleno"],
    "Senior": ["senior", "sênior", "sr"],
    "Lider": ["líder", "coordenador"],
    "Especialista": ["especialista"],
    "Engenheiro": ["engenheiro"],
    "Estagiario": ["estagiario", "estagiário", "estágio"]
}
def criar_pattern(sinonimos):
    sinonimos_patterns = []
    for chave, variantes in sinonimos.items():
        pattern = r'\b(' + '|'.join(re.escape(variacao) for variacao in variantes) + r')\b'
        sinonimos_patterns.append((pattern, chave))
    return sinonimos_patterns

def padronizar_terminos(texto, sinonimos_patterns):
    texto = texto.lower()
    for pattern, chave in sinonimos_patterns:
        texto = re.sub(pattern, chave, texto, flags=re.IGNORECASE)
    return texto

def padronizar_posicao(posicoes, sinonimos_posicao):
    posicoes_unificadas = []
    for posicao in posicoes:
        for padronizado, sinonimos in sinonimos_posicao.items():
            if any(sinonimo in posicao.lower() for sinonimo in sinonimos):
                posicoes_unificadas.append(padronizado)
                break
    return list(set(posicoes_unificadas))  # Remove duplicatas

def extrair_informacoes(titulo, descricao, sinonimos_patterns, tecnologias_pattern, sinonimos_posicao):
    texto_completo = f"{titulo} {descricao}"
    texto_padronizado = padronizar_terminos(texto_completo, sinonimos_patterns)

    tecnologias = re.findall(tecnologias_pattern, texto_padronizado, re.IGNORECASE)
    tecnologias = list(set(tecnologias))

    posicoes = padronizar_posicao([texto_completo], sinonimos_posicao)
    regime_trabalho = re.findall(r'\b(remote|remoto|presencial|híbrido|hibrido)\b', texto_padronizado, re.IGNORECASE)

    return tecnologias, posicoes, regime_trabalho
