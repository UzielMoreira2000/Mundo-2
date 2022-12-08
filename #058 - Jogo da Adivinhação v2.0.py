'''
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador
vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
'''

from random import randint

letra ={'clean':     '\033[m',
        'preto':     '\033[30m',
        'vermelho':  '\033[31m',
        'verde':     '\033[32m',
        'amarelo':   '\033[33m',
        'azul':      '\033[34m',
        'roxo':      '\033[35m',
        'azulclaro': '\033[36m',
        'cinza':     '\033[37m' }

lista = (0,10)
ia = randint(0, 11)
n = -1
tentativas = 0

print('\nOla sou seu computador...'
            '\nAcabe de pensar um numero entre 0 e 10.'
            '\nSerá que voce consegue adivinhar qual foi?')

while n != ia :

      n = int(input('Qual seu palpite? '))
      print('\nVoce escolheu {}{}{}'.format(letra['vermelho'],n,letra['clean']))
      tentativas += 1

      if n >= 11 or n <= -1:
            print('Este valor é invalido\n')
      else:
            if ia > n:
                  print('O valor é {}mais{} alto... tente outra uma vez\n'
                        .format(letra['vermelho'],letra['clean']))
            if ia < n:
                  print('O valor é {}menos{}... tente outra uma vez\n'
                        .format(letra['vermelho'],letra['clean']))

print('\n{}Parabens eu escolhi o numero {} !!! voce acertou com {} tentativas'
      .format(letra['verde'],ia,tentativas))