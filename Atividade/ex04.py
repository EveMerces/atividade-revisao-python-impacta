'''Desenvolver um programa para verificar a nota dos alunos em uma prova com 10
questões. O programa deve seguir os seguintes passos:
• Perguntar ao aluno a resposta de cada uma das 10 questões.
• Comparar as respostas fornecidas pelo aluno com o gabarito da prova.
• Calcular o total de acertos, atribuindo 1 ponto para cada resposta correta.
• Após cada aluno utilizar o sistema, perguntar se outro aluno deseja fazer a prova.
Após todos os alunos terem respondido, o programa deve informar:
• O maior e o menor número de acertos entre os alunos.
• O total de alunos que utilizaram o sistema.
• A média das notas da turma.'''

def verificar_respostas(respostas_aluno, gabarito):
    acertos = 0
    for i in range(len(gabarito)):
        if respostas_aluno[i] == gabarito[i]:
            acertos += 1
    return acertos

def main():
    gabarito = ['A', 'C', 'E', 'D', 'B', 'B', 'C', 'D', 'A', 'B']
    total_alunos = 0
    acertosaluno = []

    while True:
        total_alunos += 1
        respostas_aluno = []

        print(f"\nAluno {total_alunos}, por favor, insira suas respostas para as questões:")
        for i in range(10):
            resposta = input(f"Questão {i + 1}: ").strip().upper()
            respostas_aluno.append(resposta)

        acertos = verificar_respostas(respostas_aluno, gabarito)
        acertosaluno.append(acertos)
        print(f"Você acertou {acertos} de 10 questões.")

        continuar = input("Outro aluno deseja fazer a prova? (s/n): ").strip()
        if continuar != 's':
            break

    if total_alunos > 0:
        maior_acerto = max(acertosaluno)
        menor_acerto = min(acertosaluno)
        media_acertos = sum(acertosaluno) / total_alunos

        print(f"\nTotal de alunos que utilizaram o sistema: {total_alunos}")
        print(f"Maior número de acertos: {maior_acerto}")
        print(f"Menor número de acertos: {menor_acerto}")
        print(f"Média de acertos da turma: {media_acertos:.2f}")

if __name__ == "__main__":
    main()
