import csv
import os.path


pacientes = []
cabecalho = ["NOME","IDADE","PESO","ALTURA","IMC"]

def recebe_paciente():
    for c in range(10):
        print("Digite os dados do",c+1,"º paciente")
        paciente = {"NOME":"","IDADE":"","PESO":0.0,"ALTURA":0.0,"IMC":0.0}  
        for lb in paciente:
            print(lb+" DO PACIENTE ?")
            if lb == "IMC":
                paciente["IMC"] = round((paciente["PESO"]/paciente["ALTURA"]**2),2)
                print (paciente["IMC"])
            elif isinstance (paciente[lb],float):
                paciente[lb] = float(input())
            else:
                paciente[lb] = input()
        pacientes.append(paciente)
    return pacientes

def registra_arquivo():
    existe = os.path.exists("Bonus15\pacientes.csv")
    arquivo = open("Bonus15\pacientes.csv","a+")
    with arquivo as csvfile:
        arquivo = csv.DictWriter(csvfile, delimiter=";",fieldnames=cabecalho)
        if not existe:
            arquivo.writeheader()
        for paciente in pacientes:
            arquivo.writerow(paciente)

def exibe_arquivo():
    arquivo_novo = open("Bonus15\pacientes.csv","r")
    for linha in arquivo_novo:
        print(linha,end="")

def exibe_menu_principal():
    print("==========GREY SLOAN MEMORIAL HOSPITAL==========")
    print("|----------------------------------------------|")
    print("|---INSERIR_PACIENTES(1)---------SAIR(3)-------|")
    print("|----------------------------------------------|")