# Este projeto vai ser uma introducao a Processamento de linguagem natural (PLN) de uma forma bem simples. Voce vai criar um programa que recebe uma frase ou um pequeno texto e tenta determinar se o sentimento expresso é positivo, negativo ou neutro.

# Oque voce vai aprender: Manipulacao de strings e listas, logica condicional, funcoes, listas de palavras, contadores, entrada e saida de dados.

# Funcionalidades:Entrada de texto, lexicos de sentimento, analise de sentimento, determinacao do sentimento, exibicao do resultado.
import re


def analisar_sentimento(texto):
    # Definindo listas de palavras positivas e negativas
    palavras_positivas = [
        "bom",
        "ótimo",
        "excelente",
        "feliz",
        "alegre",
        "amor",
        "gostei",
    ]
    palavras_negativas = [
        "ruim",
        "péssimo",
        "horrível",
        "triste",
        "decepcionado",
        "ódio",
        "não gostei",
    ]

    # Normalizando o texto
    texto = texto.lower()
    texto = re.sub(r"[^\w\s]", "", texto)  # Remove pontuação

    # Contadores de sentimentos
    positivo = sum(1 for palavra in texto.split() if palavra in palavras_positivas)
    negativo = sum(1 for palavra in texto.split() if palavra in palavras_negativas)

    # Determinando o sentimento
    if positivo > negativo:
        return "Sentimento positivo"
    elif negativo > positivo:
        return "Sentimento negativo"
    else:
        return "Sentimento neutro"


# Função principal para entrada e saída
def main():
    texto = input("Digite uma frase ou texto para analisar o sentimento: ")
    resultado = analisar_sentimento(texto)
    print(f"Resultado da análise: {resultado}")


if __name__ == "__main__":
    main()
# Este é um exemplo simples de análise de sentimento. Você pode expandir as listas de palavras e melhorar a lógica conforme necessário.
# Você também pode considerar o uso de bibliotecas de PLN mais avançadas, como NLTK ou spaCy, para análises mais complexas.
# Lembre-se de testar o programa com diferentes entradas para verificar a precisão da análise de sentimento.
# Você pode adicionar mais palavras às listas de sentimentos ou até mesmo usar dicionários de sentimentos mais completos.
# Boa sorte com o seu projeto de análise de sentimento! Divirta-se aprendendo e programando!
