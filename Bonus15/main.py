from function import *

exibe_menu_principal()
print ("O que deseja fazer ?")
op = input()

if op == "1":
    pacientes = recebe_paciente()
else:
    print ("|=================OBRIGADO POR ACESSAR===============|")

registra_arquivo()

exibe_arquivo()