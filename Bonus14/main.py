def lista_paciente():
    arquivo = open("paciente.txt","r")  
    for l in arquivo.readlines():
        print(l[:-2])
    arquivo.close()

def adiciona_paciente():
    for p in range (10):
        print ()
        print ("|===DIGITE OS DADOS DO",p+1,"º PACIENTE===|")
        arquivo = open("paciente.txt","a+")
        paciente = {"NOME":"","IDADE":0,"PESO":0.0,"ALTURA":0.0,"IMC":0.0}
        for c in paciente:
            print ("|=",c,"DO PACIENTE=|")
            if c == "IMC":
                paciente["IMC"] = round((paciente["PESO"]/paciente["ALTURA"]**2),2)
                print (paciente["IMC"])
            elif isinstance (paciente[c],float):
                paciente[c] = float(input())
            else:
                paciente[c] = input()

        for c in paciente:
            arquivo.write(str(paciente[c])+"\t")
        arquivo.write("\n")
        arquivo.close()

print ("|============MEMORIAL HOSPITAL GREY SLOAN============|")
print ("|==============O QUE VOCE DESEJA FAZER ?=============|")
print ("|=======INSERIR(1)====================SAIR(2)========|")
opcao = input()

if opcao == "1":
    adiciona_paciente()
else:
    print ("|=================OBRIGADO POR ACESSAR===============|")