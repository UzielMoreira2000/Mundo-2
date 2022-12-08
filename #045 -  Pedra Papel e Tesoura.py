'''
Exercício Python 045: Crie um programa que
faça o computador jogar Jokenpô com você.
'''

from random import randint

print('Já jogou Jokenpô com uma IA? Vamos jogar ?!'
      '\nPeeeedra, papel, teeeesoura!!')

jogador = int(input('É assim ó: '
                   '\n[0] PEDRA'
                   '\n[1] PAPEL'
                   '\n[2] TESOURA'
                   '\nVai escolhe!!!:'))

lista = ('pedra','papel','tesoura')
ia = randint(0, 2)

if jogador == 0 or jogador == 1 or jogador == 2:
    print('\nEu escolhi {} e voce escolheu {}.'.format(lista[ia],lista[jogador]))

if jogador == ia:
    print('Empatamos ')

if jogador == 0 and ia == 1:
    print('Ganhei de voce !')
if jogador == 0 and ia == 2:
    print('Parabens voce ganhou !')

if jogador == 1 and ia == 0:
    print('Parabens voce ganhou !')
if jogador == 1 and ia == 2:
    print('Ganhei de voce !')

if jogador == 2 and ia == 0:
    print('Ganhei de voce !')
if jogador == 2 and ia == 1:
    print('Parabens voce ganhou !')

elif jogador > 2:
   print('\nPoxa {} nao vale...'.format(jogador))