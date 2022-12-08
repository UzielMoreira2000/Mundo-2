'''
Exercício Python 065: Crie um programa que leia vários números
inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou
não continuar a digitar valores.
'''

termos = 0
cont   = 0
cond = 'S'
maior = 0
menor = 0

while cond in'Ss':

    n = int(input('Digite um numero :'))
    cond = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    cont += 1
    termos += n
    if cont == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if  n < menor :
           menor = n

media = termos / cont
print('Voce Digitou {} numeros e a media deles foi {:.2f}'.format(cont,media))
print('O maior valor lido foi {} e o menor valor lido foi {}'.format(maior , menor))
print('FIM')






