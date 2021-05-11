def lista_aluno():
    arquivo = open("alunos.txt","r")  
    for l in arquivo.readlines():
        print(l[:-2])
    arquivo.close()

def adiciona_aluno():
    arquivo = open("alunos.txt","a+")
    aluno = {"nome":"","peso":0.0,"altura":0.0,"modalidade":""}    
    for c in aluno:
        print(c.capitalize()+"?")
        if isinstance(aluno[c],float):
            aluno[c] = float(input())
        elif c == "modalidade":
            lista_modalidade()
            cod = input()
            aluno[c] = busca_modalidade(cod)
        else:
            aluno[c] = input()
        
    for c in aluno:
        arquivo.write(str(aluno[c])+"\t")
    arquivo.write("\n")
    arquivo.close()

def lista_modalidade():
    arquivo = open("modalidades.txt","r")  
    for l in arquivo.readlines():
        print(l[:-2])
    arquivo.close()

def adiciona_modalidade():
    arquivo = open("modalidades.txt","a+")
    modalidade = {"código":"000","nome":""}
    for c in modalidade:
        print(c.capitalize()+"?")
        modalidade[c] = input()
    for c in modalidade:
        arquivo.write(modalidade[c]+"\t")
    arquivo.write("\n")
    arquivo.close()

def busca_modalidade(cod):
    arquivo = open("modalidades.txt","r")
    nome_modalidade = "Não encontrada"
    for l in arquivo.readlines():
        modalidade = l[:-2].split("\t")
        if modalidade[0] == cod:
          nome_modalidade = modalidade[1]
    arquivo.close()    
    return nome_modalidade

op = ""
while op != "3":
    print("===========ACADEMIA SARADÃO=============")
    print("===ALUNO(1)===MODALIDADES(2)===SAIR(3)==")
    print("O que deseja acessar? (1 ou 2)")
    op = input()
    if op == "1":
        print("==========CADASTRO DE ALUNOS============")
        print("===========NOVO(1)====SAIR(3)===========")
        lista_aluno()
        op = input()
        if op == "1":
            adiciona_aluno()
    elif op == "2":
        print("========CADASTRO DE MODALIDADES=========")
        print("===========NOVO(1)====SAIR(3)===========")
        lista_modalidade()
        op = input()
        if op == "1":
            adiciona_modalidade()  

print("==========PROGRAMA FINALIZADO===========")