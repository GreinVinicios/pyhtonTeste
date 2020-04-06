import random;


def jogar():
    print("***********")
    print("Bem Vindo")
    print("***********")

    numero_secreto = random.randint(0, 100);
    pontos = 1000

    print("Selecione a dificuldade");
    print("1 - Fácil");
    print("2 - Médio");
    print("3 - Difícil");
    nivel = int(input("Digite: "));

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5;

    for i in range(1, total_de_tentativas + 1):
        print("Ainda restam {} tentativas".format(total_de_tentativas))
        chute = input("Digite o seu nº: ")
        chute = int(chute)

        total_de_tentativas = total_de_tentativas - 1

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Acertou")
            break
        else:
            if (maior):
                print("Errou! O seu chute foi maior do que o nº secreto!")
            elif (menor):
                print("Errou! O seu chute foi menor do que o nº secreto!")
        pontos = pontos - 10

    if not (acertou):
        print(numero_secreto)
    else:
        print("Sua pontuação foi de: {} pontos!".format(pontos));

    print("Fim de jogo!")
