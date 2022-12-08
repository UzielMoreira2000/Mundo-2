'''
Exercício Python 046: Faça um programa que mostre na tela uma contagem
regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.

for c in range(0, 100, 2):
    print(c, end=' ')
print('\nFIM!')
'''
for c in range(0, 50):
    if c % 2 == 0:
        print(c, end=' ')
print('\nFIM!')

'''
i = int(input('inicio da contagem:'))
f = int(input('fim da contagem:'))

for c in range(i, f):
    if c % 2 == 0:
        print(c, end=' ')
print('\nFIM!')
'''




