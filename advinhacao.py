import random

def jogar():  
  print("**************************************")
  print("***Bem vindo ao jogo da Advinhação!***")
  print("**************************************")
  
  numero_tentativas = 0
  numero_secreto = random.randrange(1,101)
  pontos = 1000
  
  nivel_str = input("Qual nivel você deseja jogar (1) fácil (2) normal (3) dificil: ")
  nivel = int(nivel_str)
  
  facil   = nivel == 1
  normal  = nivel == 2
  
  if(facil):
    numero_tentativas = 10
  elif(normal):
    numero_tentativas = 7
  else:
    numero_tentativas = 5
    
  for rodada in range(1, numero_tentativas+1, 1):
    print("Tentativa {}".format(rodada))
    
    chute_str = input("Digite um valor de 1 a 100: ")
    chute = int(chute_str)
    if(chute < 1 or chute > 100):
      print("Você deve digitar um valor de 1 a 100")      
      continue
  
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
  
    if(acertou):
      print("Parabéns, você acertou! O número secreto era {} e sua pontuação final foi {}!".format(numero_secreto,pontos))
      break
    else:
      
        pontos_perdidos = int(abs(numero_secreto - chute)/3)
        pontos -= pontos_perdidos
      
        if(maior):
          print("O número digitado é maior que o número secreto")
          if(rodada == numero_tentativas):
            print("O número secreto era {}, você fez {}".format(numero_secreto, pontos))
          else:
            print("A sua pontuação atual é {}".format(pontos))
            
        else:
          print("O número digitado é menor que o número secreto")
          if(rodada == numero_tentativas):
            print("O número secreto era {}, você fez {}".format(numero_secreto, pontos))
          else:
            print("A sua pontuação atual é {}".format(pontos))
  print("Fim de Jogo")
        
if(__name__ == "__main__"):
  jogar()
