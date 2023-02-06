import os

def jogar():
    os.system("cls")
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "sertanejo"
    enforcou = False
    acertou = False
    qnt_letras = len(palavra_secreta)
    print("A palavra tem {} letras".format(qnt_letras))
    palavra_mostrada = []
    for qnt_letras in palavra_secreta:
        palavra_mostrada.append("_")
    print(palavra_mostrada)

    while(not enforcou and not acertou):
        
        palpite = input("Digite um palpite: ")
        palpite = palpite.strip()
        posicao = 1

        for letra in palavra_secreta:
            if(palpite.upper() == letra.upper() or palpite == letra):
                print("A letra {} faz parte da palavra na posição {}".format(palpite, posicao))
                palavra_mostrada[posicao-1] = letra
            posicao += 1
        print(palavra_mostrada)

        if(palavra_mostrada.count("_") == 0):
            print("Você ganhou!")
            break

    print("Fim do jogo")

if(__name__ == "__main__"):
  jogar()
