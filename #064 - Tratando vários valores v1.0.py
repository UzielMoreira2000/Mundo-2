'''
Exercício Python 064: Crie um programa que leia vários números
inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a
soma entre eles (desconsiderando o flag).
'''

print('\n')

termos = 0
cont   = 0
saida  = 0
c = termos

while termos != 999 and saida == 0:

    termos = int(input('Digite o numero [999 para parar] :'))
    if termos == 999:
        saida = 1
        c -= 999
        cont -= 1
    c += termos
    cont += 1
    termos += termos

print('Voce Digitou {} numeros e a soma deles foi {}'.format(cont,c))
print('FIM')







