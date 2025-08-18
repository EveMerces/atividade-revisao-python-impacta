"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
• Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
• Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
• A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere
o programa permitindo que o usuário digite o salário inicial do funcionário."""

# 1: Funcionário contratado em 1995 com R$ 1000
salario = 1000.00
percentual = 1.5

print("=== FUNCIONÁRIO CONTRATADO EM 1995 ===")
print(f"1995: R$ {salario:.2f}")

# 1996 - aumento de 1.5%
salario = salario * (1 + percentual/100)
print(f"1996: R$ {salario:.2f} (aumento de {percentual}%)")

# 1997 em diante - percentual dobra a cada ano
for ano in range(1997, 2026):
    percentual = percentual * 2
    salario = salario * (1 + percentual/100)
    print(f"{ano}: R$ {salario:.2f} (aumento de {percentual}%)")

print(f"\nSalário atual em 2025: R$ {salario:.2f}")

print("\n" + "="*50)

# 2: Usuário digita salário inicial
print("=== VERSÃO COM SALÁRIO DIGITADO PELO USUÁRIO ===")
salario_inicial = float(input("Digite o salário inicial: R$ "))

salario = salario_inicial
percentual = 1.5

print(f"1995: R$ {salario:.2f}")

# 1996 - aumento de 1.5%  
salario = salario * (1 + percentual/100)
print(f"1996: R$ {salario:.2f} (aumento de {percentual}%)")

# 1997 em diante - percentual dobra a cada ano
for ano in range(1997, 2026):
    percentual = percentual * 2  
    salario = salario * (1 + percentual/100)
    print(f"{ano}: R$ {salario:.2f} (aumento de {percentual}%)")

print(f"\nSalário atual em 2025: R$ {salario:.2f}")