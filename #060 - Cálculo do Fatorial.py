'''
Exercício Python 060: Faça um programa que
leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

c = int(input('\nInsira um valor para calcular seu fatorial:'))
print('Calculando {}! ='.format(c), end=' ' )
f = 1
while c >= 1:
    print('{} '.format(c), end='')
    print('x ' if c> 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''
#Utilizando FOR
i = int(input('\nInsira um valor para calcular seu fatorial:'))
print('\nCalculando {}! ='.format(i),end=' ')
fat=1
for b in range(i, 1, -1): # decrementa de um em um
    print(b,'x',end=' ')
    fat *= b
print('= {}'.format(fat))

#Utilizando math
from math import  factorial
i = int(input('\nInsira um valor para calcular seu fatorial:'))
f = factorial(i)
print('\nfatorial de {} é {}'.format(i,f))
'''









