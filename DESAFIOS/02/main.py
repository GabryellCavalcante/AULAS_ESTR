import random

numero = (random.randrange(1,5))
chute = 0

while chute != numero:
    print ("Qual número você acha que foi gerado ?")
    chute = int(input())

    if chute < numero:
        print ("O seu chute foi menor que o número !")
        print ("====================================")
    elif chute > numero:
        print("Seu chute foi maior que o número !")
        print ("=================================")
    elif chute == numero:
        print ("Acertou Mizeravi !")
        print ("==================")