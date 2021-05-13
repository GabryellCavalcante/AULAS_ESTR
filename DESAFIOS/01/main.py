import random

print ("|===========SIMULADOR DE DADOS===========|")
print ("|DESEJA INICIAR O SIMULADOR ?|")
opcao = input()

while opcao in ("sim","ss","s","ok"):  
    if opcao in ("sim","ss","s","ok"):
        print(random.randrange(1,6))
        print ("|DESEJA JOGAR NOVAMENTE ?|")
        opcao = input ()