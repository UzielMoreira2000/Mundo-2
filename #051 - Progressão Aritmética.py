'''
Exercício Python 051: Desenvolva um programa que
leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''


i = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razao da PA:'))
n =  i + 11 * r           # n é o valor final que a progressão vai admitir inicio
for c in range(i, n, r):  # da PA + a razao vzs a quantidade de termos q se deseja exibir
    print(c)
print('FIM')


