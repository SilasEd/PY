import advinhacao
import forca

def print_selecao():
    print("*********************************")
    print("********SELEÇÃO DE JOGOS*********")
    print("*********************************")

def escolha_jogador():
    print("Selecione qual jogo deseja jogar: \n")
    print("1 - Forca\n")
    print("2 - Advinhação\n")
    escolha = int(input("1 ou 2? "))
    return(escolha)

def entrada_jogo(game):
    if(game == 1):
        forca.jogar()
    else:
        advinhacao.jogar()

def menu():
    print_selecao()
    jogo = escolha_jogador()
    entrada_jogo(jogo)

if(__name__ == "__main__"):
    menu()