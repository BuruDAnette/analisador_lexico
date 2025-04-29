# Analisador Léxico - Atividade 1

**Aluna:** Bruna Castro  
**Disciplina:** Compiladores

Este projeto consiste na **etapa de análise léxica** de um compilador/tradutor/interpretador simples, com foco em linguagem natural (português). A aplicação valida os caracteres utilizados, remove *stopwords*, detecta grafias incorretas via similaridade de strings, e organiza palavras relevantes em uma Tabela de Símbolos e Fila de Tokens.

---

## ⚙️ Funcionalidades

1. **Verificação Léxica:**
    - Valida se o texto contém apenas caracteres válidos (A-Z, a-z, 0-9, pontuação e acentuação compatível com o teclado ABNT2).
    - Caracteres inválidos são detectados e geram erro.
    Retorna:
        True se todos os caracteres são válidos
    
    Lança:
        ValueError: Com lista dos caracteres inválidos encontrados

2. **Stopwords:**
    - As palavras irrelevantes à análise (como preposições, artigos etc.) são removidas com base na lista de `stopwords` do `nltk`.

3. **Similaridade de Strings:**
    - Busca por grafias incorretas com margem de erro de até 2 caracteres usando `difflib.SequenceMatcher`. Por padrão, a precisão, com um número entre 0.0 e 1.0 (palavras idênticas), foi 0.8.

4. **Tabela de Símbolos e Fila de Tokens:**
    - Palavras relevantes são armazenadas em uma estrutura de dados:
    - Lista de símbolos (sem repetições)
    - Fila de tokens (com repetição, na ordem de ocorrência)

---

## Fontes e Bibliotecas

- [NLTK Stopwords](https://www.nltk.org)
- Similaridade com [`difflib`](https://docs.python.org/3/library/difflib.html)
- Verificação de caracteres válidos em strings [Stack Overflow](https://stackoverflow.com/questions/89909/how-do-i-verify-that-a-string-only-contains-letters-numbers-underscores-and-da)
- Busca por similaridade de palavras com erros de digitação [Stack Overflow](https://stackoverflow.com/questions/37757512/how-to-match-strings-with-possible-typos)

---

## Como Executar
1. **Ativar e Instalar as Dependências:**
    Clone o repositório e instale as dependências:
    ```bash
        .\.venv\Scripts\activate
        pip install nltk
