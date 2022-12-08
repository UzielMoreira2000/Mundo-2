'''
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro
termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
'''

i = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razao da PA:'))
n =  i + 11 * r
while i < n:
    print(i,end=' -> ')
    i += r
print('FIM!')










