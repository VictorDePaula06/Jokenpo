from time import sleep
import random

nome = str(input("Antes de começarmos o jogo, Digite seu nome: ")).upper()
print(f"Seja bem-vindo {nome}")

print('SUAS OPÇÕES:'
      '\n[0] PEDRA'
      '\n[1] PAPEL'
      '\n[2] TESOURA')

computador = random.randint(0,2)
jogador = int(input('Qual é a sua jogada? '))
if (jogador >= 0 and jogador <= 2):
      sleep(1)
      print('JO')
      sleep(1)
      print('KEN')
      sleep(1)
      print('PO')
      sleep(1)
else:
      if jogador < 0 or jogador > 2:
            print("OPÇÃO INVALIDA!!!")
            jogador = int(input('Tente novamente!\nQual é a sua jogada ?'))
            if jogador < 0 or jogador > 2:
                  print("Jogada inválida novamente,programa encerrado!")
            else:
                  sleep(1)
                  print('JO')
                  sleep(1)
                  print('KEN')
                  sleep(1)
                  print('PO')
                  sleep(1)


if computador == 0 and jogador == 1:
      print('=-='*20)
      print('computador jogou PEDRA')
      print(f'{nome} jogou PAPEL')
      print('=-=' * 20)
      print(f'{nome} VENCEU')
elif computador == 0 and jogador == 2:
      print('=-=' * 20)
      print('computador jogou PEDRA')
      print(f'{nome} jogou TESOURA')
      print('=-=' * 20)
      print('COMPUTADOR VENCEU')
elif computador == 1 and jogador == 0:
      print('=-=' * 20)
      print('computador jogou PAPEL')
      print(f'{nome} jogou PEDRA')
      print('=-=' * 20)
      print('COMPUTADOR VENCEU')
elif computador == 1 and jogador == 2:
      print('=-=' * 20)
      print('computador jogou PAPEL')
      print(f'{nome} jogou TESOURA')
      print('=-=' * 20)
      print(f'{nome} VENCEU')
elif computador == 2 and jogador == 0:
      print('=-=' * 20)
      print('computador jogou TESOURA')
      print(f'{nome} jogou PEDRA')
      print('=-=' * 20)
      print(f'{nome} VENCEU')
elif computador == 2 and jogador == 1:
      print('=-=' * 20)
      print('computador jogou TESOURA')
      print(f'{nome} jogou PAPEL')
      print('=-=' * 20)
      print('COMPUTADOR GANHOU')
elif computador == 0 and jogador == 0:
      print('EMPATE! AMBOS JOGARAM AS MESMAS OPÇÕES ')
elif computador == 1 and jogador == 1:
      print('EMPATE! AMBOS JOGARAM AS MESMAS OPÇÕES ')
elif computador == 2 and jogador == 2:
      print('EMPATE! AMBOS JOGARAM AS MESMAS OPÇÕES ')



