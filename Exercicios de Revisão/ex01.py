"""1. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
• até 20 litros: desconto de 3% por litro
• acima de 20 litros: desconto de 5% por litro
Gasolina:
• até 20 litros: desconto de 4% por litro
• acima de 20 litros: desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado
da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""

combustivel = input("Digite 'a' para álcool e 'g' para gasolina:")
if combustivel == "a" or combustivel == "A":
  alcool = float(input("Quantos litros de álcool você quer abastecer?: "))
  if alcool > 20:
    valor_pago = alcool * 1.90 * 0.95
  else:
    valor_pago = alcool * 1.90 * 0.97
  print(f"O valor a ser pago é de R${valor_pago:.2f} ")
elif combustivel == "g" or combustivel == "G":
  gasolina = float(input("Quantos litros de gasolina você quer abastecer?: "))
  if gasolina > 20:
    valor_pago = gasolina * 2.50 * 0.94
  else:
    valor_pago = gasolina * 2.50 * 0.96
  print(f"O valor a ser pago é de R${valor_pago:.2f} ")