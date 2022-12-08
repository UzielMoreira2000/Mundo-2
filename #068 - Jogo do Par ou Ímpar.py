'''
Exercício Python 068: Faça um programa que jogue par ou
ímpar com o computador. O jogo só será interrompido quando
o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.
'''

import random

while True:

    ia = random.randint(0, 10)
    jogador = int(input('Digite um valor:'))
    tipo = ' '
    cont = 0
    s = ia + jogador

    while tipo not in 'PI':
        tipo = str(input('Voce quer Par ou Impar?[i/p]')).strip().upper()[0]

    print('=' * 15)
    print(f'\nEu escolhi {ia} e voce escolheu  {jogador} , {ia} + {jogador} = {s} .\n')

    if tipo == 'P':
        if s % 2 == 0:
            print(' venceu!')
            print('=' * 15, '\n')
            cont += 1
        else:
            print('voce perdeu!')
            print('=' * 15, '\n')
            break

    elif tipo == 'I':
        if s % 2 == 1:
            print('voce venceu!')
            print('=' * 15, '\n')
            cont += 1
        else:
            print(' voce perdeu!')
            print('=' * 15, '\n')
            break

    print('Vamos jogar novamente...\n')

print(f'GAME OVER! Voce venceu {cont} vezes...')








