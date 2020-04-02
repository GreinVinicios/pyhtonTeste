print("***********")
print("Bem Vindo")
print("***********")

numero_secreto = 43
total_de_tentativas = 3

while(total_de_tentativas > 0):
    print("Ainda restam {} tentativas".format(total_de_tentativas))
    chute = input("Digite o seu nº: ")
    chute = int(chute)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Acertou")
        break
    else:
        if(maior):
            print("Errou! O seu chute foi maior do que o nº secreto!")
        elif(menor):
            print("Errou! O seu chute foi menor do que o nº secreto!")
    total_de_tentativas = total_de_tentativas - 1
    
print("Fim de jogo!")
