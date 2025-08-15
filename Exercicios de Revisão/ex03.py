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
