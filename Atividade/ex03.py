"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero e
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for
D ou E."""


def chamarNota (msg):
    while True:
     nota = float(input(msg))
     if 0.0<= nota <=10.0:
         return nota
     else:
         print("Nota invalida")

nota1 = chamarNota("Nota 1: ")
nota2 = chamarNota("Nota 2: ")

media = (nota1 + nota2) / 2

if media > 10.0:
    print("nota invalida")
elif 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"


print(f"Média: {media:.2f} Conceito: {conceito}")

if conceito in ["A","B","C"]:
    print("Aprovado")
else:
    print("Reprovado")
