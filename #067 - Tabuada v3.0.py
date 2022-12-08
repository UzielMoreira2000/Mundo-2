'''
Exercício Python 067: Faça um programa que mostre a tabuada de vários
números, um de cada vez, para cada valor digitado pelo usuário. O programa
será interrompido quando o número solicitado for negativo.
'''

c = 1
while True:

    n = int(input('Deseja ver a tabuada de qual valor?:'))
    if n < 0 :
            break
    print('-' * 20)
    while c <= 10:
         print(f'{n} x {c} = {n * c}')
         c += 1
    if c == 11:
         c = 1
    print('-' * 20)
print('Valor menor que 0 inserido ...Programa encerrado ...')






