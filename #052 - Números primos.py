'''
Exercício Python 052: Faça um programa que leia
um número inteiro e diga se ele é ou não um número primo.

'''

letra ={'azulclaro': '\033[36m',
        'clean':     '\033[m'  }

n = int(input('Digite um numero:'))
cont = 0

for c in range(1, n+1):
    if n % c == 0:
        print('{}'.format(letra['azulclaro']),end='')
        cont += 1
    else:
        print(letra['clean'],end='')
    print(c,end='')

print('{}\nO numero {} foi divisivel {} vezes'.format(letra['clean'],n,cont))

if cont == 2:
    print('O numero {} é um numero primo'.format(n))
else:
    print('O numero {} não é um numero primo'.format(n))





