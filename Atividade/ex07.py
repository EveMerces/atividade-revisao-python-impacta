"""Faça um programa que leia um número indeterminado de valores numéricos, encerrando
a entrada de dados quando for informado um valor igual a −1 (que não deve ser
armazenado). Após esta entrada de dados, faça:
• Mostre a quantidade de valores que foram lidos;
• Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
• Exiba todos os valores na ordem inversa à que foram informados, um ao lado do outro;
• Calcule e mostre a soma dos valores;
• Calcule e mostre a média dos valores;
• Calcule e mostre a quantidade de valores acima da média calculada"""

valores = []

while True:
    numero = float(input("Digite um número (-1 para parar): "))
    if numero == -1:
        break
    valores.append(numero)

quantidade = len(valores)
print(f"Quantidade de valores: {quantidade}")

print("Valores na ordem informada:")
for i in range(len(valores)):
    print(valores[i], end=" ")
print()

print("Valores na ordem inversa:")
for i in range(len(valores)-1, -1, -1):
    print(valores[i], end=" ")
print()

soma = 0
for numero in valores:
    soma = soma + numero
print(f"Soma dos valores: {soma}")

media = soma / quantidade
print(f"Média dos valores: {media}")

acima_media = 0
for numero in valores:
    if numero > media:
        acima_media = acima_media + 1
print(f"Valores acima da média: {acima_media}")