import requests

pais = input("Digite um país: ").lower()
url = f"https://restcountries.com/v3.1/name/{pais}"

resp = requests.get(url)

if resp.status_code == 200:
    obj = resp.json()

    nome = obj[0]['name']['common']
    lingua = obj[0].get('languages', 'Não disponível')
    regiao = obj[0]['region']
    subregiao = obj[0]['subregion']
    capital = obj[0].get('capital', ['Não disponível'])[0]
    fronteira = obj[0].get('borders', ['Nenhuma fronteira'])

    moeda = obj[0].get('currencies', {})
    if moeda:
        sigla_moeda = list(moeda.keys())[0]
        nome_moeda = moeda[sigla_moeda]['name']
        simbolo_moeda = moeda[sigla_moeda].get('symbol', 'Não disponível')
    else:
        sigla_moeda = 'Não disponível'
        nome_moeda = 'Não disponível'
        simbolo_moeda = 'Não disponível'

    print(f"Nome do País: {nome}")
    print(f"Línguas: {', '.join(lingua.values()) if isinstance(lingua, dict) else lingua}")
    print(f"Região: {regiao}")
    print(f"Subregião: {subregiao}")
    print(f"Capital: {capital}")
    print(f"Fronteiras: {', '.join(fronteira)}")
    print(f"Sigla da Moeda: {sigla_moeda}")
    print(f"Nome da Moeda: {nome_moeda}")
    print(f"Símbolo da Moeda: {simbolo_moeda}")

else:
    print(f"Erro ao chamar API: {resp.status_code}")
    print(resp.text)
