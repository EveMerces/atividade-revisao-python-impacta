'''1. Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a 
valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas
disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo
de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes
na máquina.
• Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
• Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma
nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

print("Informe o valor a ser sacado no caixa")
dinheiro=float(input("Valor: "))
if dinheiro < 10 or dinheiro > 600:
        print("Não é possível")
    
else:
    nota_100 = dinheiro//100
    dinheiro = dinheiro % 100
    nota_50 = dinheiro//50
    dinheiro = dinheiro % 50
    nota_10 = dinheiro//10
    dinheiro = dinheiro % 10
    nota_5 = dinheiro//5
    dinheiro = dinheiro % 5
    nota_1 = dinheiro//1
    dinheiro = dinheiro % 1

print(f"Notas de R$100: {nota_100}")
print(f"Notas de R$50: {nota_50}")
print(f"Notas de R$10: {nota_10}")
print(f"Notas de R$5: {nota_5}")
print(f"Notas de R$1: {nota_1}")