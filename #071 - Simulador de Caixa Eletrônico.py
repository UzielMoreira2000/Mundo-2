'''
Exercício Python 071: Crie um programa que simule o funcionamento
e um caixa eletrônico. No início, pergunte ao usuário qual será
o valor a ser sacado (número inteiro) e o programa vai informar
quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print('=' * 14, '\n  BANCO CEV\n', end='='* 14)

valor = int(input('\nQue valor voce deseja sacar? : '))

var50 = int(valor / 50)
var20 = int((valor % 50) /20)
var10 = int((valor % 20) /10)
var1  = int((valor % 10))

if valor > 50:

    var10 = int((valor % 20) / 10)

while True:

    while valor <= 0:
         valor = int(input('\nQue valor voce deseja sacar? : '))

    if var50 > 0:
        print(f'Total de {var50} celulas de R$50')

    if var20 > 0:
        print(f'Total de {var20} celulas de R$20')

    if var10 > 0 :
        print(f'Total de {var10} celulas de R$10')

    if var1 > 0:
        print(f'Total de {var1} celulas de R$1')

    total = var1 + var10 * 10 + var20 * 20 + var50 * 50

    print(f'\nO total é R${total:.2f}')

    break

print('\nVolte sempre ao BANCO CEV tenha um bom dia!')


















