from random import randrange

def jogar():
    print("\n*********\n")
    print("Bem vindo ao jogo, de acerte o numero.\n")
    print("*********\n")

    chute = 0
    numero_secreto = randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade do jogo, você deseja?. (digite: (1) -> para nível fácil; (2) -> para nível médio; (3) -> para nível difícil.)\n")
    nivel = int(input("Digite o número 1,2 ou 3 aqui: "))
    print("\n*********\n")

    if (nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas = 5
    elif(nivel == 3):
        total_tentativas = 3
    else:
        print("\nDigite um número entre 1 a 3, para iniciar o jogo.\n")
        total_tentativas = 0

    for rodada in range(1,total_tentativas + 1):
        print("Tentativa {} de {}.\n".format(rodada,total_tentativas))
        chute = int(input("Digite um número entre 1 a 100: "))

        if(chute < 1 or chute > 100):
            print("\nDigite um número entre 1 a 100. Tente novamente.\n\n---------\n")
            continue

        if(chute == numero_secreto):
            print("\nVocê acertou e fez {} pontos, parabens!.\n\n---------\n".format(pontos))
            break

        else:
            if(chute < numero_secreto):
                print("\nVocê errou!. Seu chute foi menor, do que o número esperado.\n\n---------\n")
            elif(chute > numero_secreto):
                print("\nVocê errou!. Seu chute foi maior, do que o número esperado.\n\n---------\n")
            
            pontos_perdidos = round(abs(numero_secreto - chute) / 3) #Subtraí a diferença entre numero_secreto e chute, ou seja, será chute - numero_secreto. ex: 1,2,3-55 -> 1-55=-54; 2-55=-53; 3-55=-52 -> 54 + 53 + 52 = -159 -> 1000 - 159 = 841 pontos!.
            pontos = pontos - pontos_perdidos
        

    print("Fim do jogo!.\n")

if(__name__ == "__main__"): #Chama a variavel a funcionar individualmente.
    jogar()