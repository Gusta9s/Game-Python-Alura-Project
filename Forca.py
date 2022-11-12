from random import randrange

def jogar():

    imprime_abertura()
    
    palavra_secreta = gera_palavra_secreta() # Palavra secreta recebe a função.

    letras_acertadas = gera_letras_acertadas(palavra_secreta) # Letras acertadas recebe a função.
    print(letras_acertadas)

    enforcado = False
    acertou = False
    erros = 0

    

    while(not enforcado and not acertou): #not, porta inversora.
        chute = armazena_chute() # Chute recebe a função.

        if(chute in palavra_secreta):
            chute_correto(chute,letras_acertadas,palavra_secreta) # São mostrados parâmetros necessários para a função funcionar corretamente.
        
        else:
            erros += 1 #Contador de erros.
            forca(erros)
        
        enforcado = erros == 7 #Numero maximo de erros permitidos.
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        vencedor()
    else:
        perdedor(palavra_secreta)
        

    print("\n Fim do jogo!.\n\n ---------------------------------------------------") 

def imprime_abertura():
    
    print("\n*********\n")
    print("Bem vindo ao jogo da forca.\n")
    print("*********\n")
    print("Para você vencer este jogo, é nescessario que descubra qual é a palavra secreta. \n\n Existem quatro marcas famosas de equipamentos computacionais para serem descobertos com este desafio. \n\n Boa sorte.\n\n")

def gera_palavra_secreta():
    
    with open("conjunto.txt","r") as arquivo: # Função arquivo, para abrir a lista com as palavras secretas, with vai encerrar o arquivo automaticamente sem prescisar de declaração.

        palavras = [] # Armazenador de linhas (das palavras secretas)
        
        for linha in arquivo:
            linha = linha.strip() # Retira todos os \n que tiram a formatação nescessaria para armazenamento.
            palavras.append(linha) # Adiciona as palavras(linhas) na lista armazenadora.

        #arquivo.close() --> Encerra o arquivo em execução.

    nu = randrange(0,len(palavras)) # Escolhe aleatoriamente as palavras na lista, desde o primeiro item(indice 0) ate o seu comprimento final(len(para identificar automaticamente o tamanho da lista)).

    palavra_secreta = palavras[nu].upper() # Palavra secreta recebe lista palavras na ordem [nu] e Upper transfora todas as letra da variavel em maiusculas. 

    return(palavra_secreta)

def gera_letras_acertadas(palavra_secreta):
    list = ["_" for letra in palavra_secreta]  # Para criar uma lista de caracteres ("_") para a palavra secreta, de forma dinamica. (Automatica)
    return list

def armazena_chute():
    
    chute = str(input("Digite uma letra: "))
    print("\n")
    chute = chute.strip().upper() # Strip - Tira todos os espaçamentos selecionados.
    return chute

def chute_correto(chute,letras_acertadas,palavra_secreta):
    
    index = 0 # Ele vai dar a posição da nossa palavra.

    for letra in palavra_secreta: #letra vai prencher a variavel palavra_secreta.
        if(chute == letra): 
                                                    #print("Encontramos a letra {}, na posição {}.".format(letra,index))
            letras_acertadas[index] = letra #Ele vai fazer o anexo das letras acertadas, dentro da nossa palavra secreta.
        index += 1 # Ele vai rodar nosso index, ate mostrar todas as letras encontradas da palavra.

def vencedor():
    print("\n---------------------------------------------------")
    print("\n Parabéns, você venceu este jogo.\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def perdedor(palavra_secreta):
    print("\n---------------------------------------------------")
    print("\n Mas que pena, você perdeu, tente novamente. \n")
    print("\n A palavra era {} \n".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def forca(erros):
    print("\n  _______     ")
    print(" |/      |    \n")

    if(erros == 1):
        print("\n |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            \n")

    if(erros == 2):
        print("\n |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            \n")

    if(erros == 3):
        print("\n |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            \n")

    if(erros == 4):
        print("\n |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            \n")

    if(erros == 5):
        print("\n |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            \n")

    if(erros == 6):
        print("\n |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     \n")

    if (erros == 7):
        print("\n |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   \n")

    print("\n |            ")
    print("_|___         \n")
    print()


if(__name__ == "__main__"):
    jogar()
