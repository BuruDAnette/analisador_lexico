import re
import nltk
from nltk.corpus import stopwords
from difflib import SequenceMatcher
from collections import deque

# stopwords 
nltk.download('stopwords')
stopwords_pt = set(stopwords.words('portuguese'))

VERDE = "\033[1;32m"
VERMELHO = "\033[1;31m"
RESET = "\033[0m"

# Funcionalidade 1 - Verificação Léxica
def verificar_string(texto):
    pattern = r'[\w\sÀ-ÿ\-.!?,;:]+$'
    caracteres_invalidos = set()

    for char in texto:
        if not re.match(pattern, char):
            # identifica caracteres invisíveis
            if ord(char) < 32 or ord(char) == 127:
                char_repr = f"[ASCII:{ord(char)}]"
            else:
                char_repr = char
            caracteres_invalidos.add(char_repr)

    if caracteres_invalidos:
        chars_list = ', '.join(f"'{c}'" for c in sorted(caracteres_invalidos))
        plural = 's' if len(caracteres_invalidos) > 1 else ''
        raise ValueError(f"Erro léxico - Caractere{plural} inválido{plural} encontrado{plural}: {chars_list}.")
    
    return True

# Funcionalidade 2 - Remoção de Stopwords
def remover_stopwords(lista_de_tokens):
    return [[palavra for palavra in frase if palavra.lower() not in stopwords_pt] 
            for frase in lista_de_tokens]

# Funcionalidade 3 - Busca Fuzzy de Palavras
def busca_fuzzy(palavra_chave, texto, precisao=0.8):
    linhas = texto.split("\n")
    for i, linha in enumerate(linhas):
        palavras = linha.split()
        for palavra in palavras:
            similaridade = SequenceMatcher(None, palavra.lower(), palavra_chave.lower()).ratio()
            if similaridade >= precisao:
                return (f"Palavra similar encontrada: '{palavra}' (linha {i+1}) "
                        f"corresponde à busca '{palavra_chave}' ({VERDE}similaridade: {similaridade:.1%}{RESET})")
    
    return f"{VERMELHO}Nenhuma correspondência semelhante encontrada.{RESET}"

# Funcionalidade 4 - Tabela de Símbolos e Fila de Tokens
def gerar_tabela_simbolos(tokens):
    tabela_simbolos = list(set(token for frase in tokens for token in frase))
    fila_tokens = deque(token for frase in tokens for token in frase)
    return tabela_simbolos, fila_tokens

# programa principal (para o Usuário)
def main():
    print("\nAnalisador Léxico!")

    while True:
        print("\nEscolha uma funcionalidade para testar:")
        print("1 - Verificação Léxica")
        print("2 - Remoção de stopwords")
        print("3 - Busca fuzzy de palavras")
        print("4 - Gerar tabela de símbolos e fila de tokens")
        print("0 - Sair")

        escolha = input("\nDigite o número da opção desejada: ")

        if escolha == "1":
            texto = input("\nDigite o texto para verificar: ")
            try:
                if verificar_string(texto):
                    print(VERDE + "Texto válido: todos os caracteres permitidos!" + RESET)
            except ValueError as e:
                print(VERMELHO + f"{e}" + RESET)

        elif escolha == "2":
            texto = input("\nDigite frases separadas por ponto final: ")
            frases = [frase.strip().split() for frase in texto.split('.') if frase]
            tokens_sem_stopwords = remover_stopwords(frases)
            print(VERDE + "Resultado sem stopwords:" + RESET, tokens_sem_stopwords)

        elif escolha == "3":
            texto = input("\nDigite um texto (pode ter várias linhas): ")
            palavra_chave = input("Digite a palavra para buscar fuzzy: ")
            precisao = input("Digite a precisão mínima (0.0 a 1.0) [padrão: 0.8]: ")

            try:
                precisao = float(precisao) if precisao else 0.8
                print(busca_fuzzy(palavra_chave, texto, precisao))
            except ValueError:
                print(VERMELHO + "Precisão inválida. Tente novamente!" + RESET)

        elif escolha == "4":
            texto = input("\nDigite frases separadas por ponto final: ")
            frases = [frase.strip().split() for frase in texto.split('.') if frase]
            tabela, fila = gerar_tabela_simbolos(frases)
            print(VERDE + "\nTabela de Símbolos:" + RESET, tabela)
            print(VERDE + "Fila de Tokens:" + RESET, list(fila))

        elif escolha == "0":
            print(VERDE + "\nEncerrando o Analisador Léxico.\n"
                    "Até mais!" + RESET)
            break

        else:
            print(VERMELHO + "Opção inválida. Tente novamente." + RESET)

if __name__ == "__main__":
    main()
