'''
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro
termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
'''

i = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razao da PA:'))
termos = 10
c = 0
adc = 1

while termos != 0 and adc != 0:

    n = i + (termos) * r
    while c < n:
        print(c, end=' -> ')
        c += r
    print('\nPAUSA !')

    adc = int(input('\nQuantos termos deseja mostrar a mais:'))
    termos += adc

print('\nforam exibidos {} termos !'.format(termos))
print('\nFIM !')







