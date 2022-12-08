'''
Exercício Python 059: Crie um programa que
leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

letra ={'vermelho':'\033[31m', 'clean':'\033[m'}
i = 0

while i != 5 or i == 4 :

    n1 = int(input('\nInsira o primeiro valor:'))
    n2 = int(input('Insira o segundo valor :'))
    i= int(input('Oque deseja fazer com esse dois valor?'
                 '\nInforme uma das opções abaixo: '
                        '\n[1] Somar'
                        '\n[2] Multiplicar'
                        '\n[3] Maior'
                        '\n[4] novos numeros'
                        '\n[5] Sair do programa:'))
    if 1 < i > 5 or i ==0:
        print('\n{}ERRO..."{}" nao é uma opção valida{} \n'
              .format(letra['vermelho'],i,letra['clean']))
    else:
          if i == 1:
                n = n1 + n2
                print('\nA soma de {} + {} = {}'.format(n1,n2,n))
          if i == 2:
              n = n1 * n2
              print('\nA multiplicação de {} x {} = {}'.format(n1, n2, n))
          if i == 3:
              if n1 > n2:
                print('\n{} é maior que {}'.format(n1, n2))
              else:
                print('\n{} é maior que {}'.format(n2, n1))

print('\nPrograma encerrado.')