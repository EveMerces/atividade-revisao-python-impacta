"""Faça um programa para motoristas do Uber que, ao inserir o CEP do endereço do
destino do passageiro ele retorne qual região de São Paulo aquele CEP é. Utilize a
documentação: https://viacep.com.br/
Exemplo: ao inserir o CEP 02122-050 o resultado deve ser a mensagem: Bairro: Vila Maria
Alta, Zona Norte de São Paulo.
As zonas de São Paulo são: Norte, Sul, Leste, Oeste e Centro (indique também quando o
destino da corrida é pra fora da grande são paulo, em cidades vizinhas). Esse programa
será muito útil em relação à segurança dos motoristas, e com ele eles irão poder escolher
pra qual destino querem ou não aceitar corridas."""

import requests

cep = input("Digite o CEP: ")

# tirar traços do cep
cep = cep.replace("-", "")
cep = cep.replace(".", "")

# consultar o cep na api
url = "https://viacep.com.br/ws/" + cep + "/json/"
response = requests.get(url)
dados = response.json()

if 'erro' in dados:
    print("CEP não encontrado")
else:
    bairro = dados['bairro']
    cidade = dados['localidade']
    
    print(f"Bairro: {bairro}")
    
    # verificar se é são paulo
    if cidade != "São Paulo":
        print(f"Destino fora de São Paulo: {cidade}")
    else:
        # verificar zona pelo bairro
        bairro = bairro.lower()
        
        # zona norte
        if "santana" in bairro or "tucuruvi" in bairro or "vila maria" in bairro or "vila guilherme" in bairro or "cachoeirinha" in bairro or "brasilândia" in bairro or "freguesia" in bairro or "casa verde" in bairro or "limão" in bairro or "jaçanã" in bairro or "tremembé" in bairro or "mandaqui" in bairro:
            print("Zona Norte de São Paulo")
        
        # zona sul
        elif "vila mariana" in bairro or "saúde" in bairro or "cursino" in bairro or "ipiranga" in bairro or "jabaquara" in bairro or "vila prudente" in bairro or "cidade ademar" in bairro or "grajaú" in bairro or "socorro" in bairro or "capão redondo" in bairro or "campo limpo" in bairro or "morumbi" in bairro or "santo amaro" in bairro or "brooklin" in bairro or "itaim bibi" in bairro:
            print("Zona Sul de São Paulo")
        
        # zona leste  
        elif "mooca" in bairro or "brás" in bairro or "belém" in bairro or "tatuapé" in bairro or "vila carrão" in bairro or "penha" in bairro or "cangaíba" in bairro or "vila matilde" in bairro or "são miguel" in bairro or "itaquera" in bairro or "guaianases" in bairro or "cidade tiradentes" in bairro:
            print("Zona Leste de São Paulo")
        
        # zona oeste
        elif "perdizes" in bairro or "pompéia" in bairro or "lapa" in bairro or "jaguaré" in bairro or "butantã" in bairro or "pinheiros" in bairro or "vila madalena" in bairro or "sumaré" in bairro or "jardim paulista" in bairro:
            print("Zona Oeste de São Paulo")
        
        # centro
        elif "sé" in bairro or "república" in bairro or "santa cecília" in bairro or "consolação" in bairro or "bela vista" in bairro or "liberdade" in bairro or "cambuci" in bairro:
            print("Centro de São Paulo")
        
        else:
            print("Zona não identificada - São Paulo")