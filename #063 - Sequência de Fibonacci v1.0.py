'''
Exercício Python 063: Escreva um programa que leia
um número N inteiro qualquer e mostre na tela os N
primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
'''

n = int(input('Digite o primeiro termo da sequencia :'))
termos = int(input('\nQuantos termos deseja mostrar :'))
c  = 3
t1 = 0
t2 = 1

print('{} -> {} ->'.format(t1,t2), end=' ')

while c < termos:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')







