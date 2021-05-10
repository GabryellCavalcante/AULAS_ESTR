from Aditivos.add import *

teste()

turma = []
for c in range(2):
    estudante = Aluno()
    print(c+1,"º Aluno:")
    print("Qual o nome?")
    estudante.nome = input()
    print("Qual a N1?")
    estudante.n1 = float(input())
    print("Qual a N2?")
    estudante.n2 = float(input())
    estudante.media = (estudante.n1+estudante.n2)/2
    turma.append(estudante)
    print()

for aluno in turma:
    print("-"*60)
    print("Nome:",aluno.nome,end=" | ")
    print("N1:",aluno.n1,end=" | ")
    print("N2:",aluno.n2,end=" | ")
    print("Média:",media(aluno.n1,aluno.n2),end=" | ")
    print("Status:",end=" ")
    situacao(media(aluno.n1,aluno.n2))