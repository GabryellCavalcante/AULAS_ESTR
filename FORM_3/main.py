tabuleiro = [[]]
casas = 17
print(("+"*23)+"O JOGO"+("+"*23))
print ("Quanto jogadores desejam jogar ? Máx.4")
quant = int(input())
if quant > 4:
    quant = 4
#Receber jogadores
jogadores = [""]
for l in range(1,quant+1):
    print("Qual o apelido do {}º jogador:".format(l))
    jogadores.append(input())#[0.2].upper())



#Iniciando Tabuleiro
for c in range(casas):
    tabuleiro[0].append(str(c).zfill(2))
for l in range (1,quant+1):
    raia = []
    for c in range(casas):
        raia.append("  ")
    tabuleiro.append(raia)

#exibindo tabuleiro
print(jogadores[1:quant+1])

print("-"*52)
for raia in tabuleiro:
    linha = ""
    for col in raia:
        linha += "|" + col
    linha += "|"
    print(linha)
    print("-"*52)

