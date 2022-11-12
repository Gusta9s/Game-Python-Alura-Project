import Forca #Importando um modulo.
import Numero

def escolhe():
    print("\n*********\n")
    print("Escolha o jogo que você deseja!.\n")
    print("*********\n")

    print("Digite (1) para o jogo da forca; (2) para o jogo de acerte o número.\n")
    a = int(input("Digite 1 ou 2 aqui: "))

    if(a == 1):
        print("\nIniciando o jogo da forca...\n")
        Forca.jogar() #Força o inicio do programa, a partir do comando, da função.

    elif(a == 2):
        print("\nIniciando o jogo de acerte o número...\n")
        Numero.jogar()

if(__name__ == "__main__"):
    escolhe()
