'''
Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição
de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre elas (desconsiderando o flag).
'''

termos = 0
cont   = 0
s = 0
# laço infinito, interompido apenas pelo break
while True:
    n = int(input('Digite um numero :'))

    termos += n
    #laço é interompido caso a condição seja verdadeira
    if n == 999:
        break  # imterompe o while
    cont += 1
    s += n
print(f'Voce Digitou {cont} numeros, a soma dos numeros é {s}')
print('FIM')






