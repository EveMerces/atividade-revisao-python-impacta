'''9. Neste exercício, você irá criar um programa que solicita ao usuário a sigla de uma moeda
e exibe a cotação do Real (BRL) em relação a essa moeda. O objetivo é fazer uma
requisição à API de cotações de moedas, tratar a resposta e apresentar o valor do Real
em face da moeda escolhida. Você deve usar essa API: https://api.exchangerate-api.
com/v4/latest/BRL onde BRL é a sigla da moeda alvo (Real).
• Solicite ao usuário que insira a sigla da moeda desejada (por exemplo, “USD” para Dólar
Americano, “EUR” para Euro, “GBP” para Libra Esterlina, etc.).
• Faça uma requisição à API de cotações de moedas para obter a taxa de câmbio do Real
em relação à moeda informada pelo usuário.
• Extraia o valor da cotação do Real em relação à moeda solicitada.
• Exiba uma mensagem clara e informativa, como “O Real vale X [nome da moeda]”, onde
X é o valor da cotação. Ex: O Real vale 5.42 dólares americanos, traduzindo a sigla da
moeda para o nome completo (USD para dólares americanos).'''

import urllib.request
import json

def obter_nome_moeda(sigla):
    nomes_moedas = {
        "USD": "dólares americanos",
        "EUR": "euros",
        "GBP": "libras esterlinas",
        "JPY": "ienes japoneses",
        "AUD": "dólares australianos",
        "CAD": "dólares canadenses",
        "CHF": "francos suíços",
        "CNY": "yuans chineses",
        "INR": "rupias indianas",
        "BRL": "reais"
    }
    return nomes_moedas.get(sigla.upper(), "moeda desconhecida")

def obter_cotacao(sigla_moeda):
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    
    try:
        with urllib.request.urlopen(url) as resposta:
            dados = json.loads(resposta.read())
            if sigla_moeda in dados['rates']:
                return dados['rates'][sigla_moeda]
            else:
                return None
    except Exception as e:
        print(f"Erro ao acessar a API: {e}")
        return None

def main():
    while True:
        sigla_moeda = input("Insira a sigla da moeda desejada (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, INR): ").strip().upper()
        cotacao = obter_cotacao(sigla_moeda)
        
        if cotacao is not None:
            nome_moeda = obter_nome_moeda(sigla_moeda)
            print(f"O Real vale {cotacao:.2f} {nome_moeda}.")
        else:
            print("Sigla da moeda inválida ou não disponível.")

if __name__ == "__main__":
    main()

